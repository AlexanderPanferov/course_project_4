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
