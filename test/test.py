from colorama import *
from src.filter_func import filter_vacancies, get_top_vacancies, get_vacancies_by_salary
from src.classes.vacancy import Vacancy

vacancies_list = [
    {'name': 'Вакансия 1',
     'area': {'name': 'Москва'},
     'snippet': {'requirement': 'Высшее образование', 'responsibility': 'Работать'},
     'experience': {'name': '1 год'},
     'employer': {'name': 'ИП 1'},
     'salary': None,
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 2',
     'area': {'name': 'Ижевск'},
     'snippet': {'requirement': 'Высшее образование', 'responsibility': 'Работать'},
     'experience': {'name': '2 года'},
     'employer': {'name': 'ИП 2'},
     'salary': {'from': 30000, 'to': None, 'currency': 'USD'},
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 3',
     'area': {'name': 'Новосибирск'},
     'snippet': {'requirement': 'Базовое образование', 'responsibility': 'Работать'},
     'experience': {'name': '3 годa'},
     'employer': {'name': 'ИП 3'},
     'salary': {'from': None, 'to': 40000, 'currency': 'USD'},
     'alternate_url': 'hh.ru'}
]

filter_words = ['Москва', 'Высшее образование']

filtered_vacancy = Vacancy.from_dict(vacancies_list)


def test_filter_vacancies():
    filtered_vacancies = filter_vacancies(filtered_vacancy, filter_words)
    assert filtered_vacancies == filtered_vacancy[0:2]

    filtered_vacancies = filter_vacancies(filtered_vacancy, [])
    assert filtered_vacancies == filtered_vacancies

    filtered_vacancies = filter_vacancies(filtered_vacancy, ['Несуществующее слово'])
    assert filtered_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']

    filtered_vacancies = filter_vacancies(10, filter_words)
    assert filtered_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']


def test_get_top_vacancies():
    filtered_vacancies = get_top_vacancies(filtered_vacancy, None)
    assert filtered_vacancies == filtered_vacancy[:3]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 2)
    assert filtered_vacancies == filtered_vacancy[:2]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 5)
    assert filtered_vacancies == filtered_vacancy[:3]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, "vacancy")
    assert filtered_vacancies == [f'{Fore.RED}Ошибка ввода топа N. Введите число{Fore.RESET}']


def test_get_vacancies_by_salary():
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, "")
    assert ranged_vacancies == filtered_vacancy[0:3]

    salary_range = "50000 USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == [f'{Fore.RED}Измените формат ввода диапазона зарплат{Fore.RESET}']

    salary_range = "40000,40000,USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == filtered_vacancy[2:3]

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, None)
    assert ranged_vacancies == filtered_vacancy[0:3]

    ranged_vacancies = get_vacancies_by_salary(10, salary_range)
    assert ranged_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']

    ranged_vacancies = get_vacancies_by_salary("FSBsdfg", None)
    assert ranged_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']
