# 🔍 Regex Data Extraction Project

This project demonstrates the use of **Regular Expressions (Regex)** in Python to extract structured data from unstructured text. It includes two components:

1. **`orgapp_data.py`** – Extracts multiple data types from a file (`orgapp.txt`).
2. **`orginput_validator.py`** – Allows users to input data manually and validates it using regex.

---

## 📁 Project Files

### 1. `extract_data.py`
- Reads text from `orgapp.txt`
- Extracts and prints:
  - Email addresses
  - URLs
  - Phone numbers
  - Credit card numbers
  - Hashtags
  - Currency amounts
  - Time (12-hour and 24-hour format)
  - HTML tags

### 2. `orgapp.txt`
Contains a sample block of text with multiple data types for extraction.

### 3. `interactive_validator.py`
- Prompts users to enter input for each field.
- Validates input with regex.
- Displays `✅ Found: <input>` if valid.
- Displays `❌ Invalid. Please try again.` if not.

---

## 🧪 How to Run

Make sure you have Python installed.

### To run the data extractor:
```bash
python extract_data.py
```

### To run the interactive validator:
```bash
python interactive_validator.py
```

---

## ✅ Data Types and Examples
| Data Type     | Example                                 |
|---------------|------------------------------------------|
| Email         | leila.kimani@greenmail.com              |
| URL           | https://www.example.com                 |
| Phone Number  | (254) 711-234567                        |
| Credit Card   | 1234-5678-9012-3456                     |
| Hashtag       | #GreenInnovation                        |
| Currency      | $1,234.56                               |
| Time          | 14:30 or 2:30 PM                        |
| HTML Tag      | <div class="container">               |

---

## 📌 Author
**Leila** – Junior Full Stack Developer and Python Enthusiast 💻🌍

---

## 🔗 GitHub Repository
Make sure your repo is named like this:  
**`alu_regex-data-extraction-{yourUsername}`**

