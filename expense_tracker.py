import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime

# Function to add expense data
def add_expense(event=None):  # Allow event parameter for key binding
    # Get values from the input fields
    expense_date = date_entry.get()
    expense_category = category_entry.get()
    expense_amount = amount_entry.get()

    # Validate date format
    try:
        date_obj = datetime.strptime(expense_date, "%d/%m/%y")
        month_name = date_obj.strftime("%B")  # Get the month name
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in dd/mm/yy format.")
        return

    # Create the Excel file if it doesn't exist
    file_name = "expenses.xlsx"
    if not os.path.exists(file_name):
        # Create a new Excel file with sheets for each month
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            for month in ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]:
                pd.DataFrame(columns=["Date", "Category", "Amount"]).to_excel(writer, sheet_name=month, index=False)

    # Create a DataFrame for the new expense
    new_expense = pd.DataFrame({
        "Date": [expense_date],
        "Category": [expense_category],
        "Amount": [expense_amount]
    })

    # Write to the corresponding month sheet
    with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        new_expense.to_excel(writer, sheet_name=month_name, index=False, header=False, startrow=writer.sheets[month_name].max_row)

    messagebox.showinfo("Success", "Expense added successfully!")

# Function to create the GUI
def create_gui():
    global date_entry, category_entry, amount_entry

    # Create the main window
    window = tk.Tk()
    window.title("Expense Tracker")

    # Create labels and entries for date, category, and amount
    tk.Label(window, text="Date (dd/mm/yy):").grid(row=0, column=0)
    date_entry = tk.Entry(window)
    date_entry.grid(row=0, column=1)

    tk.Label(window, text="Category:").grid(row=1, column=0)
    category_entry = tk.Entry(window)
    category_entry.grid(row=1, column=1)

    tk.Label(window, text="Amount:").grid(row=2, column=0)
    amount_entry = tk.Entry(window)
    amount_entry.grid(row=2, column=1)

    # Create an Add Expense button
    add_button = tk.Button(window, text="Add Expense", command=add_expense)
    add_button.grid(row=3, column=0, columnspan=2)

    # Bind the Enter key to the add_expense function
    window.bind('<Return>', add_expense)  # Pressing Enter will trigger add_expense

    # Start the GUI event loop
    window.mainloop()

# Run the application
create_gui()
