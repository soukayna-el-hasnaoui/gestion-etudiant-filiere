from tkinter import Label, X, W


class SLabel(Label):

    def __init__(self,master, text):
        Label.__init__(self, master=master, text=text, anchor=W)
        self['font'] = ('Times', 15)
        self['relief'] = 'flat'
        self['bg'] = '#aec4c7'
        self['fg'] = 'white'