import os
import json

def show_notes(file_name):
    os.system('CLS')
    with open(file_name, 'a', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for note in data:
            print('id: ' + note['id'])
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')
        input('\nНажмите Enter для продолжения')
