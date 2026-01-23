import datetime
from dataclasses import dataclass

import expense_tracker.domain.errors as errors


@dataclass(frozen=True)
class Expense:
    amount: float
    category: str
    date: datetime.date
    description: str


def create_expense(amount, category, date, description) -> Expense:
    """
    Create a new expense record.
    ...
    """
    if amount <= 0:
        raise errors.INVALID_AMOUNT()

    if category not in ["Food", "Transport", "Utilities", "Entertainment", "Other"]:
        raise errors.INVALID_CATEGORY()

    if not isinstance(date, datetime.date):
        raise errors.INVALID_DATE()

    if not isinstance(description, str) or len(description) > 255 or len(description) == 0:
        raise errors.INVALID_DESCRIPTION()

    return Expense(
        amount=amount,
        category=category,
        date=date,
        description=description,
    )
