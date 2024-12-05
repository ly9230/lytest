"""
this is a practice py
"""
from name_function import get_formatted_name

def test_name_001():
    target = 'Liuyang'
    formatted_name = get_formatted_name('liu','yang')
    assert formatted_name == target
