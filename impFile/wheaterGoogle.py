from bs4 import BeautifulSoup
import requests
import datetime
import time


nightLabel= []
for night in range(17,24):
    nightLabel.append(str(night))
timeNow = datetime.datetime.now()
timeNowRes = str(timeNow.strftime('%H'))


web = requests.get('https://weather.com/id-ID/weather/today/l/be2f7870c2d1f8d852e68f947ef0293164afb704a7dfc18bc7f3d53aa76c575c')
soup = BeautifulSoup(web.text, "html.parser")
divCuaca = soup.find('div', class_='CurrentConditions--phraseValue--2xXSr').text
divTemperature = soup.find('span', class_='CurrentConditions--tempValue--3KcTQ').text

#print(divCuaca)
#print(divTemperature)

def getTime(timeInformation):
    if str(nightLabel) in timeNowRes:
        AiSay = "Goodnight !"
    else:
        AiSay = "Morning !"

    return AiSay



def getIconData(weatherIconLookoup):
    if "Hujan Ringan" in weatherIconLookoup:
        iconData = 'assets/Hujan.png'

    if "Berawan" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData = 'assets/BerawanMalam.png'
        else:
            iconData = 'assets/CerahBerawan.png'

    if "Berawan Tebal" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData ='assets/BerawanMalam.png'
        else:
            iconData ='assets/CerahBerawan.png'
    
    if "Sebagian Berawan" in weatherIconLookoup:
        iconData = 'assets/Berawan.png'

    if "Hujan" in weatherIconLookoup:
        iconData = 'assets/Hujan.png'

    if "Hujan Lebat" in weatherIconLookoup:
        iconData = 'assets/HujanLebat.png'

    if "Badai Petir" in weatherIconLookoup:
        iconData = 'assets/BadaiPetir.png'

    if "Hujan Petir" in weatherIconLookoup:
        iconData = 'assets/BadaiPetir.png'

    if "Cerah" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData = 'assets/CerahMalam.png'
        else:
            iconData = 'assets/Sun.png'

    if "Kabut" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData = 'assets/CerahBerawanMalam.png'
        else:
            iconData = 'assets/CerahBerawan.png'

    if "Cerah Berawan" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData = 'assets/CerahBerawanMalam.png'
        else:
            iconData = 'assets/CerahBerawan.png'
    return iconData



#print(celciusRes)
