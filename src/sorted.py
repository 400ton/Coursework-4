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


def check_input_salary(words):
    """
    Функция проверки входных данных с зарплаты
    :param words:
    :return: В зависимости от длины списка:
     dict с ключами "from", "to", "currency",
     dict с ключами "from", "to",
     dict с ключом "from"
    """
    # Удаление дефиса
    for i in range(len(words)):
        if words[i] == '-':
            words[i] = ''

    # Удаление пустых элементов
    words = [word for word in words if word != '']

    # Проверка длины списка
    if len(words) == 0:
        return f"Зарплата не указана"

    elif len(words) == 3:

        # Добавление ключей 'from', 'to', 'currency'
        words.insert(0, 'from')
        words.insert(2, 'to')
        words.insert(4, 'currency')

        # Преобразование в словарь
        dict_values = dict(zip(words[::2], words[1::2]))
        return dict_values

    elif len(words) == 2:
        # Добавление ключей 'from', 'to'
        for word in words:
            if word in 'RUR' or word in 'USD' or word in 'EUR' or word in 'KZT':
                words.insert(0, 'from')
                words.insert(2, 'currency')
                dict_values = dict(zip(words[::2], words[1::2]))
                return dict_values

        words.insert(0, 'from')
        words.insert(2, 'to')

        dict_values = dict(zip(words[::2], words[1::2]))
        return dict_values

    elif len(words) == 1:
        # Добавление ключa 'from'
        words.insert(0, 'from')
        dict_values = dict(zip(words[0::2], words[1::2]))
        return dict_values
    else:
        raise ValueError('Ошибка ввода')


def get_vacancies_by_salary(filtered_vacancies, check_salary):
    """
    Функция для получения вакансий по зарплате
    :param filtered_vacancies: список вакансий
    :param check_salary: диапазон зарплаты
    :return:
    """
    from_check = 0
    to_check = 0
    currency_check = 'RUR'

    try:
        if isinstance(check_salary, dict):
            if check_salary.get('from') or check_salary.get('to') or check_salary.get('currency'):
                from_check = int(check_salary.get('from'))
                to_check = int(check_salary.get('to'))
                currency_check = check_salary.get('currency')

                if currency_check is None:
                    currency_check = 'RUR'

    except TypeError:
        return [f'{Fore.RED}Ошибка ввода диапазона{Fore.RESET}']

    try:
        # Поиск зарплаты в списке отфильтрованых вакансий
        ranged_vacancies = []
        if from_check is not None or to_check is not None:
            for vacancy in filtered_vacancies:
                if from_check <= vacancy.salary <= to_check:
                    print(from_check, vacancy.salary, to_check)
                    ranged_vacancies.append(vacancy)

        elif to_check is None:
            for vacancy in filtered_vacancies:
                if vacancy.salary == from_check:
                    ranged_vacancies.append(vacancy)

            # Проверка возвращаемого функцией списка
        if not ranged_vacancies:
            return [
                f'{Fore.RED}Вакансии не найдены. Попробуйте изменить диапазон или дописать (RUR, USD, EUR, KZT){Fore.RESET}']

        return ranged_vacancies

    except AttributeError:
        return [f'{Fore.RED}Вакансии не найдены{Fore.RESET}']


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
