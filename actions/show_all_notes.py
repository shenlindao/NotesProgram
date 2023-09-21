import os
import json
from drawings.input_enter import *
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def show(file_path):
    os.system('CLS')
    with open(file_path, 'r', encoding='utf8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        print('ЗАМЕТКИ\n')
        for note in data:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')

def show_notes(file_path):
    show(file_path)
    input_enter()
