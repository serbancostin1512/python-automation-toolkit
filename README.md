
# Python Automation Toolkit

A Python file organizer that sorts files into folders based on their extensions.

## Features

- Organize files by type
- Preview planned file moves before confirmation
- Support images, documents, spreadsheets, videos, audio, archives, and code files
- Avoid overwriting files with duplicate names
- Cancel the operation before any files are moved
- Include automated unit tests

## Requirements

- Python 3
- No external packages required

## How to Run

```bash
python file_organizer.py
```

Enter the path of the folder you want to organize.

Review the preview and type `y` to confirm or `n` to cancel.

## Run Tests

```bash
python -m unittest -v
```

## Technologies

- Python
- pathlib
- shutil
- unittest

## What I Learned

- File and directory management
- Working with file extensions
- Functions and loops
- Handling duplicate filenames
- Automated testing
- Safe file operations

---

Created as part of my Python programming portfolio.
