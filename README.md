💰 Personal Finance Tracker

A simple yet powerful command-line based Personal Finance Tracker built with Python.
Easily record your daily transactions, categorize them, view detailed reports, and visualize your income vs. expenses with a clean graph.

✨ Features

✅ Add new transactions (Income/Expense) with date, amount, category, and description
✅ View all transactions neatly formatted from the CSV file
✅ Get summary reports between specific dates (total income, expenses, and savings)
✅ Generate income vs. expense graphs with Matplotlib
✅ Data stored locally in a CSV file for simplicity & portability
✅ Auto-initializes CSV file if missing


CLI Menu
Personal Finance Tracker
1. Add New Entry
2. View All Transactions
3. View Graph
4. View Transactions between a timeframe
5. Exit

Example Graph

The tracker plots your Income vs. Expenses over time:
(generated using Matplotlib)

🛠️ Installation

Clone the repository

git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker


Install dependencies

pip install -r requirements.txt


Run the program

python main.py

📂 Project Structure
personal-finance-tracker/
│── finance_data.csv       # Stores all transactions
│── data_entry.py          # Handles user input validation (date, amount, category, etc.)
│── main.py                # Main CLI entry point
│── requirements.txt       # Dependencies (pandas, matplotlib)
└── README.md              # Documentation

⚡ How It Works

Add Entry → Enter date, amount, category (Income/Expense), description

View All Transactions → Displays all data from finance_data.csv

View Graph → Plots income vs. expenses over time

Filter by Date Range → Get total income, expenses & savings within a timeframe

📊 Example Usage
Adding a transaction
Enter the date (dd-mm-yyyy) or Press Enter for today's date : 15-09-2025
Enter amount : 1200
Enter category (Income/Expense) : Income
Enter description : Freelance Project
Entry added

Viewing Transactions Between Dates
Enter the start date (dd-mm-yyyy) : 01-09-2025
Enter the end date (dd-mm-yyyy) : 15-09-2025

Transactions found for 01-09-2025 to 15-09-2025
      Date  Amount Category      Description
 01-09-2025    2000   Income    Salary
 03-09-2025     500  Expense   Groceries
 10-09-2025     700  Expense   Utilities
 15-09-2025    1200   Income   Freelance Project

Total Income : $3200
Total Expense : $1200
Total Savings : $2000

📦 Dependencies

pandas
 → Data handling

matplotlib
 → Graph plotting

Install them with:

pip install pandas matplotlib

🚀 Future Improvements

Add category-wise breakdown charts

Export reports to PDF/Excel

Add budget goals & alerts

GUI or Web-based version

👨‍💻 Author

Nafis Kamal
💼 Software Development | AI | Automation
📧 Contact: [your-email@example.com
]
🌐 GitHub: your-username

⭐ Contribute

Pull requests are welcome! If you have ideas for improvements, feel free to open an issue or submit a PR.
