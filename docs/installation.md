# Installation Guide

This guide will help you install and set up the File Organization Tool on your system.

## Requirements

- **Python**: 3.7 or higher
- **tkinter**: (usually included with Python)
- **PyInstaller**: for building executables (Optional)

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 512MB (1GB recommended)
- **Storage**: 50MB free space

## Quick Installation

### Method 1: Direct Download and Run

 **Download the repository:**

## Running the GUI Application
 **Clone or download the repository from GitHub.**

  **Open a terminal or command prompt and navigate to the project folder containing file_organizer.py:**

 **Terminal:**
 -          cd path/to/file-organization-tool

 **Terminal:**
 -          python file_organizer.py

 **On some systems, use python3 instead of python.**

**The modern file organization GUI window will open, letting you browse folders and organize files.**

# Optional: Running as an Installed Package
 **If you have installed the package locally using setup.py, you can run the GUI via the command line:**

-   **Terminal:**
-                 file-organizer-gui

 **Optional: Build Standalone Executable (Windows, Linux, macOS)**
 **Install PyInstaller if not already installed:**

-   **Terminal:**
-                  pip install pyinstaller

 **Build the executable with your custom icon:**

# On Windows:
-    **Terminal:**
-                    pyinstaller --onefile -w --icon=logo-image.ico file_organizer.py

# On Linux:
-    **Terminal:**
-                    pyinstaller --onefile --windowed --icon=logo-image.png file_organizer.py

# On macOS:
-    **Terminal:**
-                    pyinstaller --onefile --windowed --icon=logo-image.icns file_organizer.py

 **The executable will be available in the dist/ directory.**