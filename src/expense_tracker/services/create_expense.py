import expense_tracker.domain.expense as expense
import datetime


def create_expense() -> bool:
    """
    Service function to create a new expense record.

    :return: A boolean indicating success or failure.
    """
    amount = float(input("Enter expense amount: "))
    category = "Food"
    date = datetime.date.today()
    description = "Grocery shopping"

    result = expense.create_expense(amount, category, date, description)
    return result