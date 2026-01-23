import expense_tracker.repositories.repository as r
import datetime

data_test = {"amount" : 50, "date" : datetime.date(2024, 1, 1), "category" : "Food", "description" : "Lunch"}


def test_add_expense():
    repo = r.Repository()
    repo.add(data_test)
    assert len(repo.get_all()) == 1

def test_get_all_expenses():
    repo = r.Repository() 
    repo.add(data_test)
    repo.add(data_test)
    assert len(repo.get_all()) == 2

def test_empty_repository():
    repo = r.Repository()
    assert len(repo.get_all()) == 0
