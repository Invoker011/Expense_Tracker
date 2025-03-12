A simple Python-based expense tracking application that organizes monthly expenses into an Excel spreadsheet. 
This tool helps users categorize and track expenses by automatically storing them in the correct monthly sheet based on the provided date.

Features
Automatic Monthly Sorting – Expenses are categorized into the correct month based on the given date.
Excel Storage – Data is stored in an Excel file (expenses.xlsx) with 12 sheets, one for each month.
Structured Data Entry – Each entry includes:
Date (DD/MM/YY)
Category (e.g., Food, Transport, Rent)
Amount

Prerequisites
Ensure you have Python 3 installed along with the required libraries:
"pip install pandas openpyxl"

Running the Program
Clone this repository:

git clone https://github.com/yourusername/expense-tracker.git
Navigate to the project folder:

cd expense-tracker
Run the script:

python expense_tracker.py
File Structure
expense-tracker/
│── expenses.xlsx   
│── expense_tracker.py    
│── README.md              

Usage:
Run the script and input expense details when prompted.
The script will automatically store the data in the appropriate month’s sheet in expenses.xlsx.
Open the Excel file to view and analyze your expenses.

Future Enhancements:
Expense visualization with charts.
GUI-based interface for better usability.
CSV export for more flexibility.

