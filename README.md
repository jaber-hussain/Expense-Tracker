# Expense Tracker

The Expense Tracker is a PyQt5-based desktop application that helps users manage their personal expenses. With a user-friendly interface, users can add, view, and export their expenses, categorize them, and keep track of their spending habits.

## Features

- **Add Expenses**: Input expense details such as date, amount, category, and description.
- **Expense Table**: View all added expenses in a tabular format.
- **Delete Expenses**: Remove individual expenses with a delete button.
- **Export to CSV**: Save expenses to a CSV file for external use.
- **High-DPI Support**: Optimized for high-resolution displays.
- **Categorization**: Assign categories like Food, Transport, Entertainment, and Others.
- **Calendar Popup**: Select dates easily using a calendar popup.

## Installation

### Prerequisites
- Python 3.6 or higher
- PyQt5 library

### Steps
1. Clone the repository or download the project files.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required dependencies using pip:
   ```bash
   pip install PyQt5
   ```

3. Run the application:
   ```bash
   python expense_tracker.py
   ```

## Usage

1. Launch the application.
2. Use the input fields to add expense details (date, amount, category, description).
3. Click the **Add Expense** button to save the expense.
4. View all expenses in the table, which includes an option to delete individual records.
5. Export expenses to a CSV file by clicking **Export to CSV**.
6. Use the **View Summary** button to refresh the expense table.

## File Structure

```
.
├── expense_tracker.py  # Main application file
├── expenses.csv        # CSV file to store expense records (auto-generated)
└── README.md           # Documentation file
```

## Key Functions

### add_expense()
- Adds a new expense to the internal list and table.
- Saves the updated expense list to a CSV file.

### delete_expense(row)
- Deletes an expense from the table and CSV file.

### save_expenses()
- Saves the current list of expenses to a `expenses.csv` file.

### load_expenses()
- Loads existing expenses from `expenses.csv` if the file exists.

### export_to_csv()
- Exports all expenses to a CSV file.

### view_summary()
- Refreshes the table to display all expenses from the internal list.

## Screenshots
![image](https://github.com/user-attachments/assets/184693b1-669f-461a-adc7-d307cb7a81e7)


## Future Enhancements

- Add filtering and sorting options.
- Include graphical analysis of expenses.
- Integrate a database for better scalability.
- Add user authentication for multi-user support.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

Feel free to reach out for any queries or suggestions!
