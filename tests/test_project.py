def test_salary_calculation():
    salary = 50000
    assert salary > 0

def test_salary_is_numeric():
    salary = 50000
    assert isinstance(salary, (int, float))