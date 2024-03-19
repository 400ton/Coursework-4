import requests
from src.template import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API запросами c сайта hh.ru
    """

    def __init__(self):
        """
        Конструктор по умолчанию имеет url адрес для работы с API запросом для вакансий с сайта hh.ru
        """
        self.__base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """
        Функция возвращает данные с сайта по введенному ключу
        :param search_query:
        :return: json object
        """
        if search_query == '' or search_query == int:
            raise ValueError("Ввод не может быть пустым или быть числом")
        else:
            params = {"per_page": 100, "text": search_query, "page": 10}
            response = requests.get(self.__base_url, params=params)

            if response.status_code != 200:
                raise ConnectionError("Не удалось получить доступ к сайту")
            else:
                return response.json()["items"]