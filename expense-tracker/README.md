# Expense Tracker Application

This Expense Tracker uses a SQLite database to manage spending records. Users can add, view, update, and delete expenses, with summaries and filtering by month. It demonstrates full CRUD, database queries, aggregate functions, and date filtering.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install python on your computer
2. Save the program file (for example main.py)
3. Run the program via terminal using:
```bash
python expense_tracker.py
```

Instructions for using the software:

1. The program will create a SQLite database file and expenses table if it does not already exist.
2. Expenses can be added via the __add_expense( )__ function.
3. Users can manage expenses, generate summaries, and filter records by month.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python
* SQLite (included with Python)
* datetime library (included with Python library)
* Visual Studio Code (or any Python IDE)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
* [DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Create a menu that users can interact with, without the need of editing code
* [ ] Add additional tables
* [ ] Export expense reports and other added tables into a file format for easier tracking