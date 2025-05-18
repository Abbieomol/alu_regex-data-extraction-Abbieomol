import re

# Define regex patterns
regex_patterns = {
    "Email address (e.g., leila.kimani@greenmail.com)": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "URL (e.g., https://www.example.com)": r"^https?://[^\s]+$",
    "Phone number (e.g., (254) 711-234567 or 0711-234567)": r"^(\(?\d{3,4}\)?[-.\s]?\d{3}[-.\s]?\d{4})$",
    "Credit card (e.g., 1234-5678-9012-3456)": r"^(?:\d{4}[-\s]?){3}\d{4}$",
    "Time (e.g., 14:30 or 2:30 PM)": r"^(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?$",
    "HTML tag (e.g., <div>)": r"^<[^>]+>$",
    "Hashtag (e.g., #GreenInnovation)": r"^#\w+$",
    "Currency (e.g., $1,234.56)": r"^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$"
}

print("\n🔍 Regex Data Validation Checker\n")

# Loop through each pattern and validate user input
for description, pattern in regex_patterns.items():
    while True:
        user_input = input(f"Enter {description}: ")
        if re.fullmatch(pattern, user_input):
            print(f"✅ Found: {user_input}\n")
            break
        else:
            print("❌ Invalid. Please try again.\n")
