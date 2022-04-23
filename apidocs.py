from Functions import *
from datetime import datetime
from Myerror import *

oportunities = Oportunities()

"""
searcing - поиск записок по заданным данным
Параметры
 непринимат на вход параметры
Результатом работы является - найденная записка(в случае нахождения схожести), 
"""
def searching():
    filter = input("Search for: ")
    notes = oportunities.search(filter)
    oportunities.show(notes)


"""
modification - изменяет уже существующую заметку
Параметры
 непринимат на вход параметры
Результатом работы является - изменения старой записки, с фиксацией даты изменения
"""
def modification():
    id = input("Enter a note id: ")
    if id.isdigit():
        id = int(id)
        try:
            if id in range(1, oportunities.last_id + 1):
                memo, tags = input("Enter a memo: "), input("Enter tag: ")
                oportunities.upgrade(id, tags, memo, datetime.now())
        except:
            print('Notes with this id do not exist')
    else:
        print('Please enter a number')

"""
addition - создает новую заметку
Параметры
 непринимат на вход параметры
Результатом работы является - создание новой, с фиксацией даты создания
"""
def addition():
    memo, tag = input("Enter a memo: "), input("Enter tag: ")
    oportunities.create(memo, tag, datetime.now())
    print("Your note has been added.")

"""
choise - выполняет функцию, в соответсвии с выбором пользователя
Параметры
 непринимат на вход параметры
Результатом работы является - выполнение вызванной функции

Исключения
-ValueTooSmallError - введено число меньше существующих
-ValueTooLargeError - введено число больше существующих
-WrongdataTypeError - введен другой тип данных
"""
def choice():
    while True:
        try:
            menu()
            number = input("\nEnter an option: ")
            print(SEPARATOR)
            if number.isdigit():
                number = int(number)
                if 5 < number - 1 :
                    raise ValueTooLargeError
                elif number - 1 < 1:
                    raise ValueTooSmallError
                else:
                    function = interface[number - 1][2]()
            else:
                raise WrongdataTypeError
        except ValueTooSmallError:
            print('There is no team with this number, please enter a higher number')
        except ValueTooLargeError:
            print('There is no team with this number, enter a lower number')
        except WrongdataTypeError:
            print('Please enter a number')
"""
sort - посик заметок в определенном интервале времени
Параметры
 непринимат на вход параметры
Результатом работы является - вывод всех заметок, созданных в заданный период
"""
def sort():
    year1, month1, day1 = int(input("Enter a year1:")), int(input("Enter a month1:")), int(input("Enter a day1:"))
    year2, month2, day2 = int(input("Enter a year2:")), int(input("Enter a month2:")), int(input("Enter a day2:"))
    border1 = datetime(year1, month1, day1)
    border2 = datetime(year2, month2, day2)
    notes = oportunities.sort(border1, border2)
    print(SEPARATOR)
    oportunities.show(notes)
"""
interface - меню выбора функции
"""
interface = [(1, "Show all notes", oportunities.show),
             (2, 'Search notes', searching),
             (3, 'Add note', addition),
             (4, 'Modify note', modification),
             (5, 'Sort', sort),
             (6, 'Quit', oportunities.quit_prog)]

"""
menu - вывод меню выбора функции
Параметры
 непринимат на вход параметры
Результатом работы является - выводит меню, в которым пользователь может выбрать
необходимую функцию
"""
def menu():
    print(SEPARATOR, '\n')
    for i in range(0, 6):
        print(interface[i][0], '. ', interface[i][1], sep='')


if __name__ == '__main__':
    choice()
