import expense_tracker.domain.expense as e


def create_expense(amount, category, date, description, repo) -> e.Expense:
    """
    Service function to create a new expense record.

    :return: Expense object
    """
    result = e.create_expense(amount, category, date, description)
    repo.add(result)
    return result