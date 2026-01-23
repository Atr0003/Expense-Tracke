import expense_tracker.services.create_expense as s
import expense_tracker.repositories.repository as r
import expense_tracker.domain.errors as errors

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
    try:
        s.create_expense(-50, "Food", datetime.date(2024, 1, 1), "Grocery shopping", repo)
    except errors.INVALID_AMOUNT as e:
        assert e.code == "INVALID_AMOUNT"
        assert e.message == "Le montant doit être strictement positif"
        assert e.field == "amount"

def test_create_expense_invalid_category():
    repo = r.Repository()
    try:
        s.create_expense(50, "InvalidCategory", datetime.date(2024, 1, 1), "Grocery shopping", repo)
    except errors.INVALID_CATEGORY as e:
        assert e.code == "INVALID_CATEGORY"
        assert e.message == "La catégorie fournie n'est pas valide"
        assert e.field == "category"

def test_create_expense_invalid_date():
    repo = r.Repository()
    try:
        s.create_expense(50, "Food", "2024-01-01", "Grocery shopping", repo)
    except errors.INVALID_DATE as e:
        assert e.code == "INVALID_DATE"
        assert e.message == "La date fournie n'est pas valide"
        assert e.field == "date"

def test_create_expense_invalid_description():
    repo = r.Repository()
    try:
        s.create_expense(50, "Food", datetime.date(2024, 1, 1), "", repo)
    except errors.INVALID_DESCRIPTION as e:
        assert e.code == "INVALID_DESCRIPTION"
        assert e.message == "La description fournie n'est pas valide"
        assert e.field == "description"

def test_create_expense_description_too_long():
    repo = r.Repository()
    long_description = "x" * 300  # 300 characters, exceeds 255 limit
    try:
        s.create_expense(50, "Food", datetime.date(2024, 1, 1), long_description, repo)
    except errors.INVALID_DESCRIPTION as e:
        assert e.code == "INVALID_DESCRIPTION"
        assert e.message == "La description fournie n'est pas valide"
        assert e.field == "description"

