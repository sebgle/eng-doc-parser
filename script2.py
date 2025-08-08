"""
File: read_█.py
Author: Sebastian Le
Description: Generic script to extract structured information from text files
"""    

import re
import os
import sys
import csv

# Set of valid acronyms used in label tags
valid = {
    # Enter valid acronyms here
}


def extract_base_and_revision(filename: str):
    name_part = filename.rsplit('█', █)[█]
    match = re.match(█, name_part)
    if match:
        return match.group(█), match.group(█)
    else:
        return name_part, ''


def find_acronym_tag_pairs_█(txt_file_path: str):
    number_pattern = re.compile(█) 
    acronym_pattern = re.compile(█)
    inline_pattern = re.compile(█)

    tag_pairs = set()
    used_indices = set()

    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    for i in range(len(lines)):
        if i in used_indices:
            continue

        # Case 1: █
        if i < len(lines) - 1 and (█) not in used_indices:
            line1, line2 = lines[█], lines[█]

            if number_pattern.match(line1) and acronym_pattern.match(line2) and line2 in valid:
                tag_pairs.add(f"{line2} {line1}")
                used_indices.update({█, █})
                continue

            elif acronym_pattern.match(line1) and number_pattern.match(line2) and line1 in valid:
                tag_pairs.add(f"{line1} {line2}")
                used_indices.update({█, █})
                continue

        # Case 2: █
        line = lines[i]
        inline_match = inline_pattern.match(line)
        if inline_match:
            code_a, code_b = inline_match.groups()
            if code_a in valid:
                tag_pairs.add(f"{code_a} {code_b}")
                used_indices.add(i)
                
                if i > 0 and number_pattern.match(lines[█]):
                    tag_pairs.add(f"{code_a} {lines[█]}")
                    used_indices.add(i-1)
                
                if i + 1 < len(lines) and acronym_pattern.match(lines[█]) and lines[█] in valid:
                    tag_pairs.add(f"{lines[█]} {code_b}")
                    used_indices.add(█)
                
    return tag_pairs


def process_folder(folder_path):
    output_rows = [("█","█", "█","█")]
    
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            base_name, revision = extract_base_and_revision(filename)
            tags = find_acronym_tag_pairs_█(file_path)
            for idx, tag in enumerate(sorted(tags), 1):
                output_rows.append(( idx, base_name, revision, tag))
                
    with open("output_results.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_tag_folder.py <folder_path>")
        sys.exit(1)
    
    folder = os.path.normpath(sys.argv[1].strip('"'))

    if not os.path.isdir(folder):
        print("Not a valid folder path.")
        sys.exit(1)

    process_folder(folder)
    print("datas successfully extracted to 'output_results.csv'!")
    
    print(f"Done! Opening  now...")
    if os.name == 'nt':
        os.startfile('output_results.csv')
    elif os.name == 'posix':
        subprocess.call(('xdg-open', 'output_results.csv'))


    sys.exit(0)
