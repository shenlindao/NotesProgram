import json
from actions.show_all_notes import show
from drawings.input_enter import input_enter
from json.decoder import JSONDecodeError
file_path = './data/notes.json'

def delete_note(file_path):
    show(file_path)
    delete(file_path)

def delete(file_path):
     with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except JSONDecodeError:
            print('Невалидный JSON файл')
        try:
            delete_index = int(input("\nВведите id заметки для удаления: "))
            note = next((note for note in data if note['id'] == delete_index), None)
            if note is None:
                print('\nЗаметки с таким id не существует!\n')
                delete(file_path)
            else:
                for index, note in enumerate(data):
                    if note['id'] == int(delete_index):
                        data.pop(index)
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(json.dumps(data, ensure_ascii=False, indent=2))
                            print("\nЗаметка успешно удалена")
                            input_enter()
        except ValueError:
            print("\nВведно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки\n")
            delete(file_path)
