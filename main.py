from src.connector import Connector
from src.sort_classes import Vacancy

if __name__ == '__main__':
    print()
    print('Привет, данная программа поможет подобрать тебе твою будущую работу')
    print('Выберите ресурс для поиска работы:')
    user_choise = input("""Наберите соответствующий номер:
    1 - HH
    2 - SJ
    0 - exit\n""")

    while user_choise not in ['0', '1', '2']:
        print('Некорректный ввод')
        print("Введите  1 - HH, 2 - SJ, 0 - exit")
        user_choise = input()

    if user_choise == "0":
        print("Завершение работы программы...")
        exit()

    user_speciality = input('Введите специальность:').lower()

    vacancies = None
    connect = Connector(user_speciality)
    if user_choise == "1":
        try:
            connect.connectHH()
        except IndexError:
            print("Cпециальность не найдена")
            quit()
        vacancies = connect.select_HH()

    elif user_choise == "2":
        try:
            connect.connectSJ()
        except IndexError:
            print("Cпециальность не найдена")
            quit()
        vacancies = connect.select_SJ()
    else:
        print("Спасибо, что воспользовались нашим приложением")
        quit()

    for vacancy in vacancies:
        vacancy_class = Vacancy(vacancy['employer'], vacancy['name'], vacancy['url'], vacancy['requirement'],
                                vacancy['salary_from'], vacancy['salary_to'])
        print(vacancy_class)
    print(f"Всего найдено вакансий {len(vacancies)}")
    user_sort = input("\nХотите отсортировать вакансии по зарплате(от большего к меньшему Y/N? ").lower()
    if user_sort == "y":
        for sort in Vacancy.sorting(vacancies):
            print(sort)
        try:
            user_top = int(input("""\nХотите вывести список топ вакансий? 
    (Введите количество): """))
            if user_top:
                for top in Vacancy.get_top(vacancies, user_top):
                    print(top)
        except ValueError:
            print("Спасибо, что воспользовались нашим приложением")
    else:
        print("Спасибо, что воспользовались нашим приложением")
