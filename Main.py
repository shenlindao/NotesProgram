import sys
from actions.show_notes import *
from actions.add_note import *
from actions.edit_note import *
from actions.delete_note import *
from drawings.drawing_main import *
file_path = './data/notes.json'

def main(file_path):
    while True:
        os.system('CLS')
        drawing_main()
        user_choice = int(input('\nВведите номер нужной операции от 1 до 5: '))
        if user_choice == 1:
            show_notes(file_path)
        elif user_choice == 2:
            add_note(file_path)
        elif user_choice == 3:
            edit_note(file_path)
        elif user_choice == 4:
            delete_note(file_path)
        elif user_choice == 5:
            print('\nХорошего дня!\n')
            sys.exit()

main(file_path)