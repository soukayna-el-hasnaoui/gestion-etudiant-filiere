from tkinter import *


class SButton(Button):

    def __init__(self, master, text, command=None):
        Button.__init__(self, master=master, text=text, command=command)
        self['font'] = ('Times', 15)
        self['relief'] = 'flat'
        self['bg'] = 'white'
        self.id = 0
        self.tk_info = ''



