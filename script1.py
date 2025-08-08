"""
File: read_█.py
Author: Sebastian Le
Description: Generic script to extract structured information from text files
"""    

import argparse
import csv
import os
from pathlib import Path
import re
import sys
import subprocess
import time


def prompt_folder_path() -> Path:
    """
    Prompts user to enter a folder path and validates it
    return: (Path) corresponding to the folder to be processed
    """
    folder_input = input("Please enter folder here (copy as path): ").strip('"')
    folder = Path(folder_input)
    
    # Validate folder path
    if not folder.exists():
        print(f"Error: The path '{folder}' does not exist.", file=sys.stderr)
        sys.exit(1)
    if not folder.is_dir():
        print(f"Error: The path '{folder}' is not a directory.", file=sys.stderr)
        sys.exit(1)
    return folder

    
def get_tags(file: Path) -> set:
    """
    Reads a .txt file and extracts all tags
    return: (set) of tags
    """
    tags = set()
    with open(file, 'r') as file:
        for line in file:
            tags.add(line.strip())
    return tags
  
  
def process_█(file: Path, valid_data_tags: set, valid_feed_tags: set) -> list:
    """
    Validates and extracts all data tags, datas, data #s, data tags, and data details from an █ .txt file
    return: (list) with all rows of data extracted from given █ file
    """
    rows = []
    with open(file, 'r') as f:
        lines = [line.strip().lstrip('█') for line in f if line.strip()]
        
    for i in range(3, len(lines)):
        # Assign line descriptions and format
        line_a = lines[█]
        line_b = lines[█]
        line_c = lines[█]
        line_d = lines[█]
        feed_parts = line_b.split('█')
        data_parts = line_a.split('█')
        
        # Pull data and data tags from respective lines
        if len(data_parts) > █ and len(feed_parts) > █:
            tag_a = data_parts[█].upper()
            tag_b = feed_parts[█].upper()
            
            # Check if tags are in the tag list before proceeding
            if tag_a in valid_data_tags and tag_b in valid_feed_tags:
                
                # Pull data code_b from the feed line
                if len(feed_parts) > █:
                    feed_parts = line_b.rsplit('█', █)
                    if len(feed_parts) == █ and all(p.strip().is█() for p in feed_parts[█].split('█')):
                        line_b, id_number = feed_parts[█], feed_parts[█]
                else:
                    id_number = "N/A"
                
                # Check if data detail is valid
                if not line_d.startswith("█"):
                    line_d = "Read Error"
                
                # Edge Case: data tag and data detail on same line
                if line_c.startswith("█"):
                    parts_c = line_c.rsplit('█', █)
                    line_d, line_c = parts_c[█], parts_c[█]
                    
                # Append all extracted fields to the list
                rows.append((
                    file.name.strip('.txt'),
                    line_a,
                    line_b,
                    id_number,
                    line_c,
                    line_d
                ))
                
    return rows


def prompt_file_name() -> str:
    """
    Prompts the user to enter the name of their new spreadsheet
    return: (str) corresponding to the name of the destination file
    """
    raw_input = input("Enter a name for your new spreadsheet: ").strip()
    name = raw_input.replace(" ", "_")
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    if not name.lower().endswith('.csv'):
        name += '.csv'
    return name

   
def write_file(filepath: Path, output_rows: list) -> bool:
    """
    Attempts to write extracted data to a spreadsheet
    return: (bool) can the file be written to?
    """
    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(output_rows)
            return True
    except PermissionError:
        print(f"\nError!: Unable to write to '{filepath}' (file may be open in another program)")
        input("Please close the spreadsheet and press enter or CTRL + C to exit")
        return False

   
def main():
    # Get and validate folder path
    folder = prompt_folder_path()
    
    # Read valid data/feed tags
    list_a = get_tags("list_a.txt")
    list_b = get_tags("list_b.txt")
    
    # Format spreadsheet
    output_rows = [("Document", "data Tag", "Fed from", "CKT #", "data Tag", "data Detail")]
    
    # Process files
    start_time = time.time()
    for file in folder.iterdir():
        if '█' in str(file).lower():
            rows = process_█(file, list_a, list_b)
            if rows:
                output_rows.extend(rows)
    end_time = time.time()
        
    # Print status
    for i in range(3):
        print('.')
        time.sleep(0.1)
    print(f"Finished in {end_time - start_time} seconds!")
    
    # Output data to spreadsheet
    file_name = prompt_file_name()
    while not write_file(file_name, output_rows):
        continue
        
    # Open spreadsheet
    print(f"Done! Opening '{file_name}' now...")
    if os.name == 'nt':
        os.startfile(file_name)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', file_name))

    sys.exit(0)

    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTask canceled")