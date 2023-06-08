import pytest

from employee import Employee


@pytest.fixture
def global_var():
    default_salary = Employee('liu', 'yang', '5000')
    return default_salary


def test_employee_001(global_var):
    message = global_var.give_raise()
    assert  message == "liuyang's salary is 10000"


def test_employee_002(global_var):
    message = global_var.give_raise(10000)
    assert message == "liuyang's salary is 15000"

