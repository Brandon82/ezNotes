import dearpygui.dearpygui as dpg
import os

class Note:
    def __init__(self, name, folderpath, note):
        self.name = name
        self.folderpath = folderpath
        self.note = note
        self.fullpath = f'{self.folderpath}\\{self.name}.txt'
        self.refresh()

    def refresh(self):
        if(os.path.exists(self.folderpath)):
            self.readlines()
        else:
            os.makedirs(self.folderpath)
            self.readlines()
    
    def empty_file(self):
        open(self.fullpath, 'w+').close()
        self.note = ''''''
    
    def save_file(self):
        with open(self.fullpath, 'w+') as n1:
            n1.writelines(self.note)
        n1.close()

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
    
    def get_folderpath(self):
        return self.folderpath

    def set_note(self, note):
        self.note = note

    def readlines(self):
        data = ''''''
        with open(self.fullpath, 'r+') as n1:
            for line in n1:
                data += line
        n1.close()
        self.note = data