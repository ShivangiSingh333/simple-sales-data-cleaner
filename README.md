# simple-sales-data-cleaner
This is a small Python project where I read sales data from a CSV file, remove incomplete records, and calculate total and average sales. The goal of this project was to practice file handling and basic data processing using Python.

I worked on a small Python project where I used a CSV file containing daily sales records and created a script to clean and organize the data. The program reads the file, ignores incomplete entries, and calculates basic information like total and average sales. It then prints a short summary so that the data can be quickly understood without manually checking the Excel sheet.
Through this project I practiced file handling, basic data validation, and writing simple automation scripts in Python.

What I did in the project:-

1) Read sales data from CSV file
2) Removed rows with missing values
3) Calculated total and average sales
4) Generated a quick summary output
5) Used Python loops, conditions and file handling

 ## Technologies Used
- Python 3  
- CSV module (built-in Python library)

  simple-sales-data-cleaner/
│
├── sales_data_cleaner.py # Main Python script
├── sales_data.csv # Sample sales dataset
├── README.md # Project documentation


---

## How It Works
1. The script reads the CSV file using `csv.DictReader`
2. It extracts sales amounts from each row
3. Missing or invalid values are ignored
4. Total and average sales are calculated
5. Results are displayed in the terminal

---

## Sample Output
Total Sales = 2500.0
Average Sales = 833.33


---

## What I Learned
- Reading and processing CSV files in Python  
- Using lists and loops for data aggregation  
- Basic data validation  
- Writing clean and readable Python scripts  

---

## Future Improvements
- Add error handling for invalid data
- Support multiple columns (date, product, region)
- Use Pandas for advanced data analysis

---

## Author
**Shivangi Singh**  
Beginner Python Developer 🚀

