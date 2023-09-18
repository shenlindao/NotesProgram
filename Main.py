from ShowNotes import *
from AddNote import *
from EditNote import *
from DeleteNote import *
file_path = './data/notes.json'

def drawing():
    print('1 - Показать все заметки')
    print('2 - Добавить заметку')
    print('3 - Редактировать заметку')
    print('4 - Удалить заметку')
    print('5 - Выход')

def main(file_path):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Введите номер нужной операции от 1 до 6: '))
        if user_choice == 1:
            show_notes(file_path)
        elif user_choice == 2:
            add_note(file_path)
        elif user_choice == 3:
            edit_note(file_path)
        elif user_choice == 4:
            delete_note(file_path)
        elif user_choice == 5:
            print('Хорошего дня!')
            return

main(file_path)