import os.path


def display():
    print('''
          Welcome to your expense tracker
          Options
          1.view expenses
          2.add expenses and save to excel
          3.delete expenses
          4.view total cost
          5.exit
    ''')

expenses=[]

def add_expenses():
    description=input("description: ")
    try:
        cost=float(input("how much did it cost: "))
    except ValueError:
        print("invalid input")
    date=input("date of expense(DD/MM/YYYY): ")
    expenses.append({"description": description,
                     "cost": cost,
                     "date": date
                     }
                    )
    print("expense added successfully")
    save()
    add_others=input("would you like to add other tasks?(yes/no) ")
    if add_others.lower()=="yes":
        add_expenses()
    elif add_others.lower()=="no":
        main()
    else:
        print("invalid input")


def delete_expenses():
    if not expenses:
        print("nothing to delete as there are no expenses")
        return
    view_expenses()
    try:
        delete_expense=int(input("which expenses would you like to delete? "))
        if len(expenses)>=delete_expense>0:
            expenses.pop(delete_expense-1)
            save()
            print("expense deleted and saved successfully")
            delete_other=input("do you want to delete other expenses? ")
            if delete_other=="yes":
                delete_expenses()
            elif delete_other=="no":
                main()
            else:
                print("invalid input")
        else:
            print("invalid input")
            delete_expenses()
    except ValueError:
        print("invalid input")




def view_total_cost():
    if not expenses:
        print("0 KES")
        return
    cost_list=[]
    for index, expense in enumerate(expenses):
        cost=expense["cost"]
        cost_list.append(cost)
    total_cost=sum(cost_list)
    print(f"total cost: {total_cost}")


def view_expenses():
    if not expenses:
        print("no expenses have been added")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f" {index} description: {expense["description"]}  cost: {expense["cost"]}KES  date: {expense["date"]}")

import _json
import json
import pandas as pd
def save():
    column_data=["description", "cost", "date"]
    df=pd.DataFrame(columns=column_data)
    for index, expense in enumerate(expenses, start=1):
        individual_row_data = []
        for col in column_data:
            individual_row_data.append(expense.get(col, None))
        length = len(df)
        df.loc[length] = individual_row_data
    print(df)
    df.to_csv(r'C:\textbooks\python files\expenses.csv', index=False)
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
        print("expenses saved successfully")

def load():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses= json.load(file)
            print("expenses found and loaded successfully")
    except FileNotFoundError:
        print("trouble loading")




def main():
    while True:
        display()
        load()
        choice=input("what would you like to do: ")
        if choice=="1":
            view_expenses()
        elif choice=="2":
            add_expenses()
        elif choice=="3":
            delete_expenses()
        elif choice=="4":
            view_total_cost()
        elif choice=="5":
            print("thank you")
            break

if __name__=="__main__":
    main()
