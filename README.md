# alu_regex-data-extraction_Abbieomol

This project demonstrates how to extract structured data from unstructured text using Python and Regular Expressions (Regex). It was developed as part of a short-term web application development gig.

## 🔍 What the Project Does

The script reads text data from a file (`orgapp.txt`) and uses regular expressions to search and extract:

- ✅ Email addresses  
- ✅ URLs  
- ✅ Phone numbers  
- ✅ Credit card numbers for the sponsors
- ✅ Currency values  
- ✅ Hashtags  
- ✅ Time formats (12-hour and 24-hour)  
- ✅ HTML tags  

If a pattern is not found, the script prints `"Not found"` under that data type.

## 🛠 Technologies Used

- **Python 3**
- **Regex (`re` module)**

## 📂 Files in This Repository

- `extract_data.py`: The main Python script that performs the regex extraction.
- `orgapp.txt`: A sample text file containing strings to extract data from.
- `README.md`: This file — explains the project.

## ▶️ How to Run the Project

1. Make sure Python is installed.
2. Clone this repo:
   ```bash
   git clone https://github.com/Abbieomol/alu_regex-data-extraction-Abbieomol.git

