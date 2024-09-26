# Duplicate Image Removal Script

This Python script automatically deletes duplicate or similar images in a specified folder. It uses image hashing to detect similarities and removes images that fall below a set similarity threshold.

## Requirements

- Python 3.x
- `Pillow` library (Python Imaging Library, fork of PIL)
- `imagehash` library

You can install the required libraries using pip:

```bash
pip install pillow imagehash
