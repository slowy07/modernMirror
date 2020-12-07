from tkinter import *
import locale
import threading
import json
import traceback
import feedparser

from PIL import Image, ImageTk
from contextlib import contextmanager

LOCALE_LOCK = threading.Lock()


ui_locale = ''
time_format = 24 #12 for set 12 hour time format
xlarge_text_size = 94
larget_text_size = 48
medium_text_size = 28
small_text_size = 18


@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)




class FullScreenWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background = 'black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        #----pack topFrame, bottomFrame------------------------------
        self.topFrame.pack(side = TOP, fill = BOTH, expand = YES)
        self.bottomFrame.pack(side = TOP, fill = BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>")
        self.tk.bind("<Escape>")
        #-------------------------------------------------------------

        #-------------------------clock-------------------------------
        #-------------------------------------------------------------

    def toggle_fullscreen(self, event = None):
        self.state = not self.state #toggling boolean   
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event = None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    w = FullScreenWindow()
    w.tk.mainloop()