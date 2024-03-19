from colorama import *


class Vacancy:
    def __init__(self, name, area, requirement, responsibility, salary, experience, employer, url):
        self.name = name
        self.area = area
        self.requirement = self.check(requirement)
        self.responsibility = self.check(responsibility)
        self.salary = self.check_salary(salary)
        self.experience = experience
        self.employer = employer
        self._url = url

    @staticmethod
    def check(value):
        if value is None:
            return f'Требования не указаны'
        else:
            return f'{value}'

    @staticmethod
    def check_salary(value):
        if isinstance(value, dict):
            if value['from'] is None:
                return f'{value['to']} {value['currency']}'

            elif value['to'] is None:
                return f'{value['from']} {value['currency']}'
            else:
                return f'{value['from']} - {value['to']} {value['currency']}'

        else:
            return f"Зарплата не указана"



    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        return False

    def __eq__(self, other):
        if self.salary == other.salary:
            return True
        return False

    @classmethod
    def from_dict(cls, data: list):
        vacancies = []
        for value in data:
            name = value['name']
            area = value['area']['name']
            requirement = value['snippet']['requirement']
            responsibility = value['snippet']['responsibility']
            salary = value['salary']
            experience = value['experience']['name']
            employer = value['employer']['name']
            url = value['alternate_url']
            vacancies.append(
                cls(name=name, area=area, requirement=requirement, responsibility=responsibility, salary=salary,
                    experience=experience, employer=employer, url=url))
        return vacancies

    def __str__(self):
        """
        Строковое отображение атрибутов класса для пользователя
        :return:
        """
        return (f'Название вакансии: {Fore.CYAN}{self.name}{Fore.RESET}\n'
                f'Город: {Fore.CYAN}{self.area}{Fore.RESET}\n'
                f'Требования: {Fore.CYAN}{self.requirement}{Fore.RESET}\n'
                f'Обязанности: {Fore.CYAN}{self.responsibility}{Fore.RESET}\n'
                f'Зарплата: {Fore.CYAN}{self.salary}{Fore.RESET}\n'
                f'Опыт работы: {Fore.CYAN}{self.experience}{Fore.RESET}\n'
                f'Организация: {Fore.CYAN}{self.employer}{Fore.RESET}\n'
                f'Ссылка: {self._url}\n')

    def __repr__(self):
        """
        Отображение информации о класса для разработчика
        :return:
        """
        return (
            f'Имя класса: {self.__class__.__name__}. Атрибуты класса: ({self.name}, {self.area}, {self.requirement},'
            f'{self.responsibility}, {self.salary}, {self.experience}, {self._url})')
