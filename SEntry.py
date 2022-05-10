from tkinter import *


class SEntry(Entry):

    def __init__(self, master=None):
        Entry.__init__(self, master=master)
        self['font'] = ('Times', 14, 'bold')
        self['width'] = 20
        self['relief'] = GROOVE
        self['bd'] = 1

