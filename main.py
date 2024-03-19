from src.head_hunterAPI import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saving import JSONManager
from src.sorted import filter_vacancies, get_vacancies_by_salary, get_top_vacancies


# Функция для взаимодействия с пользователем
def user_interaction():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получаем данные от пользователя
    search_query = input("Введите поисковый запрос: ").lower()
    top_n = input("Введите количество вакансий для вывода в топ N, по умолчанию стоит 10: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").capitalize().split()
    salary_range = input("Введите диапазон зарплат, пример: 100000 - 150000 RUR (USD, EUR, KZT) "
                         "по умолчанию зарплата не указана: ")

    # Получение вакансий с hh.ru в формате JSON по запросу
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Сохранение информации о вакансиях в файл
    json_saving = JSONManager('data/data.json')  # Инициализация менеджера загрузки
    json_saving.add_vacancy(hh_vacancies)  # Сохранение информации в файл

    # Открытие файла (интерпретатор создаст его сам, если файла нет)
    data = json_saving.open_file()

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.from_dict(data)

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)  # Фильтация по ключам
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)  # Фильтрация по диапазону зарплат
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)  # Фильтрация по колличеству вакансий

    # Вывод вакансий в топ N
    for vacancy in top_vacancies:
        print(f"{vacancy}\n")

    # Удаляем файл
    json_saving.delete_vacancy()


if __name__ == "__main__":
    user_interaction()
