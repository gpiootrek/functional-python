import requests
from bs4 import BeautifulSoup
import pandas as pd

def load_data(url, columns):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    rows = soup.find_all('table')[1].find('tbody').find_all('tr')[0:]
    data_list = []

    for row in rows:
        cells = list(row.find_all('td'))
        data_list.append([cells[0].contents[0], cells[1].contents[0],
                         cells[2].contents[0], cells[4].contents[0], cells[6].contents[0]])

    dane = pd.DataFrame(data=data_list, columns=columns)

    return dane