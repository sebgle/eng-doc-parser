# Text Data Extraction Scripts

This repository contains two Python scripts for extracting structured information from `.txt` files in a given folder and exporting the results to a CSV spreadsheet. They are designed to process text-based datasets with consistent formatting, automatically identify matching elements, and organize them into an easily analyzable format.

## Features
- Batch processing of all text files in a selected folder.
- Flexible tag/code matching using regular expressions.
- Customizable list-based validation for which data entries to include.
- Clean CSV output that can be opened in Excel, Google Sheets, or any spreadsheet tool.

## Scripts
- **`script1.py`** – Reads input files, validates entries against predefined lists, and outputs structured rows of matched data.
- **`script2.py`** – Extracts code–number pairings from text files using multiple matching patterns, then compiles results into a CSV.

## Requirements
- Python 3.8+
- No external dependencies (only built-in Python modules are used).

## Usage
1. Place your `.txt` files and the required list files in the same directory as the scripts.
2. Run the desired script:
   ```bash
   python script1.py
   ```
   or
   ```bash
   python script2.py <folder_path>
   ```
3. Follow the on-screen prompts to select the folder and specify the output file name.

## Folder structure (example)
```
.
├── script1.py
├── script2.py
├── list_a.txt
├── list_b.txt
└── README.md
```

## Redaction note
Variable names, certain file names, and a few comments have been slightly generalized/redacted to avoid exposing project-specific terminology. This is a cosmetic change only — it does not affect the scripts’ functionality for similarly structured datasets.

## License
MIT License — feel free to adapt and reuse for your own projects.
