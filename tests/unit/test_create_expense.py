import expense_tracker.domain.expense as expense
import datetime

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
    try:
        expense.create_expense(**data_test_invalid)
    except expense.errors.INVALID_AMOUNT as e:
        assert e.code == "INVALID_AMOUNT"
        assert e.message == "Le montant doit être strictement positif"
        assert e.field == "amount"

def test_invalid_category():
    data_test_invalid = data_test.copy()
    data_test_invalid["category"] = "InvalidCategory"
    try:
        expense.create_expense(**data_test_invalid)
    except expense.errors.INVALID_CATEGORY as e:
        assert e.code == "INVALID_CATEGORY"
        assert e.message == "La catégorie fournie n'est pas valide"
        assert e.field == "category"

def test_invalid_description_length():
    data_test_invalid = data_test.copy()
    data_test_invalid["description"] = "x" * 300  # Exceeds 255 characters
    try:
        expense.create_expense(**data_test_invalid)
    except expense.errors.INVALID_DESCRIPTION as e:
        assert e.code == "INVALID_DESCRIPTION"
        assert e.message == "La description fournie n'est pas valide"
        assert e.field == "description"

def test_invalid_description_empty():
    data_test_invalid = data_test.copy()
    data_test_invalid["description"] = ""  
    try:
        expense.create_expense(**data_test_invalid)
    except expense.errors.INVALID_DESCRIPTION as e:
        assert e.code == "INVALID_DESCRIPTION"
        assert e.message == "La description fournie n'est pas valide"
        assert e.field == "description"

def test_invalid_date():
    data_test_invalid = data_test.copy()
    data_test_invalid["date"] = "InvalidDate"
    try:
        expense.create_expense(**data_test_invalid)
    except expense.errors.INVALID_DATE as e:
        assert e.code == "INVALID_DATE"
        assert e.message == "La date fournie n'est pas valide"
        assert e.field == "date"
