from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы API сервиса с вакансиями, является шаблоном для всех классов наследников
    """

    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class AbstractFileManager(ABC):
    """
    Абстрактный класс для работы с файлом, является шаблоном для всех классов наследников
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
