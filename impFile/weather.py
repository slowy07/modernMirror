from bs4 import BeautifulSoup
import requests

url = 'https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Langsa&AreaID=501406&Prov=1'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

weatherInformation = soup.find('div', class_='kiri').p.text
temperatureInformation = soup.find('div', class_='kanan').h2.text
windInformation = soup.find('div', class_='kanan').p.next_element.next_element.next_element.next_element.next_element.next_element
