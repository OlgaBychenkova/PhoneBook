# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник
# с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр,
# сохранение, импорт, поиск, удаление, изменение данных.
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных


import json

phonebook = {
    "Иван 1": {
        'phones': [1321231, 121212],
        'email': '123@mail.ru',
        'birthday': '11.10.2000'
    },
    "Иван 2": {
        'phones': [55555],
        'email': '',
        'birthday': ''
    }
}


def input_new_name():
    name = input("Введите имя абонента: ")
    while name in phonebook:
        name = input("Такой с таким именем уже существует. Введите другое имя: ")
    return name


def input_new_phone_numbers():
    phone_numbers = []
    phone_number = input("Введите номер телефона (нажмите enter, чтобы перейти к следующему полю): ")
    while phone_number != "":
        phone_numbers.append(phone_number)
        phone_number = input("Введите следующий номер телефона (нажмите Enter, чтобы перейти к следующему полю): ")
    return phone_numbers


def input_new_email():
    email = input("Введите электронный адрес: ")
    while "@" not in email:
        email = input("Введите корректный электронный адрес: ")
    return email


def input_new_birthday():
    birthday = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
    return birthday


# Добавление записи
def new():
    name = input_new_name()
    phone_numbers = input_new_phone_numbers()
    email = input_new_email()
    birthday = input_new_birthday()

    phonebook[name] = {
        'phones': phone_numbers,
        'email': email,
        'birthday': birthday
    }

    save()
    print("Запись успешно добавлена.")


# Обновление записи
def update():
    old_name = input("Введите имя абонента: ")
    if old_name not in phonebook:
        print("Такого абонента нет в справочнике")
        return

    name_input = input("Xoтите изменить имя абонента? Введите \'да\' чтобы изменить, или Enter чтобы пропустить: ")
    if name_input != "":
        name = input_new_name()
    else:
        name = old_name

    phone_number_input = input("Хотите изменить номер телефона? Введите \'да\' чтобы изменить, или Enter чтобы пропустить ")
    if phone_number_input != "":
        phone_numbers = input_new_phone_numbers()
    else:
        phone_numbers = phonebook[old_name]['phones']

    email_input = input("Хотите изменить электронный адрес? Введите \'да\' чтобы изменить, или Enter чтобы пропустить ")
    if email_input != "":
        email = input_new_email()
    else:
        email = phonebook[old_name]['email']

    birthday_input = input("Хотите изменить дату рождения? Введите \'да\' чтобы изменить, или Enter чтобы пропустить ")
    if birthday_input != "":
        birthday = input_new_birthday()
    else:
        birthday = phonebook[old_name]['birthday']

    del phonebook[old_name]

    phonebook[name] = {
        'phones': phone_numbers,
        'email': email,
        'birthday': birthday
    }
    save()
    print("Запись успешно обновлена.")


#  Экспорт
def save():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Ваш справочник телефонов успешно сохранен в файле phonebook.json")


#  Импорт
def load():
    try:
        with open("phonebook.json", "r", encoding="utf-8") as fh:
            global phonebook
            phonebook = json.load(fh)
        print("Справочник телефонов успешно загружен")
    except FileNotFoundError:
        print("Файл не найден")


def print_info():
    print("Телефонный справочник:")
    for name, data in phonebook.items():
        print(f"Имя: {name} - Телефон: {data['phones']} - Email: {data['email']} - День рождения: {data['birthday']}")


def delete():
    name = input("Введите имя абонента: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Такого абонента нет в справочнике")
    save()


def manual():
    print("""
    /all - вывести весь справочник
    /new - добавить новую запись
    /update - обновить запись
    /delete - удалить запись
    /save - сохранить справочник
    /load - загрузить справочник
    /stop - выход из программы
    """)


def run():
    while True:
        command = input("Введите команду. Для справки введите /help: ")
        if command == "/help":
            manual()
        elif command == "/stop":
            save()
            print("Бот остановил свою работу. Заходите ещё, будем рады!")
            break
        elif command == "/all":
            print_info()
        elif command == "/new":
            new()
        elif command == "/update":
            update()
        elif command == "/delete":
            delete()
        elif command == "/save":
            save()
        elif command == "/load":
            load()
        else:
            print("Неопознанная команда. Просьба изучить мануал через /help")


run()
