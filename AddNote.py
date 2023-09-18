import os
import json
from datetime import datetime
file_path = './data/notes.json'

def add_note(file_path):
    os.system('CLS')
    head = ''
    head += input('Введите название заметки: ')
    body = ''
    body += input('Введите текст заметки: ')
    current_date = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    os.system('CLS')
    with open(file_path, encoding='utf8') as file:
        if os.stat(file_path).st_size != 0:
            data = json.load(file)
        else:
            data = []
        id = len(data)
        id += 1
        new_data = {
            'id': id,
            'head': head,
            'body': body,
            'date': current_date,
        }
        data.append(new_data)
        with open(file_path, 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
        input('Заметка успешно добавлена! Нажмите Enter для возврата')
