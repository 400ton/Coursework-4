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

filter_words = ['Москва', 'Опыт работы']

filtered_vacancy = Vacancy.from_dict(vacancies_list)


def test_filter_vacancies():
    filtered_vacancies = filter_vacancies(filtered_vacancy, filter_words)
    assert filtered_vacancies == filtered_vacancy[0:2]

    filtered_vacancies = filter_vacancies(filtered_vacancy, [])
    assert filtered_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']

    filtered_vacancies = filter_vacancies(filtered_vacancy, ['Несуществующее слово'])
    assert filtered_vacancies == [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']


def test_get_top_vacancies():
    filtered_vacancies = get_top_vacancies(filtered_vacancy, 1)
    assert filtered_vacancies == filtered_vacancy[:1]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 2)
    assert filtered_vacancies == filtered_vacancy[:2]

    filtered_vacancies = get_top_vacancies(filtered_vacancy, 5)
    assert filtered_vacancies == filtered_vacancy[:3]


def test_get_vacancies_by_salary():
    salary_range = ""
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == filtered_vacancy[0:1]

    salary_range = "50000 USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == [(f'{Fore.RED}Вакансии не найдены. '
                                f'Попробуйте изменить диапазон или дописать (RUR, USD, EUR, KZT){Fore.RESET}')]

    salary_range = "40000 USD"
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, salary_range)
    assert ranged_vacancies == filtered_vacancy[2:3]

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancy, None)
    assert ranged_vacancies == filtered_vacancy[0:1]


