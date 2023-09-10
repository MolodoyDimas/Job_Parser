from src.api_classes import HHapi, SuperJobApi
from abc import ABC, abstractmethod
import json


class VacancyFile(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **kwargs):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        pass


class VacanciesAll:
    '''Класс делает данные более удобными для работы'''

    def vac_hh(self):
        info_hh = []
        hh = HHapi().get_job()
        for x in hh:
            name = x['name']
            url = x['alternate_url']
            if x['salary'] == None:
                salary = 0
            else:
                salary = x['salary']['from']
            city = x['area']['name']
            info_hh.append({'name': name, 'city': city, 'salary': salary, 'url': url})
        with open('../Job_Parser/src/HH.json', 'w') as f:
            json.dump(info_hh, f)

    def vac_sj(self):
        info_sj = []
        sj = SuperJobApi().get_job()
        for x in sj:
            name = x['profession']
            url = x['link']
            if x['payment_from'] == None:
                salary = 0
            else:
                salary = x['payment_from']
            if x['address'] == None:
                city = None
            else:
                address = x['address'].split(', ')
                city = address[0]
            info_sj.append({'name': name, 'city': city, 'salary': salary, 'url': url})
        with open('../Job_Parser/src/SJ.json', 'w') as f:
            json.dump(info_sj, f)


class Vacanc():
    '''Работа с Вакасией'''

    def __init__(self, name: str, city: str, salary: int, url: str):
        self.name = name
        self.city = city
        self.salary = salary
        self.url = url

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary




class JsonFile(VacancyFile):

    def __init__(self, filename):
        self._filename = filename
        self._vacancies = []

        with open(filename, 'r') as f:
            self._vacancies = json.load(f)

    def add_vacancy(self, vacancy):
        self._vacancies.append(vacancy)
        self._write_to_file()

    def get_vacancies(self, **kwargs):
        return [vacancy for vacancy in self._vacancies if
                all(vacancy.get(key) == value for key, value in kwargs.items())]

    def remove_vacancy(self, vacancy):
        self._vacancies.remove(vacancy)
        self._write_to_file()

    def _write_to_file(self):
        with open(self._filename, 'w') as f:
            json.dump(self._vacancies, f)
