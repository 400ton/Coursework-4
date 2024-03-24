from colorama import *


def filter_vacancies(vacancies_list, filter_words):
    """
    Функция для фильтрации вакансий
    :param vacancies_list: список вакансий
    :param filter_words: ключ по которому идет фильтрация
    :return:
    """
    filtered_vacancies = []
    if isinstance(vacancies_list, list):
        if not filter_words:
            return vacancies_list

        for vacancy in vacancies_list:
            for word in filter_words:
                if (word in vacancy.name or word in vacancy.area or word in vacancy.experience
                        or word in vacancy.employer or word in vacancy.requirement or word in vacancy.responsibility):
                    filtered_vacancies.append(vacancy)

        if len(filtered_vacancies) != 0 or filtered_vacancies is not None:
            return filtered_vacancies
        else:
            return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']
    else:
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Функция для получения вакансий по зарплате
    :param filtered_vacancies: список вакансий
    :param salary_range: диапазон зарплаты
    :return:
    """
    try:
        if not salary_range:
            return filtered_vacancies
        else:
            from_salary, to_salary, currency = salary_range.split(' ')
            print(from_salary, to_salary, currency)

            ranged_vacancies = []
            for vacancy in filtered_vacancies:
                if int(from_salary) <= vacancy.salary <= int(to_salary):
                    ranged_vacancies.append(vacancy)
            return ranged_vacancies

    except ValueError:
        return [f'{Fore.RED}Измените формат ввода диапазона зарплат{Fore.RESET}']


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Функция для получения топовых вакансий
    :param sorted_vacancies: список вакансий
    :param top_n: количество топовых вакансий
    :return:
    """
    if not top_n:
        top_n = len(sorted_vacancies)
        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies

    try:
        top_n = int(top_n)
        if len(sorted_vacancies) < top_n:
            top_n = len(sorted_vacancies)

        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies

    except ValueError:
        return [f'{Fore.RED}Ошибка ввода топа N{Fore.RESET}']
