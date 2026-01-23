import expense_tracker.services.create_expense as s
import expense_tracker.repositories.repository as r
import expense_tracker.domain.errors as errors
import pytest

import datetime




def test_valid_create_expense():
    repo = r.Repository()
    expense = s.create_expense(100, "Food", datetime.date(2024, 1, 1), "Grocery shopping", repo)
    assert expense.amount == 100
    assert expense.category == "Food"
    assert expense.date == datetime.date(2024, 1, 1)
    assert expense.description == "Grocery shopping"
    assert len(repo.get_all()) == 1

def test_create_expense_invalid_amount():
    repo = r.Repository()

    with pytest.raises(errors.INVALID_AMOUNT) as exc_info:
        s.create_expense(
            -50,
            "Food",
            datetime.date(2024, 1, 1),
            "Grocery shopping",
            repo
        )

    assert exc_info.value.code == "INVALID_AMOUNT"
    assert exc_info.value.field == "amount"


def test_create_expense_invalid_category():
    repo = r.Repository()
    with pytest.raises(errors.INVALID_CATEGORY) as exec_info:
        s.create_expense(50, "", datetime.date(2024, 1, 1), "Grocery shopping", repo)
        assert exec_info.value.code == "INVALID_CATEGORY"
        assert exec_info.value.message == "La catégorie fournie n'est pas valide"
        assert exec_info.value.field == "category"

def test_create_expense_invalid_date():
    repo = r.Repository()
    with pytest.raises(errors.INVALID_DATE) as exec_info:
        s.create_expense(50, "Food", "2024-01-01", "Grocery shopping", repo)
        assert exec_info.value.code == "INVALID_DATE"
        assert exec_info.value.message == "La date fournie n'est pas valide"
        assert exec_info.value.field == "date"

def test_create_expense_invalid_description():
    repo = r.Repository()
    with pytest.raises(errors.INVALID_DESCRIPTION) as exec_info:
        s.create_expense(50, "Food", datetime.date(2024, 1, 1), 12345, repo)
        assert exec_info.value.code == "INVALID_DESCRIPTION"
        assert exec_info.value.message == "La description fournie n'est pas valide"
        assert exec_info.value.field == "description"

def test_create_expense_description_too_long():
    repo = r.Repository()
    long_description = "x" * 300  # 300 characters, exceeds 255 limit
    with pytest.raises(errors.INVALID_DESCRIPTION) as exec_info:
        s.create_expense(50, "Food", datetime.date(2024, 1, 1), long_description, repo)
        assert exec_info.value.code == "INVALID_DESCRIPTION"
        assert exec_info.value.message == "La description fournie n'est pas valide"
        assert exec_info.value.field == "description"

