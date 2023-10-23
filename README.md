# Python Batch File Processing

## Overview

This Python project offers a graphical interface to automate common file operations, including batch-renaming files and converting image formats. Designed to simplify everyday tasks.
## Features

### Batch File Renaming

- Choose a directory to batch-rename all files within it.
- Adds a prefix (currently hardcoded as "sample_") to each file.

### Image Format Conversion

- Choose a directory to convert image formats.
- User can specify the original and target image formats.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pillow for image processing (`pip install Pillow`)

### How to Use

1. Run `processing.py`.
2. A graphical interface will appear.
3. Choose the operation you want to perform:
    - **Rename Files**: Click this button and choose a directory. All files in the directory will be renamed with a prefix.
    - **Convert Images**: Click this button and choose a directory. You'll also need to enter the original and target image formats. All images in the directory with the original format will be converted to the target format.

## Future Enhancements

- [ ] Add more file operations like sorting, moving, and compressing files.
- [ ] Make the prefix for batch renaming customizable through the GUI.
