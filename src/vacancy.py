from colorama import *


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name, area, requirement, responsibility, salary, currency, experience, employer, url):
        self.name = name
        self.area = area
        self.requirement = self.check(requirement)
        self.responsibility = self.check(responsibility)
        self.salary = self.check_salary(salary)
        self.currency = currency
        self.experience = experience
        self.employer = employer
        self._url = url

    @staticmethod
    def check(value):
        """
        Проверка значений атрибутов класса на None
        :param value:
        :return:
        """
        if value is None:
            return f'Требования не указаны'
        else:
            return f'{value}'

    @staticmethod
    def check_salary(value):
        """
        Функция используется для проверки значений атрибута класса salary на None
        :param value:
        :return:
        """
        if isinstance(value, dict):
            if value['from'] is None:
                return int(value['to'])

            elif value['to'] is None:
                return int(value['from'])
            else:
                return (int(value['from']) + int(value['to'])) / 2
        else:
            return 0

    def __lt__(self, other):
        """
        Функция для сравнений вакансий по зарплате
        :param other:
        :return: bool
        """
        if self.salary < other:
            return True
        return False

    def __eq__(self, other):
        """
        Функция для сравнения вакансии по зарплате
        :param other:
        :return: bool
        """
        if self.salary == other:
            return True
        return False

    def __le__(self, other):
        """
        ��ункция для сравнений вакансий по зарплате
        :param other:
        :return: bool
        """
        if self.salary <= other:
            return True
        return False

    @classmethod
    def from_dict(cls, data: list):
        """
        Преобразование набора данных из JSON в список обьекта
        :param data:
        :return: обьекты класса
        """
        if isinstance(data, list):

            vacancies_list = []
            for value in data:
                if value['salary'] is None:
                    currency = ''
                else:
                    currency = value['salary']['currency']

                vacancies_list.append(cls(name=value['name'],
                                          area=value['area']['name'],
                                          requirement=value['snippet']['requirement'],
                                          responsibility=value['snippet']['responsibility'],
                                          salary=value['salary'],
                                          currency=currency,
                                          experience=value['experience']['name'],
                                          employer=value['employer']['name'],
                                          url=value['alternate_url']))

            if len(vacancies_list) == 0 or vacancies_list is None:
                return f"Список не может быть пустым"
            return vacancies_list
        else:
            return f"Неверный формат данных"

    def __str__(self):
        """
        Строковое отображение атрибутов класса для пользователя
        :return:
        """
        if self.salary == 0:
            self.salary = f"Зарплата не указана"
        return (f'Название вакансии: {Fore.CYAN}{self.name}{Fore.RESET}\n'
                f'Город: {Fore.CYAN}{self.area}{Fore.RESET}\n'
                f'Требования: {Fore.CYAN}{self.requirement}{Fore.RESET}\n'
                f'Обязанности: {Fore.CYAN}{self.responsibility}{Fore.RESET}\n'
                f'Зарплата: {Fore.CYAN}{self.salary} {self.currency}{Fore.RESET}\n'
                f'Опыт работы: {Fore.CYAN}{self.experience}{Fore.RESET}\n'
                f'Организация: {Fore.CYAN}{self.employer}{Fore.RESET}\n'
                f'Ссылка: {self._url}\n')

    def __repr__(self):
        """
        Отображение информации о класса для разработчика
        :return:
        """
        return (
            f'Имя класса: {self.__class__.__name__}. Атрибуты класса: ({self.name}, {self.area}, {self.requirement}, '
            f'{self.responsibility}, {self.salary}, {self.experience}, {self._url})\n')
