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
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        category TEXT,
        amount REAL NOT NULL,
        date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
""")
conn.commit()

# ----------------------------
# 4. CRUD Function Stubs
# ----------------------------

def add_expense(item, category, amount, date=None):
    """
    Add a new expense to the database.
    """
    if not item:
        raise ValueError("item is required")
    try:
        amount = float(amount)

        if date is None:
            cursor.execute(
                "INSERT INTO expenses (item, category, amount) VALUES (?, ?, ?)",
                (item, category, amount),
            )
        else:
            if isinstance(date, datetime):
                date_str = date.strftime("%Y-%m-%d %H:%M:%S")
            else:
                date_str = str(date)
            cursor.execute(
                "INSERT INTO expenses (item, category, amount, date) VALUES (?, ?, ?, ?)",
                (item, category, amount, date_str),
            )

        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        conn.rollback()
        raise

def view_expenses():
    """
    Query and display all expenses.
    """
    try:
        cursor.execute("SELECT id, item, category, amount, date FROM expenses")
        rows = cursor.fetchall()
        if not rows:
            print("No expenses found.")
            return rows
        
        print("\n" + "="*80)
        print(f"{'ID':<5} {'Item':<20} {'Category':<15} {'Amount':<12} {'Date':<20}")
        print("="*80)
        for row in rows:
            expense_id, item, category, amount, date = row
            print(f"{expense_id:<5} {item:<20} {category or 'N/A':<15} ${amount:<11.2f} {date:<20}")
        print("="*80 + "\n")
        return rows
    except sqlite3.Error as e:
        print(f"Error retrieving expenses: {e}")
        raise

def update_expense(expense_id, item=None, category=None, amount=None, date=None):
    """
    Update an existing expense.
    """
    try:
        # Build dynamic UPDATE query
        updates = []
        params = []

        if item is not None:
            updates.append("item = ?")
            params.append(item)
        if category is not None:
            updates.append("category = ?")
            params.append(category)
        if amount is not None:
            updates.append("amount = ?")
            params.append(float(amount))
        if date is not None:
            if isinstance(date, datetime):
                date_str = date.strftime("%Y-%m-%d %H:%M:%S")
            else:
                date_str = str(date)
            updates.append("date = ?")
            params.append(date_str)

        if not updates:
            raise ValueError("At least one field must be provided to update")

        params.append(expense_id)
        query = f"UPDATE expenses SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        conn.commit()

        if cursor.rowcount == 0:
            print(f"No expense found with ID {expense_id}")
        else:
            print(f"Expense {expense_id} updated successfully.")
        return cursor.rowcount
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error updating expense: {e}")
        raise

def delete_expense(expense_id):
    """
    Delete an expense.
    """
    try:
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"No expense found with ID {expense_id}")
        else:
            print(f"Expense {expense_id} deleted successfully.")
        return cursor.rowcount
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error deleting expense: {e}")
        raise

# ----------------------------
# 5. Challenge Function Stubs
# ----------------------------

def summary():
    """
    Calculate total and average expenses.
    """
    try:
        cursor.execute("SELECT SUM(amount), AVG(amount), COUNT(*) FROM expenses")
        result = cursor.fetchone()
        total, average, count = result

        print("\n" + "="*50)
        print("EXPENSE SUMMARY")
        print("="*50)
        print(f"Total Expenses: ${total or 0:.2f}")
        print(f"Average Expense: ${average or 0:.2f}")
        print(f"Number of Expenses: {count or 0}")
        print("="*50 + "\n")

        return {"total": total or 0, "average": average or 0, "count": count or 0}
    except sqlite3.Error as e:
        print(f"Error calculating summary: {e}")
        raise

def filter_by_month(year, month):
    """
    Show expenses for a specific month.
    """
    try:
        # Format: YYYY-MM
        start_date = f"{year:04d}-{month:02d}-01"

        # Calculate the end date of the month
        if month == 12:
            end_date = f"{year + 1:04d}-01-01"
        else:
            end_date = f"{year:04d}-{month + 1:02d}-01"

        cursor.execute(
            "SELECT id, item, category, amount, date FROM expenses WHERE date >= ? AND date < ? ORDER BY date",
            (start_date, end_date)
        )
        rows = cursor.fetchall()

        if not rows:
            print(f"\nNo expenses found for {year:04d}-{month:02d}.\n")
            return rows
        
        print(f"\n" + "="*80)
        print(f"EXPENSES FOR {year:04d}-{month:02d}")
        print("="*80)
        print(f"{'ID':<5} {'Item':<20} {'Category':<15} {'Amount':<12} {'Date':<20}")
        print("="*80)
        for row in rows:
            expense_id, item, category, amount, date = row
            print(f"{expense_id:<5} {item:<20} {category or 'N/A':<15} ${amount:<11.2f} {date:<20}")

        # Calculate total for the month
        total = sum(row[3] for row in rows)
        print("="*80)
        print(f"{'Total for month':<40} ${total:.2f}")
        print("="*80 + "\n")

        return rows
    except sqlite3.Error as e:
        print(f"Error filtering expenses by month: {e}")
        raise

# ----------------------------
# 6. Example Usage / Testing
# ----------------------------
if __name__ == "__main__":
    print("Expense Tracker Application")
    print("=" * 50)

    # Example: Add some expenses
    print("\n--- Adding Expenses ---")
    add_expense("Candy", "Snacks", 5.50)
    add_expense("Gas", "Transportation", 50.00)
    add_expense("Groceries", "Food", 100.50, datetime(2026, 2, 7))
    add_expense("Video Game", "Entertainment", 70.00)
    add_expense("Movie", "Disney Plus", 10.00)

    # View all expenses
    print("\n--- All Expenses ---")
    view_expenses()

    # Get summary
    print("--- Expense Summary ---")
    summary()

    # Filter by month
    print("--- February 2026 Expenses ---")
    filter_by_month(2026, 2)

    # Update an expense
    print("--- Update Expense (ID: 1) ---")
    update_expense(1, amount=6.00)

    # View updated expenses
    print("--- All Expenses After Update ---")
    view_expenses()

    # Delete an expense
    print("--- Delete Expense (ID: 4) ---")
    delete_expense(4)

    # Final View
    print("--- Final Expenses ---")
    view_expenses()

# ----------------------------
# 7. Close Database Connection
# ----------------------------
conn.close()