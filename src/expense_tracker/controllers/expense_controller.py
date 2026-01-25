import datetime
import expense_tracker.domain.errors as errors


def input_amount():
    while True:
        try:
            amount_str = float(input("Enter amount: "))
            return amount_str
        except ValueError:
            print("Please enter a valid number.")


def input_description():
    while True:
        description = input("Enter description: ")
        if description != "":
            return description
        print("Please enter a valid description.")


def input_date():
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Please enter a valid date.")


def input_category():
    while True:
        category = input("Enter category (Food, Transport, Utilities, Entertainment, Other): ")
        if category != "":
            return category
        print("Please enter a valid category.")

def create_expense(service, repo) -> 'Expense':
    while True:
        try:
            amount = input_amount()
            category = input_category()
            date = input_date()
            description = input_description()
            return service.create_expense(amount, category, date, description, repo)
        except errors.INVALID_AMOUNT as e:
            print(e.message + ". Please try again.")
        except errors.INVALID_CATEGORY as e:
            print(e.message + ". Please try again.")
        except errors.INVALID_DATE as e:
            print(e.message + ". Please try again.")
        except errors.INVALID_DESCRIPTION as e:
            print(e.message + ". Please try again.")