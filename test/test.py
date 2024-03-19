import pytest
from colorama import *
from src.sorted import filter_vacancies, get_top_vacancies, get_vacancies_by_salary
from src.vacancy import Vacancy

vacancies_list = [
    {'name': 'Вакансия 1',
     'area': {'name': 'Москва'},
     'snippet': {'requirement': 'Высшее образование', 'responsibility': 'Работать'},
     'experience': {'name': '1 год'},
     'employer': {'name': 'ИП 1'},
     'salary': None,
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 2',
     'area': {'name': 'Санкт-Петербург'},
     'snippet': {'requirement': 'Опыт работы', 'responsibility': 'Работать'},
     'experience': {'name': '2 года'},
     'employer': {'name': 'ИП 2'},
     'salary': 200000,
     'alternate_url': 'hh.ru'},

    {'name': 'Вакансия 3',
     'area': {'name': 'Новосибирск'},
     'snippet': {'requirement': 'Базовое образование', 'responsibility': 'Работать'},
     'experience': {'name': '3 годa'},
     'employer': {'name': 'ИП 3'},
     'salary': {'from': 50000, 'to': None, 'currency': 'USD'},
     'alternate_url': 'hh.ru'}
]

filter_words = ['Москва', 'Опыт работы']

filtered_vacancy = Vacancy.from_dict(vacancies_list)


def test_filter_vacancies():
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    assert filtered_vacancies == vacancies_list[0:2]

    filtered_vacancies = filter_vacancies(vacancies_list, [])
    assert filtered_vacancies == f'{Fore.RED}Вакансии не найдены{Fore.RESET}'

    filtered_vacancies = filter_vacancies(vacancies_list, ['Несуществующее слово'])
    assert filtered_vacancies == f'{Fore.RED}Вакансии не найдены{Fore.RESET}'


def test_get_top_vacancies():
    pass


def test_get_vacancies_by_salary():
    salary_range = "Зарплата не указана"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == filtered_vacancy[0:1]

    salary_range = "50000 USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == []
