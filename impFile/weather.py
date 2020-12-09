from bs4 import BeautifulSoup
import requests
import datetime
import time



url = 'https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Langsa&AreaID=501406&Prov=1'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

nightLabel= []
for night in range(17,24):
    nightLabel.append(str(night))
timeNow = datetime.datetime.now()
timeNowRes = str(timeNow.strftime('%H'))


weatherInformation = soup.find('div', class_='kiri').p.text
temperatureInformation = soup.find('div', class_='kanan').h2.text
windInformation = soup.find('div', class_='kanan').p.next_element.next_element.next_element.next_element.next_element.next_element


def getIconData(weatherIconLookoup):
    if "Hujan Ringan" in weatherIconLookoup:
        iconData = 'assets/Hujan.png'

    if "Berawan" in weatherIconLookoup:
        iconData = 'assets/Berawan.png'

    if "Berawan Tebal" in weatherIconLookoup:
        if str(nightLabel) in timeNowRes:
            iconData ='assets/BerawanMalam.png'
        else:
            iconData ='assets/CerahBerawan.png'

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
