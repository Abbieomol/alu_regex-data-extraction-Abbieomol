# orgapp_data.py

import re
import os

# Regular Expressions for different data types
regex_patterns = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://[^\s]+",
    "Phone Numbers": r"(\(?\d{3,4}\)?[-.\s]?\d{3}[-.\s]?\d{3,4})",
    "Credit Cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "Hashtags": r"#\w+",
    "Currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    "Time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "HTML Tags": r"<[^>]+>"
}

# Prompt the user to enter a filename
file_name = input("Enter the name of the file to extract data from (e.g., org.txt): ")

# Check if file exists
if not os.path.exists(file_name):
    print(f"❌ File '{file_name}' does not exist.")
    exit()

# Read content from the file
with open(file_name, "r", encoding="utf-8") as file:
    file_text = file.read()

# Extract and print matches
for data_type, pattern in regex_patterns.items():
    matches = re.findall(pattern, file_text)
    print(f"\n🔎 {data_type} found:")
    if matches:
        for match in matches:
            print(f"  ✅ {match}")
    else:
        print("  ❌ Not found")


