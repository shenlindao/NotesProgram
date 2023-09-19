import os
import json
from datetime import datetime
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def edit_note(file_path):
    os.system('CLS')
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        print('РЕДАКТИРОВАНИЕ ЗАМЕТОК\n')
        for note in data:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')
        edit_index = input("Введите id заметки для редактирования: ")
        if edit_index.isdigit():
            for note in data:
                if note['id'] == int(edit_index):
                    head = ''
                    head += input('\nВведите название заметки: ')
                    note['head'] = head
                    body = ''
                    body += input('\nВведите текст заметки: ')
                    note['body'] = body
                    current_date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
                    note['date'] = current_date
                    with open(file_path, 'w', encoding='utf8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                        print("\nЗаметка успешно обновлена")
                    break
                else:
                    print('\nЗаметки с таким id не существует')
        else:
            print("\nВведно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки")
    input('\nНажмите Enter для возврата')