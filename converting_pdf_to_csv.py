import os
import re
import pdfplumber
import csv

# Define folder with PDFs and output CSV file
INPUT_DIR = "kcet_pdfs"  # Folder where your 8 PDFs are stored
OUTPUT_CSV = "kcet_cutoff_data.csv"

# Map common round indicators to standard round names
file_metadata = {
    "mock": "Mock",
    "r1": "Round 1",
    "round1": "Round 1",
    "r2": "Round 2",
    "round2": "Round 2",
    "ext": "Extended"
}


def extract_year_and_round(filename):
    year_match = re.search(r'20\d{2}', filename)
    year = year_match.group(0) if year_match else "Unknown"

    lower_filename = filename.lower()
    for key in file_metadata:
        if key in lower_filename:
            return year, file_metadata[key]

    return year, "Unknown"

# Categories in order as per the cutoff table
categories = [
    "1G", "1K", "1R", "2AG", "2AK", "2AR",
    "2BG", "2BK", "2BR", "3AG", "3AK", "3AR",
    "3BG", "3BK", "3BR", "GM", "GMK", "GMR",
    "SCG", "SCK", "SCR", "STG", "STK", "STR"
]

# Write to CSV
with open(OUTPUT_CSV, "w", newline='', encoding='utf-8') as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(["Year", "Round", "College", "Branch", "Category", "CutoffRank"])

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            year, round_name = extract_year_and_round(filename)

            print(f"📄 Processing {filename} → Year: {year}, Round: {round_name}")

            with pdfplumber.open(pdf_path) as pdf:
                current_college = ""
                for page_num, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()
                    lines = text.split('\n') if text else []

                    for line in lines:
                        line = line.strip()

                        # Match college line
                        college_match = re.match(r'^\d+\s+E\d+\s+(.*)', line)
                        if college_match:
                            current_college = college_match.group(1).strip()
                            continue

                        # Match branch and cutoff line
                        branch_match = re.match(r'^([A-Z]{2,3})\s+([A-Za-z\s\.\-&()]+?)\s+([\d\-\s]+)$', line)
                        if branch_match:
                            branch_code = branch_match.group(1)
                            branch_name = branch_match.group(2).strip()
                            cutoffs_raw = branch_match.group(3).strip().split()

                            if len(cutoffs_raw) >= len(categories):
                                for cat, rank in zip(categories, cutoffs_raw):
                                    if rank != "--":
                                        writer.writerow([year, round_name, current_college, branch_name, cat, rank])
                            continue

                    else:
                        continue  # No match in line — silently skip

print("\n✅ Extraction complete! CSV saved to:", OUTPUT_CSV)
