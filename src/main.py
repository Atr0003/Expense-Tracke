import expense_tracker.repositories.repository as r
import expense_tracker.services.create_expense as s
import expense_tracker.controllers.expense_controller as c

def create_expense(service, repo):
    expense = c.create_expense(service, repo)
    print("Expense created successfully:")
    print(f"Amount: {expense.amount}")
    print(f"Category: {expense.category}")
    print(f"Date: {expense.date}")
    print(f"Description: {expense.description}")


if __name__ == "__main__":
    repo = r.Repository()
    expense = create_expense(s, repo)