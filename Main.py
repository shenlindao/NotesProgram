import sys
from actions.show_all_notes import *
from actions.show_note_for_date import *
from actions.add_note import *
from actions.edit_note import *
from actions.delete_note import *
from drawings.drawing_main import *
file_path = './data/notes.json'

def main(file_path):
    while True:
        os.system('CLS')
        drawing_main()
        user_choice = int(input('\nВведите номер нужной операции от 1 до 6: '))
        if user_choice == 1:
            show_notes(file_path)
        elif user_choice == 2:
            show_note_for_date(file_path)
        elif user_choice == 3:
            add_note(file_path)
        elif user_choice == 4:
            edit_note(file_path)
        elif user_choice == 5:
            delete_note(file_path)
        elif user_choice == 6:
            print('\nХорошего дня!\n')
            sys.exit()

main(file_path)