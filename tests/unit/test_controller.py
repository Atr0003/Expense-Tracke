import expense_tracker.controllers.expense_controller as c
import expense_tracker.repositories.repository as r
import expense_tracker.services.create_expense as s
import datetime


def test_valid_create_expense(monkeypatch, capsys):

    inputs = iter([
        "100",              # amount
        "Food",             # category
        "2024-01-01",       # date
        "Groceries"         # description
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repo = r.Repository()
    expense = c.create_expense(s, repo)

    captured = capsys.readouterr()
    #assert "Error" not in captured.out
    assert expense.amount == 100
    assert expense.category == "Food"
    assert expense.date == datetime.date(2024, 1, 1)
    assert expense.description == "Groceries"
    assert len(repo.get_all()) == 1

def test_invalid_amount_then_valid(monkeypatch, capsys):

    inputs = iter([
        "invalid",          # invalid amount
        "200",              # valid amount
        "Transport",       # category
        "2024-02-01",      # date
        "Bus fare"         # description
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repo = r.Repository()
    expense = c.create_expense(s, repo)

    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert expense.amount == 200
    assert expense.category == "Transport"
    assert expense.date == datetime.date(2024, 2, 1)
    assert expense.description == "Bus fare"
    assert len(repo.get_all()) == 1

def test_invalid_date_then_valid(monkeypatch, capsys):

    inputs = iter([
        "150",              # amount
        "Utilities",       # category
        "invalid-date",    # invalid date
        "2024-03-01",      # valid date
        "Electricity bill" # description
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repo = r.Repository()
    expense = c.create_expense(s, repo)

    captured = capsys.readouterr()
    assert "Please enter a valid date." in captured.out
    assert expense.amount == 150
    assert expense.category == "Utilities"
    assert expense.date == datetime.date(2024, 3, 1)
    assert expense.description == "Electricity bill"
    assert len(repo.get_all()) == 1

def test_empty_description_then_valid(monkeypatch, capsys):

    inputs = iter([
        "75",               # amount
        "Entertainment",   # category
        "2024-04-01",      # date
        "",                 # empty description
        "Movie ticket"     # valid description
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repo = r.Repository()
    expense = c.create_expense(s, repo)

    captured = capsys.readouterr()
    assert "Please enter a valid description." in captured.out
    assert expense.amount == 75
    assert expense.category == "Entertainment"
    assert expense.date == datetime.date(2024, 4, 1)
    assert expense.description == "Movie ticket"
    assert len(repo.get_all()) == 1

def test_empty_category_then_valid(monkeypatch, capsys):

    inputs = iter([
        "50",               # amount
        "",                 # empty category
        "Other",           # valid category
        "2024-05-01",      # date
        "Miscellaneous"    # description
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repo = r.Repository()
    expense = c.create_expense(s, repo)

    captured = capsys.readouterr()
    assert "Please enter a valid category." in captured.out
    assert expense.amount == 50
    assert expense.category == "Other"
    assert expense.date == datetime.date(2024, 5, 1)
    assert expense.description == "Miscellaneous"
    assert len(repo.get_all()) == 1

