# test_organizer.py (النسخة النهائية مع الاختبار المحدث)
import pytest
from pathlib import Path
import os
import datetime
import shutil
import logging

import file_organizer

# ------------------- الإعداد للاختبارات (Test Fixtures) -------------------

@pytest.fixture
def test_environment(tmp_path):
    source_dir = tmp_path / "source"
    dest_dir = tmp_path / "dest"
    source_dir.mkdir()
    (source_dir / "image.jpg").touch()
    (source_dir / "document.pdf").write_text("old content")
    (source_dir / "archive.zip").touch()
    (source_dir / "unknown.xyz").touch()
    (source_dir / "small_file.txt").write_text("small")
    (source_dir / "medium_file.bin").write_bytes(b'\0' * (2 * 1024 * 1024))
    (source_dir / "Alpha.txt").touch()
    (source_dir / "123_numeric.log").touch()
    sub_dir = source_dir / "subfolder"
    sub_dir.mkdir()
    (sub_dir / "nested_video.mp4").touch()
    yield source_dir, dest_dir

# ------------------- 1. اختبارات أوضاع التنظيم (Organization Modes) -------------------

def test_organize_by_type(test_environment):
    source, dest = test_environment
    params = {"source": source, "dest": dest, "mode": "type", "action": "move", "recursive": False, "conflict_policy": "rename", "dry_run": False, "categories": file_organizer.DEFAULT_CATEGORIES}
    result = file_organizer.process_directory(**params)
    assert result["succeeded"] == 8
    assert (dest / "Images" / "image.jpg").exists()
    assert (dest / "Documents" / "document.pdf").exists()

def test_organize_by_name(test_environment):
    source, dest = test_environment
    file_to_test = source / "Alpha.txt"
    file_organizer.organize_by_name(file_to_test, dest, action="move", conflict_policy="rename", dry_run=False)
    assert (dest / "Alpha" / "Alpha.txt").exists()
    assert not file_to_test.exists()

def test_organize_by_date(tmp_path):
    source, dest = tmp_path / "source", tmp_path / "dest"
    source.mkdir()
    test_file = source / "file_from_past.txt"
    test_file.touch()
    past_date = datetime.datetime(2023, 10, 26)
    m_time = past_date.timestamp()
    os.utime(test_file, (m_time, m_time))
    file_organizer.organize_by_date(test_file, dest, action="move", conflict_policy="rename", dry_run=False)
    expected_path = dest / "2023" / "10-October" / "file_from_past.txt"
    assert expected_path.exists()

def test_organize_by_size(test_environment):
    source, dest = test_environment
    file_organizer.organize_by_size(source / "small_file.txt", dest, action="copy", conflict_policy="rename", dry_run=False)
    file_organizer.organize_by_size(source / "medium_file.bin", dest, action="copy", conflict_policy="rename", dry_run=False)
    assert (dest / "Small (Under 1MB)" / "small_file.txt").exists()
    assert (dest / "Medium (1-100MB)" / "medium_file.bin").exists()

def test_organize_by_first_letter(test_environment):
    source, dest = test_environment
    file_organizer.organize_by_first_letter(source / "Alpha.txt", dest, action="copy", conflict_policy="rename", dry_run=False)
    file_organizer.organize_by_first_letter(source / "123_numeric.log", dest, action="copy", conflict_policy="rename", dry_run=False)
    assert (dest / "A" / "Alpha.txt").exists()
    assert (dest / "#" / "123_numeric.log").exists()

# ------------------- 2. اختبارات سياسات التعارض (Conflict Policies) -------------------

def test_conflict_policy_rename(test_environment):
    source, dest = test_environment
    dest_docs_dir = dest / "Documents"; dest_docs_dir.mkdir(parents=True)
    (dest_docs_dir / "document.pdf").touch()
    file_organizer.organize_by_type(source / "document.pdf", dest, action="copy", conflict_policy="rename", dry_run=False, ext_index=file_organizer.build_ext_index(file_organizer.DEFAULT_CATEGORIES))
    assert (dest_docs_dir / "document.pdf").exists()
    assert (dest_docs_dir / "document (1).pdf").exists()

def test_conflict_policy_skip(test_environment):
    source, dest = test_environment
    dest_docs_dir = dest / "Documents"; dest_docs_dir.mkdir(parents=True)
    (dest_docs_dir / "document.pdf").write_text("original")
    original_mtime = (dest_docs_dir / "document.pdf").stat().st_mtime
    result = file_organizer.organize_by_type(source / "document.pdf", dest, action="copy", conflict_policy="skip", dry_run=False, ext_index=file_organizer.build_ext_index(file_organizer.DEFAULT_CATEGORIES))
    assert result is None
    assert (dest_docs_dir / "document.pdf").read_text() == "original"
    assert (dest_docs_dir / "document.pdf").stat().st_mtime == original_mtime

def test_conflict_policy_overwrite(test_environment):
    source, dest = test_environment
    dest_docs_dir = dest / "Documents"; dest_docs_dir.mkdir(parents=True)
    (dest_docs_dir / "document.pdf").write_text("original")
    file_organizer.organize_by_type(source / "document.pdf", dest, action="copy", conflict_policy="overwrite", dry_run=False, ext_index=file_organizer.build_ext_index(file_organizer.DEFAULT_CATEGORIES))
    assert (dest_docs_dir / "document.pdf").read_text() == "old content"

# ------------------- 3. اختبارات الخيارات والحالات الخاصة (Options & Edge Cases) -------------------

def test_empty_source_folder(tmp_path):
    source, dest = tmp_path / "source", tmp_path / "dest"
    source.mkdir()
    result = file_organizer.process_directory(source=source, dest=dest, mode="type", action="move", recursive=False, conflict_policy="rename", dry_run=False)
    assert result["total"] == 0
    assert result["succeeded"] == 0
    assert not dest.exists() or len(list(dest.glob("*"))) == 0

def test_recursive_option(test_environment):
    source, dest = test_environment
    result = file_organizer.process_directory(source=source, dest=dest, mode="type", action="move", recursive=True, conflict_policy="rename", dry_run=False, categories=file_organizer.DEFAULT_CATEGORIES)
    assert result["succeeded"] == 9
    assert (dest / "Videos" / "nested_video.mp4").exists()
    assert (source / "subfolder").exists()
    assert len(list((source / "subfolder").iterdir())) == 0

def test_dry_run_option(test_environment, caplog):
    """الاختبار 3.3 المحدث: هل يقوم 'dry_run=True' بإنشاء المجلدات دون نقل الملفات؟"""
    source, dest = test_environment
    
    with caplog.at_level(logging.INFO):
        result = file_organizer.process_directory(source=source, dest=dest, mode="type", action="move", recursive=True, conflict_policy="rename", dry_run=True, categories=file_organizer.DEFAULT_CATEGORIES)

    assert result["succeeded"] == 9
    
    # التأكيد على أن الملفات لم يتم نقلها
    assert (source / "image.jpg").exists()
    assert (source / "subfolder" / "nested_video.mp4").exists()
    
    # التأكيد على أن هيكل المجلدات تم إنشاؤه
    assert dest.exists()
    assert (dest / "Images").is_dir()
    assert (dest / "Videos").is_dir()
    
    # التأكيد على أن المجلدات في الوجهة فارغة
    assert not any(dest.rglob("*.*"))

    assert "[DRY-RUN]" in caplog.text

def test_source_is_destination(test_environment):
    source, _ = test_environment
    files = file_organizer.list_files(source, recursive=True, exclude_dir=source)
    assert len(files) == 0