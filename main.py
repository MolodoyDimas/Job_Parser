from src import api_classes, working_vacancies, functions
import src
import json
import re # правда сам нашёл


hh = api_classes.HHapi()
sj = api_classes.SuperJobApi()
vac_hh_sj = working_vacancies.VacanciesAll()

print("Загрузка Сайта HH.ru ...")
hh.get_job()
print("Загрузка Сайта SuperJob.ru ...")
sj.get_job()
print("Формирование списка вакансий HH.ru ...")
vac_hh_sj.vac_hh()
print("Формирование списка вакансий SuperJob.ru ...")
vac_hh_sj.vac_sj()

def search_filter(list):
    '''Функция выполняет поиск по вакансиям используя: Город, ЗП, Профессию или Выводит все'''
    while True:
        number = int(input('''\nВведите цифру нужного пункта поиска:
1: Город
2: Зарплата ОТ
3: Профессия
4: Все доступные
Ввод: '''))

        if number == 1:
            city = input('\nВведите Город: ').capitalize()
            filtered_jobs = [job for job in list if job["city"] == city]
            return filtered_jobs

        elif number == 2:
            filtered_vacancies = []
            salary_user = int(input('\nВведите желаемую зарплату: '))
            for vacancy in list:
                salary = vacancy.get('salary')

                if salary is not None and salary >= salary_user:
                    filtered_vacancies.append(vacancy)
            return filtered_vacancies

        elif number == 3:
            name = input('\nВведите Профессию: ').capitalize()
            result = []
            for job in list:
                if name.lower() in job['name'].lower():
                    result.append(job)
            return result

        elif number == 4:
            return list

        else:
            print('\nСделайте выбор от 1 до 4:')


def interaction():
    '''Функция взаимодействия с пользователем'''

    print('\nДобро пожаловать!\n')
    list_vacancy = functions.output_sites()
    filter_list = search_filter(list_vacancy)
    if len(filter_list) == 0:
        print('Ничего не найдено')
    for x in filter_list:
        print(f'Профессия: {x["name"]}, Зарплата ОТ: {x["salary"]} RUB в Городе: {x["city"]}. {x["url"]}')
    return

print(interaction())
