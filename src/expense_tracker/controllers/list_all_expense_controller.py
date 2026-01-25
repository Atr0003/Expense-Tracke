
def list_all_expense(service, repository):
    """
    Controller function to list all expenses.

    Args:
        service: The service module for listing expenses.
        repository: An instance of the expense repository.
    Returns:
        A list of all expense records.
    """
    return service.list_all_expense(repository)