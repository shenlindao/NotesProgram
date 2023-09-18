import os
import json
file_path = './data/notes.json'

def show_notes(file_name):
    os.system('CLS')
    with open(file_path, 'r', encoding='utf8') as file:
        data = json.load(file)
        print('ЗАМЕТКИ\n')
        for note in data:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')
        input('Нажмите Enter для продолжения')
