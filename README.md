# 📂 Sortify - Advanced File Organizer

A powerful and user-friendly desktop application built with Python and PySide6 to intelligently sort your files into clean, organized folders.

Tired of cluttered "Downloads" or "Desktop" folders? Sortify automates the cleaning process with a rich set of features, a multi-language interface, and robust safety mechanisms like Undo and Dry-run mode.

`![Sortify Screenshot]([blob:https://github.com/5e69c052-5396-4ebd-9dcd-6f32d6887659](https://raw.githubusercontent.com/abdulrahman20242/File-Organizer_v2/main/Capture.PNG)`

---

## 🚀 Features

### Core Functionality
*   **Multiple Organization Modes:**
    *   **By Type:** Groups files into folders like `Images`, `Videos`, `Documents`.
    *   **By Name:** Creates a dedicated folder for each file.
    *   **By Date:** Sorts files into `Year/Month` folders.
    *   **By Size:** Categorizes files as `Small`, `Medium`, or `Large`.
    *   **By First Letter:** Groups files into alphabetical folders (`A`, `B`, `C`...).
*   **Flexible Actions:** Choose to **Move** original files or create a **Copy**.
*   **Smart Conflict Resolution:** Automatically `Rename`, `Overwrite`, or `Skip` files if they already exist in the destination.
*   **Recursive Processing:** Option to include all files from subdirectories in the organization process.

### User Experience & Interface
*   **Modern GUI:** Clean and intuitive interface built with PySide6.
*   **Real-time Progress:** A progress bar shows the status of organizing and undoing operations, ensuring the app never freezes.
*   **Detailed Results Table:** See the status of each file (Success, Skipped, Failed) in a clear, color-coded table.
*   **Multi-language Support:** Switch between **English** and **Arabic** on the fly.
*   **Themes:** Instantly switch between **Light** and **Dark** modes.
*   **Drag & Drop:** Easily drop your source folder into the path input field.

### Safety & Customization
*   **Undo Last Operation:** A critical safety feature! Revert the entire last organization process with a single click.
*   **Dry-run Mode:** A simulation mode that creates the target folder structure **without touching your files**, allowing you to preview the result safely.
*   **Profiles:** Save and load your favorite settings (e.g., "Sort Downloads" vs. "Backup Photos") for quick reuse.
*   **Editable Categories:** Full control to add, remove, or rename categories and their associated file extensions directly through the `categories.json` file.

---

## 🛠️ Installation

1.  Clone or download this repository.
2.  Make sure you have **Python 3.13+** installed.
3.  Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🖥️ Usage

Run the graphical application from your terminal:

```bash
python file_organizer_gui.py
```

**How it works:**

1.  **Select Source & Destination:** Use the "Browse" buttons or drag-and-drop a folder into the "Source Folder" field. If the destination is left empty, a folder named `Organized_Files` will be created inside the source.
2.  **Choose Your Options:** Select the organization mode, action (move/copy), and conflict policy from the dropdowns.
3.  **Run:** Click the "Run" button to start the process.
4.  **Monitor:** Watch the progress bar and view live logs or results in the tabbed view.
5.  **Undo (if needed):** If you're not happy with the result, simply click the "Undo" button.

---

## ⚙️ Customization

You can easily customize which file extensions belong to which category by editing the **`categories.json`** file. For example, to add `.eps` files to the "Images" category, simply add it to the list:

```json
{
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".eps"],
  "Videos": [...]
}
```

---

## 🧪 Running Tests

This project includes a comprehensive test suite to ensure the core logic is working correctly. To run the tests:

1.  Install the development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```
2.  Run pytest from the project's root directory:
    ```bash
    pytest -v
    ```

---

## 📒 Project Structure

*   `file_organizer.py`: Contains all the backend logic for file operations (listing, moving, organizing, undoing). It has no dependency on the GUI.
*   `file_organizer_gui.py`: The main file for the PySide6 graphical user interface.
*   `translations.json`: Stores the text strings for multi-language support (English & Arabic).
*   `categories.json`: Default and user-customizable file type categories.
*   `test_organizer.py`: The `pytest` test suite for the backend logic.
*   `requirements.txt`: Project dependencies.
