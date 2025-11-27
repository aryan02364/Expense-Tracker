# Expense Tracker Project

expensesList = [] # list of expenses in form of dictionary
print("Welcome to Expense Tracker")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses ")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

# 1. Add Expense
    if(choice == 1):
        date = input("Enter a date(dd/mm/yyyy): ")
        category = input("Enter a category(Food, Travel, Makeup, Books): ")
        description = input("Please provide the information: ")
        amount = float(input("Enter an amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Done. Expense is added successfully")

# 2. View All Expenses
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("OOPS! You haven't puchased anything yet. Please do some shopping before viwing your all expense.")
        else:
            print("====Your All Expenses====")
            count = 1
            for eachExp in expensesList:
                print(f"Expense No. {count} --> {eachExp["date"]}, {eachExp["category"]}, {eachExp["description"]}, {eachExp["amount"]}")
                count += 1

# 3. View Total Expenses
    elif(choice == 3):
        total = 0
        for eachEXP in expensesList:
            total = total + eachEXP["amount"]
        
        print("Total Expenses: ", total)

# 4. Exit
    elif(choice == 4):
        print("Thank You! For the using our Personal Finance App - Expense Tracker")
        break

# Invalid Option
    else:
        print("Invalid Choice! Please try again(Enter between 1 to 4 to get your desired result)")