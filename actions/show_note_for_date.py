import os
import json
from drawings.input_enter import *
from json.decoder import JSONDecodeError
file_path = './data/notes.json'


def show_one_note(file_path):
    os.system('CLS')
    target_note = input("Введите дату в формате (DD.MM.YYYY): ")
    flag = False
    if target_note.replace(".", "").isdigit():
        if (
            len(target_note) == 10
            and 0 < int(target_note[0:2]) < 32
            and target_note[2] == "."
            and 0 < int(target_note[3:5]) < 13
            and target_note[5] == "."
            and int(target_note[6::]) > 0
        ):
            with open(file_path, 'r', encoding='utf8') as file:
                try:
                    data = json.load(file)
                except JSONDecodeError:
                    print('Невалидный JSON файл')
                for note in data:
                    if note["date"][0:10] == target_note:
                        print('')
                        print('id: ' + str(note['id']))
                        print('head: ' + note['head'])
                        print('body: ' + note['body'])
                        print('date: ' + note['date'])
                        flag = True
                if flag == False:
                    print("\nЗаметок с такой датой нет")
        else:
            print("\nВведена некорректная дата")
    else:
        print("\nВведена некорректная дата")


def show_note_for_date(file_path):
    show_one_note(file_path)
    input_enter()
