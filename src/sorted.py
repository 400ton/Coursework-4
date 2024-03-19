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
            if word in str(vacancy):
                filtered_vacancies.append(vacancy)
                break
    if len(filtered_vacancies) != 0:
        return filtered_vacancies
    else:
        return f'Вакансии не найдены'


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """
    Функция для получения вакансий по зарплате
    :param filtered_vacancies: список вакансий
    :param salary_range: диапазон зарплаты
    :return:
    """
    ranged_vacancies = []
    if salary_range == "":
        salary_range = f"Зарплата не указана"
        for vacancy in filtered_vacancies:
            if salary_range <= vacancy.salary <= salary_range:
                ranged_vacancies.append(vacancy)

        return ranged_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """
    Функция для получения топовых вакансий
    :param sorted_vacancies: список вакансий
    :param top_n: количество топовых вакансий
    :return:
    """
    if top_n == "":
        top_n = 10
        top_vacancies = sorted_vacancies[:top_n]
        return top_vacancies
    elif top_n != int:
        return f'Введите число'
    else:
        if int(top_n) > len(sorted_vacancies):
            top_n = len(sorted_vacancies)
            top_vacancies = sorted_vacancies[:top_n]
            return top_vacancies
