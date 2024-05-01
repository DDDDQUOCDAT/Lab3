import employee_info as info

def test_get_employees_by_age_range():
    result = []
    assert(result == info.get_employees_by_age_range( 40 , 50 ))

def test_calculate_average_salary():
    result = (50000 + 60000 + 56000 + 70000 + 65000 + 60000)/6
    assert( info.calculate_average_salary() == result)

def test_get_employees_by_dept():
    result = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(result==info.get_employees_by_dept('Marketing'))