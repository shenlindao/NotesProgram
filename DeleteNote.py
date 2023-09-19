import os
import json
file_path = './data/notes.json'

def delete_note(file_path):
    os.system('CLS')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for note in data:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('body: ' + note['body'])
            print('date: ' + note['date'])
            print('')
        delete_index = int(input("\nВведите id заметки для удаления: "))
        for index, note in enumerate(data):
            if note['id'] == delete_index:
                data.pop(index)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False, indent=2))
