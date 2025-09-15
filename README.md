# 💰 Personal Finance Tracker

A simple **Personal Finance Tracker** built with Python that allows you to **record, view, and analyze your income and expenses** over time.  
This project demonstrates **file handling, data visualization, and basic data analysis** in Python using CSV files and Matplotlib.

---

## 🚀 Features
- ➕ **Add New Entry** – Record income or expense transactions with date, amount, category, and description  
- 📋 **View All Transactions** – Display all recorded transactions in a neat tabular format  
- 📊 **Graph Transactions** – Visualize income and expenses over time using a line graph  
- 🗓️ **View Transactions in a Timeframe** – Filter transactions between two dates  
- 💾 **Persistent Storage** – All transactions are stored in `finance_data.csv` and loaded automatically  

---

## 🛠️ Tech Stack
- **Language**: Python 3  
- **Libraries**: `pandas`, `matplotlib`  
- **Storage**: CSV (`finance_data.csv`)  

---

## 📂 Project Structure
📁 personal-finance-tracker
│── main.py # Main menu loop and program logic
│── data_entry.py # Functions to handle user input validation
│── finance_data.csv # Transaction storage (auto-created if missing)
│── README.md # Project documentation


---

## ▶️ Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/personal-finance-tracker.git
   cd personal-finance-tracker


## Install dependencies:

pip install pandas matplotlib


## Run the program:

python main.py


Follow the on-screen menu:

## Personal Finance Tracker
1. Add New Entry
2. View All Transactions
3. View Graph
4. View Transactions between a timeframe
5. Exit

Enter your choice : 1
Enter the date (dd-mm-yyyy) or Press Enter for today's date: 15-09-2025
Enter amount: 500
Select category (Income/Expense): Income
Enter description: Freelance project
✅ Entry added

Enter your choice : 2
All Transactions:
Date        Amount Category Description
15-09-2025  500    Income   Freelance project

## 🌟 Future Improvements

Add categories summary (monthly totals for each category)

Export transactions to Excel or PDF reports

Add automatic currency conversion or multi-currency support

Build a GUI version using Tkinter or PyQt

Integrate with a web dashboard for interactive visualization

## DEVELOPED BY : Nafis Kamal
                  
