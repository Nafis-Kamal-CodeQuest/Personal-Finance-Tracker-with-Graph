import pandas as pd
import csv
from datetime import datetime
from data_entry import *
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = [
        "Date",
        "Amount",
        "Category",
        "Description",
    ]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Ensure date is in correct format before saving
        try:
            date = datetime.strptime(date, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            date = datetime.today().strftime("%d-%m-%Y")

        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        with open(cls.CSV_FILE, 'a', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        try:
            df = pd.read_csv(cls.CSV_FILE)

            if df.empty:
                print("No entries found")
                return df

            # Convert Date column to datetime
            df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", dayfirst=True, errors="coerce")
            df = df.dropna(subset=["Date"])  # drop invalid dates

            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")

            mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
            filtered_df = df.loc[mask]

            if filtered_df.empty:
                print("No entries found in this range")
            else:
                print(f"Transactions found for {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')}")
                print(filtered_df.to_string(
                    index=False,
                    formatters={"Date": lambda x: x.strftime("%d-%m-%Y")}
                ))

                total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
                total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()

                print(f"Total Income : ${total_income}")
                print(f"Total Expense : ${total_expense}")
                print(f"Total Savings : ${total_income - total_expense}")

            return filtered_df

        except FileNotFoundError:
            print("CSV file not found. Please add a transaction first.")
            return pd.DataFrame(columns=cls.COLUMNS)

    @classmethod
    def show_all_transactions(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            if df.empty:
                print("No transactions found.")
                return df

            # Ensure Date column is datetime and formatted consistently
            df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", dayfirst=True, errors="coerce")
            df = df.dropna(subset=["Date"])
            df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")

            print("All Transactions:")
            print(df.to_string(index=False))
            return df
        except FileNotFoundError:
            print("CSV file not found. Please add a transaction first.")
            return pd.DataFrame(columns=cls.COLUMNS)


def add():
    CSV.initialize_csv()
    date = get_date("Enter the date (dd-mm-yyyy) or Press Enter for today's date : ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):
    if df.empty:
        print("No transactions to plot.")
        return

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y", dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Date"])  # drop invalid dates

    if df.empty:
        print("No valid dates to plot. Check your data.")
        return

    df = df.set_index("Date")

    # Separate Income and Expense
    income_df = (
        df[df["Category"] == "Income"]
        .resample("D")["Amount"]
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["Category"] == "Expense"]
        .resample("D")["Amount"]
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df, label="Income", color="g")
    plt.plot(expense_df.index, expense_df, label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add New Entry")
        print("2. View All Transactions")
        print("3. View Graph")
        print("4. View Transactions between a timeframe")
        print("5. Exit")
        choice = input("Enter your choice : ")

        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            CSV.show_all_transactions()
        elif choice == 3:
            df = CSV.show_all_transactions()
            plot_transactions(df)
        elif choice == 4:
            start = get_date("Enter the start date (dd-mm-yyyy) : ")
            end = get_date("Enter the end date (dd-mm-yyyy) : ")
            CSV.get_transactions(start, end)
        elif choice == 5:
            print("Thank you for using Personal Finance Tracker")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
