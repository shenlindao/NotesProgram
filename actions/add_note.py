import os
import json
from drawings.input_enter import *
from datetime import datetime
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def add_note(file_path):
    os.system('CLS')
    with open(file_path, encoding='utf8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        print('ДОБАВЛЕНИЕ ЗАМЕТОК\n')
        head = ''
        head += input('Введите название заметки: ')
        body = ''
        body += input('\nВведите текст заметки: ')
        current_date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        if data:
            id = data[-1]['id']
            id += 1
        else:
            id = 1
        new_note = {
            'id': id,
            'head': head,
            'body': body,
            'date': current_date,
        }
        data.append(new_note)
        with open(file_path, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
    print('\nЗаметка успешно добавлена!')
    input_enter()
