from tkinter import *
import time
import locale
import threading
import datetime
import traceback
import random

from PIL import Image, ImageTk
from contextlib import contextmanager


import impFile.wiki as wiki
import impFile.weather as weatherData
import impFile.wheaterGoogle as wheaterGoogleData

LOCALE_LOCK = threading.Lock()


ui_locale = ''
dateFormat = "%b %d %Y"
time_format = 24 #12 for set 12 hour time format
xlarge_text_size = 94
large_text_size = 48
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
        self.timeLabel = Label(self, font = ('Helvetica', large_text_size), fg = 'white', bg = 'black')
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

        self.contentData = wiki.Wikipedia(random.choice(wiki.keyword))
        self.contentLabel = Label(self, text = self.contentData, font = ('Helvetica', small_text_size), fg = 'white', bg = 'black', justify = LEFT,wraplength=1000)
        self.contentLabel.pack(side = TOP, anchor = W)

        self.getWikiData()

    def getWikiData(self):
        getNameEvent = wiki.Wikipedia(random.choice(wiki.keyword))
        if getNameEvent != self.contentData:
            self.eventName = getNameEvent
            self.contentLabel.config(text= getNameEvent)

        self.contentLabel.after(600000, self.getWikiData)

#----------------------------wikipedia--------------------------------------------------------------------



#---------------------------weather information-----------------------------------------------------------
class wheater(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.forecast = wheaterGoogleData.divCuaca
        self.temperature = wheaterGoogleData.divTemperature

        image = Image.open(f'{wheaterGoogleData.getIconData(self.forecast)}')
        image = image.resize((100,100), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)
        self.iconLabelWeatherInformation = Label(self,image= photo, relief =FLAT, bg='black', bd=0)
        self.iconLabelWeatherInformation.image = photo
        self.iconLabelWeatherInformation.pack(side =LEFT, anchor = N, padx = 20)


        self.forecastLabel = Label(self, text = self.forecast, font = ('Helvetica', medium_text_size), fg = 'white', bg='black')
        self.forecastLabel.pack(side =TOP, anchor = W)


        self.temperatureLabel = Label(self, text = self.temperature, font = ('helvetica', large_text_size), fg = 'white', bg='black')
        self.temperatureLabel.pack(side=LEFT, anchor = N)

        image1 = Image.open('assets/Wind.png')
        image1 = image1.resize((20,20), Image.ANTIALIAS)
        image1 = image1.convert('RGB')
        photo1 = ImageTk.PhotoImage(image1)
        self.iconLabelWind = Label(self,image= photo1, relief =FLAT, bg='black', bd=0)
        self.iconLabelWind.image1 = photo1
        self.iconLabelWind.pack(side = LEFT, anchor = N)

        self.windforecastLabel = Label(self, text=weatherData.windInformation, font = ('Helvetica', small_text_size), fg = 'white', bg='black')
        self.windforecastLabel.pack(side=LEFT, anchor = N)




        self.getInformationWeatherForcast()

    def getInformationWeatherForcast(self):
        informationForcast = wheaterGoogleData.divCuaca
        informationTemperature = wheaterGoogleData.divTemperature
        if informationForcast != self.forecast:
            self.forecast = informationForcast
            self.forecastLabel.config(text = informationForcast)
        if informationTemperature != self.temperature:
            self.temperature = informationTemperature
            self.temperatureLabel.config(text =informationTemperature)

        self.temperatureLabel.after(600000, self.getInformationWeatherForcast)


#---------------------------weather information-----------------------------------------------------------

#----------------------------say day----------------------------------------------------------------------
class sayTodayInformation(Frame):
    def __init__(self,parent, *args, **kwargs):
        Frame.__init__(self, parent, bg = 'black')
        timedelta = datetime.datetime.now()
        self.getDateInformation = str(timedelta.strftime('%H'))
        
        self.sayAiLabel = Label(self, text = self.getDateInformation, font = ('Helvetica', small_text_size), fg = 'white', bg='black')
        self.sayAiLabel.pack(side=TOP, anchor = S)
        
        self.getTimeInformation()



    def getTimeInformation(self):
        timeInformationResult = wheaterGoogleData.getTime(self.getDateInformation)
        self.getDateInformation = timeInformationResult
        self.sayAiLabel.config(text =timeInformationResult)

        self.sayAiLabel.after(600000, self.getTimeInformation)

#----------------------------say day----------------------------------------------------------------------



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
        self.tk.bind("<Return>", self.toggle_fullscreen) #fullscreen
        self.tk.bind("<Escape>", self.end_fullscreen) #exit fullscreen
        #-------------------------------------------------------------


        #-------------------------ai say--------------------------------
        self.ai = sayTodayInformation(self.bottomFrame)
        self.ai.pack(side=TOP, anchor = S)
        #---------------------------------------------------------------

        #-------------------------clock Frame---------------------------
        self.clock = Clock(self.topFrame)
        self.clock.pack(side = RIGHT, anchor = N, padx = 95, pady = 60)
        #-------------------------------------------------------------

        #-----------------------wikipedia------------------------------------
        self.Wiki1 = WikipediaKnowledge(self.bottomFrame)
        self.Wiki1.pack(side = LEFT, anchor = S, padx = 95, pady = 50)
        #-------------------------------------------------------------------

        #--------------------other stuff--------------------------------
        self.weather1 = wheater(self.topFrame)
        self.weather1.pack(side = LEFT, anchor = N, padx =95, pady=60)

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
