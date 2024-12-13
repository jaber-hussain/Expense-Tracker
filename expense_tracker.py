import sys
import os
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QSpacerItem, QSizePolicy, QDialog, QDialogButtonBox, QTableWidget, QTableWidgetItem, QAbstractItemView, QDateEdit
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

# Set DPI scaling environment variables
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  # Enable per-screen scaling
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1.25"  # Adjust this according to your screen DPI (optional)
os.environ["QT_SCALE_FACTOR"] = "1"  # Global scale factor for the app

# Enable high-DPI scaling
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 800, 600)  # Set size of the window
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar for full-screen effect
        
        # Initialize expense list
        self.expenses = self.load_expenses()

        # Create the main layout and font
        layout = QVBoxLayout()
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

        # Layout for close, minimize, restore buttons
        button_layout = QHBoxLayout()
        
        # Close button
        self.close_button = QPushButton("X", self)
        self.close_button.setStyleSheet("background-color: red; color: white; border-radius: 5px;")
        self.close_button.setFixedSize(40, 40)
        self.close_button.clicked.connect(self.close)  # Close the application
        
        # Minimize button
        self.minimize_button = QPushButton("-", self)
        self.minimize_button.setStyleSheet("background-color: yellow; color: black; border-radius: 5px;")
        self.minimize_button.setFixedSize(40, 40)
        self.minimize_button.clicked.connect(self.showMinimized)  # Minimize the window
        
        # Restore button
        self.restore_button = QPushButton("□", self)
        self.restore_button.setStyleSheet("background-color: green; color: white; border-radius: 5px;")
        self.restore_button.setFixedSize(40, 40)
        self.restore_button.clicked.connect(self.toggle_maximize)  # Toggle maximize/restore
        
        # Add buttons to the layout
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Spacer to push buttons right
        button_layout.addWidget(self.minimize_button)
        button_layout.addWidget(self.restore_button)
        button_layout.addWidget(self.close_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        # Date input (QDateEdit to show calendar)
        self.date_label = QLabel("Date (YYYY-MM-DD):")
        self.date_input = QDateEdit(self)
        self.date_input.setDisplayFormat("yyyy-MM-dd")  # Set the date format
        self.date_input.setDate(QDate.currentDate())  # Set current date as default
        self.date_input.setCalendarPopup(True)  # Enable calendar popup

        # Amount input
        self.amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter your amount")
        
        # Category input (ComboBox)
        self.category_label = QLabel("Category:")
        self.category_input = QComboBox(self)
        self.category_input.addItems(["Food", "Transport", "Entertainment", "Others"])

        # Description input
        self.description_label = QLabel("Description:")
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Enter description here")
        
        # Add Expense Button
        self.add_expense_button = QPushButton("Add Expense", self)
        self.add_expense_button.setStyleSheet("""
            background-color: #1e02ab;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.add_expense_button.setFixedHeight(40)
        self.add_expense_button.clicked.connect(self.add_expense)  # Connect the add_expense function
        
        # Export to CSV and View Summary buttons
        self.export_button = QPushButton("Export to CSV", self)
        self.export_button.setStyleSheet("""
            background-color: #1e02ab;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.export_button.setFixedHeight(40)
        self.export_button.clicked.connect(self.export_to_csv)  # Connect the export_to_csv function
        
        self.view_summary_button = QPushButton("View Summary", self)
        self.view_summary_button.setStyleSheet("""
            background-color: #1e02ab;
            color: white;
            border-radius: 5px;
            padding: 10px;
        """)
        self.view_summary_button.setFixedHeight(40)
        self.view_summary_button.clicked.connect(self.view_summary)  # Connect the view_summary function

        # Create the table for displaying expenses
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Date", "Amount", "Category", "Description", "Actions"])
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)  # Allow editing cells

        # Add table to the layout
        layout.addWidget(self.table)

        # Add widgets to the layout
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.category_label)
        layout.addWidget(self.category_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.add_expense_button)
        layout.addWidget(self.export_button)
        layout.addWidget(self.view_summary_button)

        # Set the layout to the widget
        self.setLayout(layout)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()  # Restore window
        else:
            self.showMaximized()  # Maximize window

    def add_expense(self):
        date = self.date_input.text()
        amount = self.amount_input.text()
        category = self.category_input.currentText()
        description = self.description_input.text()

        # Store the expense in a list
        expense = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        self.expenses.append(expense)

        # Save the updated expenses to CSV
        self.save_expenses()

        # Add the expense to the table
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(date))
        self.table.setItem(row, 1, QTableWidgetItem(amount))
        self.table.setItem(row, 2, QTableWidgetItem(category))
        self.table.setItem(row, 3, QTableWidgetItem(description))
        
        # Add delete button in the table
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_expense(row))
        self.table.setCellWidget(row, 4, delete_button)

        # Clear input fields
        self.clear_fields()

    def delete_expense(self, row):
        # Remove the expense from the list
        del self.expenses[row]

        # Remove the row from the table
        self.table.removeRow(row)

        # Save the updated expenses to CSV
        self.save_expenses()

    def save_expenses(self):
        # Save expenses to a CSV file
        filename = "expenses.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Category", "Description"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_expenses(self):
        # Load expenses from a CSV file
        filename = "expenses.csv"
        expenses = []
        if os.path.exists(filename):
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(row)
        return expenses

    def export_to_csv(self):
        # Export expenses to CSV
        if not self.expenses:
            print("No expenses to export!")
            return

        filename = "expenses.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Category", "Description"])
            writer.writeheader()
            writer.writerows(self.expenses)
        print(f"Exported {len(self.expenses)} expenses to {filename}.")

    def view_summary(self):
        # Update the table to show all expenses
        self.table.setRowCount(0)  # Clear the table

        for expense in self.expenses:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(expense["Date"]))
            self.table.setItem(row, 1, QTableWidgetItem(expense["Amount"]))
            self.table.setItem(row, 2, QTableWidgetItem(expense["Category"]))
            self.table.setItem(row, 3, QTableWidgetItem(expense["Description"]))
            
            # Add delete button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, row=row: self.delete_expense(row))
            self.table.setCellWidget(row, 4, delete_button)

    def clear_fields(self):
        self.date_input.clear()
        self.amount_input.clear()
        self.description_input.clear()


# Create the application and window
app = QApplication(sys.argv)
window = ExpenseTracker()
window.show()

sys.exit(app.exec_())
