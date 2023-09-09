from abc import ABC, abstractmethod
import requests

class AbstractAPI(ABC):
    '''Абстрактный класс ля работы с API и вакансиями'''

    @abstractmethod
    def get_job(self):
        '''Метод получения вакансий'''
        pass

class HHapi(AbstractAPI):
    '''Класс для получения данных с сайта HH.ru и записи вакансий'''

    URL = 'https://api.hh.ru/vacancies'

    def get_job(self):
        params = {'text': 'python', 'per_page': 100}
        return requests.get(self.URL, params=params).json()['items']

class SuperJobApi(AbstractAPI):
    URL = 'https://api.superjob.ru/2.0/vacancies'
    HEADERS = {'X-Api-App-Id': 'v3.r.124528170.621d62a557b8856426457c2f77a545d774ab924b.2e6fff7100796e4d0bd72e84eb76c04532f4486b'}

    def get_job(self):
        params = {'keyword': f'python', 'count': 100}
        return requests.get(self.URL, headers=self.HEADERS, params=params).json()["objects"]

sja = SuperJobApi()
print(sja.get_job())