# ----------------------------
# 1. Import Libraries
# ----------------------------
import sqlite3
from datetime import datetime

# ----------------------------
# 2. Connect to the Database
# ----------------------------
# Opens or creates the SQLite database file
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ----------------------------
# 3. Create the Table
# ----------------------------
# Define the table schema for expenses
# Columns: id (PK), item, category, amount, date
cursor.execute("""
# CREATE TABLE SQL COMMAND GOES HERE
""")
conn.commit()

# ----------------------------
# 4. CRUD Function Stubs
# ----------------------------

def add_expense(item, category, amount, date=None):
    """
    Add a new expense to the database.
    """
    pass  # TODO: implement INSERT logic

def view_expenses():
    """
    Query and display all expenses.
    """
    pass  # TODO: implement SELECT logic

def update_expense(expense_id, item=None, category=None, amount=None, date=None):
    """
    Update an existing expense.
    """
    pass  # TODO: implement UPDATE logic

def delete_expense(expense_id):
    """
    Delete an expense.
    """
    pass  # TODO: implement DELETE logic

# ----------------------------
# 5. Stretch Challenge Function Stubs
# ----------------------------

def summary():
    """
    Calculate total and average expenses.
    """
    pass  # TODO: implement SUM and AVG

def filter_by_month(year, month):
    """
    Show expenses for a specific month.
    """
    pass  # TODO: implement date filtering

# ----------------------------
# 6. Example Usage / Testing
# ----------------------------
if __name__ == "__main__":
    # TODO: Call functions to test your code
    pass

# ----------------------------
# 7. Close Database Connection
# ----------------------------
conn.close()