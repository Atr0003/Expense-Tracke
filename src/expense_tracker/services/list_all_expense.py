

def list_all_expense(repository):
    """
    Retrieve all expenses from the repository.

    Args:
        expense_repository: An instance of the expense repository.
    Returns:
        A list of all expense records.
    """
    return repository.get_all()