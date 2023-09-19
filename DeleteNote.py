import os
import json
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def delete_note(file_path):
    os.system('CLS')
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        print('УДАЛЕНИЕ ЗАМЕТОК\n')
        for note in data:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')
        delete_index = input("Введите id заметки для удаления: ")
        if delete_index.isdigit():
            for index, note in enumerate(data):
                if note['id'] == int(delete_index):
                    data.pop(index)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(json.dumps(data, ensure_ascii=False, indent=2))
                        print("\nЗаметка успешно удалена")
        else:
            print("\nВведно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки")
    input('\nНажмите Enter для возврата')
