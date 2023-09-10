from src import api_classes, vacans
import json
#from main import interaction

def output_sites():
    '''Предоставляет список вакансий из выбранных сайтов'''
    number = int(input('''Выберете сайт для поиска и введите его цифру:
1: HH.ru
2: SuperJob
3: Все
Ввод: '''))

    vacancies_list = []

    if number == 1:
        with open('../Job_Parser/src/HH.json', 'r') as f:
            vac = json.load(f)
        vacancies_list.append(vac)

    elif number == 2:
        with open('../Job_Parser/src/SJ.json', 'r') as f:
            vac = json.load(f)
        vacancies_list.append(vac)

    elif number == 3:
        with open('../Job_Parser/src/HH.json', 'r') as a:
            vachh = json.load(a)
            vacancies_list.append(vachh)
        with open('../Job_Parser/src/SJ.json', 'r') as b:
            vacsj = json.load(b)
            vacancies_list.append(vacsj)

    else:
        print('\nТакой цифры нет')
        return output_sites()
    new_vacancies_list = [elem for sublist in vacancies_list for elem in sublist]
    return new_vacancies_list

