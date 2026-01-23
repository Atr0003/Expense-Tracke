import expense_tracker.domain.expense as expense
import expense_tracker.domain.errors as errors
import datetime
import pytest

data_test = {"amount" : 50, "date" : datetime.date(2024, 1, 1), "category" : "Food", "description" : "Lunch"}

def test_valid_expense():
    result = expense.create_expense(**data_test)
    assert result.amount == 50
    assert result.date == datetime.date(2024, 1, 1)
    assert result.category == "Food"
    assert result.description == "Lunch"

def test_invalid_amount():
    data_test_invalid = data_test.copy()
    data_test_invalid["amount"] = -10
    with pytest.raises(expense.errors.INVALID_AMOUNT) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_AMOUNT"
    assert e.value.message == "Le montant doit être strictement positif"
    assert e.value.field == "amount"

def test_invalid_category():
    data_test_invalid = data_test.copy()
    data_test_invalid["category"] = "InvalidCategory"
    with pytest.raises(expense.errors.INVALID_CATEGORY) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_CATEGORY"
    assert e.value.message == "La catégorie fournie n'est pas valide"
    assert e.value.field == "category"

def test_invalid_description_length():
    data_test_invalid = data_test.copy()
    data_test_invalid["description"] = "x" * 300  # Exceeds 255 characters
    with pytest.raises(expense.errors.INVALID_DESCRIPTION) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_DESCRIPTION"
    assert e.value.message == "La description fournie n'est pas valide"
    assert e.value.field == "description"

def test_invalid_description_empty():
    data_test_invalid = data_test.copy()
    data_test_invalid["description"] = ""  
    with pytest.raises(expense.errors.INVALID_DESCRIPTION) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_DESCRIPTION"
    assert e.value.message == "La description fournie n'est pas valide"
    assert e.value.field == "description"

def test_invalid_date():
    data_test_invalid = data_test.copy()
    data_test_invalid["date"] = "InvalidDate"
    with pytest.raises(expense.errors.INVALID_DATE) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_DATE"
    assert e.value.message == "La date fournie n'est pas valide"
    assert e.value.field == "date"

def test_invalid_date_type():
    data_test_invalid = data_test.copy()
    data_test_invalid["date"] = 20240101  # Not a date object
    with pytest.raises(expense.errors.INVALID_DATE) as e:
        expense.create_expense(**data_test_invalid)
    assert e.value.code == "INVALID_DATE"
    assert e.value.message == "La date fournie n'est pas valide"
    assert e.value.field == "date"