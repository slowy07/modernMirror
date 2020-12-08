from tkinter import *
import time
import locale
import threading
import json
import traceback
import feedparser
import random

from PIL import Image, ImageTk
from contextlib import contextmanager


import impFile.wiki as wiki
import impFile.weather as weatherData

LOCALE_LOCK = threading.Lock()


ui_locale = ''
dateFormat = "%b %d %Y"
time_format = 24 #12 for set 12 hour time format
xlarge_text_size = 94
larget_text_size = 48
medium_text_size = 28
small_text_size = 14

@contextmanager
def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

#----------------------------clock--------------------------------------------------------------------
class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg = 'black')
        
        self.time1 = ''
        self.timeLabel = Label(self, font = ('Helvetica', xlarge_text_size), fg = 'white', bg = 'black')
        #---------time label pack--------------
        self.timeLabel.pack(side = TOP, anchor = E)
        #--------------------------------------

        self.dayOfWeek1 = ''
        self.dayOfWeekLabel = Label(self, text = self.dayOfWeek1, font = ('Helvetica', small_text_size), fg = 'white', bg ='black')
        #--------day of week label--------------
        self.dayOfWeekLabel.pack(side = TOP, anchor = E)
        #---------------------------------------

        self.date1 = ''
        self.dateLabel = Label(self, text = self.date1, font = ('Helvetica', small_text_size), fg = 'white', bg = 'black')
        #-------date label-------------------
        self.dateLabel.pack(side = TOP, anchor = E)
        #------------------------------------
        
        self.tick()

    def tick(self):
        with setlocale(ui_locale):
            if time_format == 12:
                time2 = time.strftime('%H:%M %p') #12 hour time format
            else:
                time2 = time.strftime('%H:%M:%S') #24 hour time format
            
            
            dayOfWeek2 = time.strftime('%A')
            date2 = time.strftime(dateFormat)

            if time2 != self.time1:
                self.time1 = time2
                self.timeLabel.config(text = time2)
            
            if dayOfWeek2 != self.dayOfWeek1:
                self.dayOfWeek1 = dayOfWeek2
                self.dayOfWeekLabel.config(text = dayOfWeek2)

            if date2 != self.date1:
                self.date1 = date2
                self.dateLabel.config(text = date2)

            self.timeLabel.after(200, self.tick)
#----------------------------clock--------------------------------------------------------------------


#----------------------------wikipedia--------------------------------------------------------------------
class WikipediaKnowledge(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg = 'black')
        self.title = 'Knowledge today'
        self.titleLabel = Label(self, text = self.title, font = ('Helvetica', medium_text_size), fg = 'white', bg = 'black')
        self.titleLabel.pack(side = TOP, anchor = W)
        
        #self.contentData = wiki.Wikipedia(random.choice(wiki.keyword))
        #self.contentLabel = Label(self, text = self.contentData, font = ('Helvetica', small_text_size), fg = 'white', bg = 'black', justify = LEFT,wraplength=900)
        #self.contentLabel.pack(side = TOP, anchor = W)

        self.contentContainer = Frame(self, bg = 'black')
        self.contentContainer.pack(side = TOP)
        self.getWikiData()
        
    def getWikiData(self):
        try:
            result = wiki.Wikipedia(random.choice(wiki.keyword))
            contentWiki = contentWikipedia(self.contentContainer, result)
            contentWiki.pack(side= TOP, anchor = W)
        except Exception as err:
            traceback.print_exc()
            print(err)

class contentWikipedia(Frame):
    def __init__(self, parent, event_name = ""):
        Frame.__init__(self, parent, bg = 'black')
        self.eventName = event_name
        self.eventNameLabel = Label(self, text = self.eventName, font = ('Helvetica', small_text_size), fg = 'white', bg ='black', justify=LEFT, wraplength= 1000)
        self.eventNameLabel.pack(side = LEFT, anchor = N)

#----------------------------wikipedia--------------------------------------------------------------------

#---------------------------weather information-----------------------------------------------------------
class wheater(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.forecast = weatherData.weatherInformation
        self.temperature = weatherData.temperatureInformation
        
        self.forecastLabel = Label(self, text = self.forecast, font = ('Helvetica', medium_text_size), fg = 'white', bg='black')
        self.forecastLabel.pack(side = TOP, anchor=N)

        self.temperatureLabel = Label(self, text = self.temperature, font = ('helvetica', larget_text_size), fg = 'white', bg='black')
        self.temperatureLabel.pack(side= LEFT, anchor = N)

#---------------------------weather information-----------------------------------------------------------



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
        self.tk.bind("<Return>") #fullscreen
        self.tk.bind("<Escape>") #exit fullscreen
        #-------------------------------------------------------------

        
        
        #-------------------------clock Frame---------------------------
        self.clock = Clock(self.topFrame)
        self.clock.pack(side = RIGHT, anchor = N, padx = 100, pady = 60)
        #-------------------------------------------------------------
        
        #-----------------------wikipedia------------------------------------
        self.Wiki1 = WikipediaKnowledge(self.bottomFrame)
        self.Wiki1.pack(side = LEFT, anchor = S, padx = 60, pady = 60) 
        #-------------------------------------------------------------------

        #--------------------other stuff--------------------------------
        self.weather1 = wheater(self.topFrame)
        self.weather1.pack(side = LEFT, anchor = N, padx =100, pady=60)

        #---------------------------------------------------------------



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
    w.tk.title('modern mirror')
    w.tk.mainloop()