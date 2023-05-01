
def sort_by_salary_min(data):
    """Функция сортировки по минимальной зарплате"""
    data = sorted(data, reverse=True)
    return data

def sort_by_salary_max(data):
    """Функция сортировки по максимальной зарплате"""
    data = sorted(data, key=lambda x: (x.salary_sort_max is not None, x.salary_sort_max), reverse=True)
    return data