import os

def edit_note(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file:
        notes = file.readlines()
        for n, note in enumerate(notes, start=1):
            print(n, '-', note, end='')
    edit_index = int(input("\nВведите номер строки для редактирования: ")) - 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for note, line in enumerate(notes):
            if note in [edit_index]:
                res = ''
                res += input('Введите фамилию: ') + ' '
                res += input('Введите имя: ') + ' '
                res += input('Введите телефон: ')
                file.write(res + '\n')
            else:
                file.write(line)
    input('\nНажмите Enter для возврата')