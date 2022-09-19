import dearpygui.dearpygui as dpg

def get_note(note):
    data = ''''''
    with open(f'{note}.txt', 'r+') as n1:
        for line in n1:
            data += line
    n1.close()
    return data

def save_note(note_file, cur_note):
    print(cur_note)
    with open(f'{note_file}.txt', 'w+') as n1:
        n1.writelines(cur_note)
    n1.close()

def empty_file(note_file):
    open(f'{note_file}.txt', 'w+').close()