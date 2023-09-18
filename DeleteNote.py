import os

def delete_note(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        notes = file.readlines()
        for n, note in enumerate(notes, start=1):
            print(n, '-', note, end='')
    print('')
    delete_index = int(input("\nВведите номер строки для удаления: ")) - 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for note, line in enumerate(notes):
            if note not in [delete_index]:
                file.write(line)