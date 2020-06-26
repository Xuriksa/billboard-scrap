import requests
from bs4 import BeautifulSoup
from utils import writeJSON

def getWeek(folder, url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    container = soup.find_all(id = 'charts')
    
    date = container[0]['data-chart-date']
    code = container[0]['data-chart-title']

    rows = soup.find_all(class_ = 'chart-element__wrapper') 
    dict = {'date': date, 'code': code, 'chartRows': []}
    
    for row in rows:
         position = row.find(class_='chart-element__rank__number').string
         artist = row.find(class_='chart-element__information__artist').string
         song = row.find(class_='chart-element__information__song').string
         trend = row.find(class_='chart-element__trend').string

         meta = row.find_all(class_='chart-element__meta')
         
         lastWeek = meta[0].string
         peak = meta[1].string
         duration = meta[2].string

         dict['chartRows'].append({'tw': position, 'lw': lastWeek, 'song': song, "artist": artist, 'peak': peak, 'wc': duration, 'trend': trend})
   
    writeJSON(dict, folder + "/" + date + '.json')
