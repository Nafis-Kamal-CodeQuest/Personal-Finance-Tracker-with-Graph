from datetime import datetime


def get_date(prompt, allow_default = False):
    date_input = input(prompt)
    if allow_default and not date_input:
        return datetime.today().strftime("%d - %m - %Y")
    else:
        valid_date = datetime.strptime(date_input, "%d - %m - %Y")
        return valid_date

def get_amount():
    try:
         amount = float(input("Enter amount : "))
         if(amount<=0):
             raise ValueError("Invalid amount")

         return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
        category = int(input("1. Income \n2. Expense : "))

        if(category==1):
            return "Income"
        elif(category==2):
            return "Expense"

def get_description():
        description = input("Enter description : ")
        return description