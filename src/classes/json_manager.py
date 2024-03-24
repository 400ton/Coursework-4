import os
import json
from src.classes.template import AbstractFileManager


class JSONManager(AbstractFileManager):
    """
    Класс для работы с файлом
    """

    def __init__(self, filename):
        """
        Конструктор принимает путь к файлу
        :param filename:
        """
        self.filename = filename

    def add_vacancy(self, value):
        """
        Добавляет данные в файл
        :param value:
        :return:
        """
        with open(self.filename, 'a', encoding='UTF-8') as file:
            json.dump(value, file, indent=2, ensure_ascii=False)
            file.write('\n')

    def open_file(self):
        """
        Открывает файл для чтения
        :return: open file
        """
        with open(self.filename, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def delete_vacancy(self):
        """
        Полностью очищает файл
        :return:
        """
        open(self.filename, 'w').close()
        os.remove(self.filename)