import json
from actions.show_all_notes import show
from drawings.input_enter import input_enter
from datetime import datetime
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def edit_note(file_path):
    show(file_path)
    edit(file_path)

def edit(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        try:
            edit_index = int(input("\nВведите id заметки для редактирования: "))
            note = next((note for note in data if note['id'] == edit_index), None)
            if note is None:
                print('\nЗаметки с таким id не существует!\n')
                edit(file_path)
            else:
                head = input('\nВведите название заметки: ')
                note['head'] = head
                body = input('\nВведите текст заметки: ')
                note['body'] = body
                current_date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
                note['date'] = current_date
                with open(file_path, 'w', encoding='utf8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                    print("\nЗаметка успешно обновлена")
                    input_enter()
        except ValueError:
            print("\nВведно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки\n")
            edit(file_path)

