import argparse
import json
from datetime import datetime
from pathlib import Path
from tabulate import tabulate
FILE = Path("./memory.json")
def list_expense():
    if not FILE.exists() or FILE.read_text().strip() == "":
        return []   
    return json.loads(FILE.read_text())
def save_expense(expense):
    FILE.write_text(json.dumps(expense))
    return
def add_expense(expense):
    expense_data = list_expense()
    id = len(expense_data)+1
    expense_data.append({"id":id,
                    "description":expense.description,
                  "amount":expense.amount,
                  "category":expense.category if expense.category else "Personal",
                  "datetime":str(datetime.now())
                  })
    save_expense(expense_data)
    print(f'{id} added')
    return
def update_expense(expense):
    expense_data = list_expense()
    for i in expense_data:
        if i['id'] == expense.id:
            if expense.description:
                i['description'] = expense.description
            if expense.amount:
                i['amount'] = expense.amount
            if expense.category:
                i['category'] = expense.category
            save_expense(expense_data)
            print('updated')
            return

    print("expense not found")
    return 
def delete_expense(id):
    expense_data = list_expense()
    for index, expense in enumerate(expense_data):
        if expense["id"] == id:
            expense_data.pop(index)
            save_expense(expense_data)
            print("Deleted successfully")
            return

    print("Expense not found")
        
def print_expenses(expenses):
    print(tabulate(expenses, headers="keys", tablefmt="grid"))
    return
def main():
    parser = argparse.ArgumentParser()

    
    parser.add_argument("action")
    
    parser.add_argument("--id",type=int)

    parser.add_argument("--description")

    parser.add_argument("--amount", type=int)

    parser.add_argument("--category")

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Access and use the arguments
    if args.action == 'add':
        add_expense(args)
    elif args.action == 'update':
        update_expense(args)
    elif args.action == 'list':
        print_expenses(list_expense())
    elif args.action == 'delete':
        delete_expense(args.id)
        
        
    return

if __name__ == "__main__":
    main()
