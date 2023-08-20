import json
from src.classes import HH, SJ


class Connector:
    """
    Класс для доступа к файлу json
    """

    def __init__(self, vacancy):
        self.vacancy = vacancy

    def connectHH(self):
        """
        Проверка на существование файла от HH с данными и
        создание его при необходимости
        """
        try:
            with open(f'{self.vacancy}_hh.json', encoding='utf-8') as file:
                self.vacancies_hh = json.load(file)
        except FileNotFoundError:
            print("Файл не найден, создание нового файла")
            self.vacancies_hh = HH(self.vacancy).get_request()

    def select_HH(self):
        """
        Изменяет созданный файл для последующей его обработки
        """
        hh_info = []

        for vacancy in self.vacancies_hh:
            hh_info.append(vacancy)

        return hh_info

    def connectSJ(self):
        """
        Проверка на существование файла от SJ с данными и
        создание его при необходимости
        """
        try:
            with open(f'{self.vacancy}_sj.json', encoding='utf-8') as file:
                self.vacancies_sj = json.load(file)
        except FileNotFoundError:
            print("Файл не найден, создание нового файла")
            self.vacancies_sj = SJ(self.vacancy).get_request()

    def select_SJ(self):
        """
        Изменяет созданный файл для последующей его обработки
        """
        sj_info = []

        for vacancy in self.vacancies_sj:
            sj_info.append(vacancy)

        return sj_info
