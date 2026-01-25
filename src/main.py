import expense_tracker.repositories.repository as r
import expense_tracker.services.create_expense as s
import expense_tracker.services.list_all_expense as l
import expense_tracker.controllers.create_expense_controller as c_e
import expense_tracker.controllers.list_all_expense_controller as c_l

def create_expense(service, repo):
    expense = c_e.create_expense(service, repo)
    print("Expense created successfully:")
    print(f"Amount: {expense.amount}")
    print(f"Category: {expense.category}")
    print(f"Date: {expense.date}")
    print(f"Description: {expense.description}")


def list_all_expense(service, repo):
    expenses = c_l.list_all_expense(service, repo)
    print("All Expenses:")
    for expense in expenses:
        print(f"- {expense.amount} | {expense.category} | {expense.date} | {expense.description}")

if __name__ == "__main__":
    repo = r.Repository()
    expense = create_expense(s, repo)
    list_all = list_all_expense(l, repo)