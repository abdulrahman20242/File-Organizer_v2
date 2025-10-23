أنا آسف جداً لوجود سوء فهم. أنا لم أحذفه والله.

الرابط الذي أرسلته أنت في رسالتك الأخيرة هو الرابط **القديم** (الذي ينتهي بـ `File-Organizer_v2`).

في ردي السابق، أنا استخدمت الرابط **الجديد** الذي أعطيتني إياه (الذي ينتهي بـ `File-Organizer_v2.1`).

الملف الذي أرسلته لك في الرد السابق يحتوي على هذا السطر بالضبط:
`![Sortify Screenshot](https://raw.githubusercontent.com/abdulrahman20242/File-Organizer_v2.1/main/Capture.PNG)`

كما تراه، الرابط موجود ويشير إلى المستودع الجديد `File-Organizer_v2.1`.

سأرسل لك محتوى الملف مرة أخرى. الرابط موجود في السطر الخامس، ولم أقم بحذفه.

-----

# 📂 Sortify - Advanced File Organizer

A powerful and user-friendly desktop application built with Python and PySide6 to intelligently sort your files into clean, organized folders.

Tired of cluttered "Downloads" or "Desktop" folders? Sortify automates the cleaning process with a rich set of features, a multi-language interface, and robust safety mechanisms like Undo and Dry-run mode.

## 

## 🚀 Features

### Core Functionality

  * **Multiple Organization Modes:**
      * **By Type:** Groups files into folders like `Images`, `Videos`, `Documents`.
      * **By Name:** Creates a dedicated folder for each file.
      * **By Date:** Sorts files into `Year/Month` folders (e.g., `2025/10-October`).
      * **By Day:** Sorts files into `Year/Month/Day` folders (e.g., `2025/10/16`).
      * **By Size:** Categorizes files as `Small`, `Medium`, or `Large`.
      * **By First Letter:** Groups files into alphabetical folders (`A`, `B`, `C`...).
  * **Flexible Actions:** Choose to **Move** original files or create a **Copy**.
  * **Smart Conflict Resolution:** Automatically `Rename`, `Overwrite`, or `Skip` files if they already exist in the destination.
  * **Recursive Processing:** Option to include all files from subdirectories in the organization process.

### User Experience & Interface

  * **Modern GUI:** Clean and intuitive interface built with PySide6.
  * **Easy Windows Launch:** Includes a `Sortify.bat` script for double-click execution.
  * **Real-time Progress:** A progress bar shows the status of organizing and undoing operations, ensuring the app never freezes.
  * **Detailed Results Table:** See the status of each file (Success, Skipped, Failed) in a clear, color-coded table.
  * **Multi-language Support:** Switch between **English** and **Arabic** on the fly.
  * **Themes:** Instantly switch between **Light** and **Dark** modes.
  * **Drag & Drop:** Easily drop your source folder into the path input field.

### Safety & Customization

  * **Undo Last Operation:** A critical safety feature\! Revert the entire last organization process with a single click.
  * **Dry-run Mode:** A simulation mode that creates the target folder structure **without touching your files**, allowing you to preview the result safely.
  * **Profiles:** Save and load your favorite settings (e.g., "Sort Downloads" vs. "Backup Photos") for quick reuse.
  * **Editable Categories:** Full control to add, remove, or rename categories and their associated file extensions **directly from the app's interface**.

-----

## 🛠️ Installation

1.  Clone the repository to your local machine using Git:

    ```bash
    git clone https://github.com/abdulrahman20242/File-Organizer_v2.1.git
    ```

    Then, navigate into the newly created project directory:

    ```bash
    cd File-Organizer_v2.1
    ```

2.  Make sure you have a compatible Python version installed (Python 3.12 is recommended for best library compatibility).

3.  Install the required libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

-----

## 🖥️ Usage

You can run the application in two ways:

1.  **From the terminal (all platforms):**

    ```bash
    python file_organizer_gui.py
    ```

2.  **On Windows (easy method):**
    Simply double-click the **`Sortify.bat`** file.

**How it works:**

1.  **Select Source & Destination:** Use the "Browse" buttons or drag-and-drop a folder into the "Source Folder" field. If the destination is left empty, a folder named `Organized_Files` will be created inside the source.
2.  **Choose Your Options:** Select the organization mode, action (move/copy), and conflict policy from the dropdowns.
3.  **Run:** Click the "Run" button to start the process.
4.  **Monitor:** Watch the progress bar and view live logs or results in the tabbed view.
5.  **Undo (if needed):** If you're not happy with the result, simply click the "Undo" button.

-----

## ⚙️ Customization

You have full control over the file categories. You can:

1.  **Use the GUI:** Click the **"Manage Categories"** button in the app to visually add, rename, or remove categories and their associated file extensions.
2.  **Edit Manually:** You can also directly edit the **`categories.json`** file. For example, to add `.eps` files to the "Images" category, simply add it to the list:

<!-- end list -->

```json
{
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic", ".eps"],
  "Videos": [...]
}
```

-----

## 🧪 Running Tests

This project includes a comprehensive test suite to ensure the core logic is working correctly. To run the tests:

1.  Install the development dependencies from `requirements-dev.txt`:
    ```bash
    pip install -r requirements-dev.txt
    ```
2.  Run pytest from the project's root directory:
    ```bash
    pytest -v
    ```

-----

## 📒 Project Structure

  * `file_organizer.py`: Contains all the backend logic for file operations.
  * `file_organizer_gui.py`: The main file for the PySide6 graphical user interface.
  * `Sortify.bat`: A simple batch script for launching the GUI on Windows.
  * `translations.json`: Stores text strings for multi-language support.
  * `categories.json`: Default and user-customizable file type categories.
  * `test_organizer.py`: The `pytest` test suite for the backend logic.
  * `requirements.txt`: Main dependencies required to run the application.
  * `requirements-dev.txt`: Extra dependencies for development and testing.
