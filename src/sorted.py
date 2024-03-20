from colorama import *


def filter_vacancies(vacancies_list, filter_words):
    """
    Функция для фильтрации вакансий
    :param vacancies_list: список вакансий
    :param filter_words: ключ по которому идет фильтрация
    :return:
    """
    filtered_vacancies = []

    for vacancy in vacancies_list:
        for word in filter_words:
            if (word in vacancy.name or word in vacancy.area or word in vacancy.experience or word in vacancy.employer
                    or word in vacancy.requirement or word in vacancy.responsibility):
                filtered_vacancies.append(vacancy)

    if len(filtered_vacancies) != 0 or filtered_vacancies is None:
        return filtered_vacancies
    else:
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Функция для получения вакансий по зарплате
    :param filtered_vacancies: список вакансий
    :param salary_range: диапазон зарплаты
    :return:
    """
    if not salary_range:
        salary_range = "Зарплата не указана"

    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        if vacancy.salary == salary_range:
            ranged_vacancies.append(vacancy)

    if len(ranged_vacancies) == 0 or ranged_vacancies is None:
        return [f'{Fore.RED}Вакансии не найдены. Попробуйте изменить диапазон или дописать (RUR, USD, EUR, KZT){Fore.RESET}']
    return ranged_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Функция для получения топовых вакансий
    :param sorted_vacancies: список вакансий
    :param top_n: количество топовых вакансий
    :return:
    """
    if len(sorted_vacancies) < top_n:
        top_n = len(sorted_vacancies)

    top_vacancies = sorted_vacancies[:top_n]
    return top_vacancies

