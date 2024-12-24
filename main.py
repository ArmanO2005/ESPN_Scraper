import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
import re

headers = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/108.0.0.0 Safari/537.36")
}

def NFL_Offensive():
    url = "https://www.espn.com/nfl/stats/team"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("teamStats":\[.*?\]),"dictionary"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['displayName']
    for j in stats['teamStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['teamStats']):
        row = []
        row.append(i['team']['displayName'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def NFL_Defensive():
    url = "https://www.espn.com/nfl/stats/team/_/view/defense"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("teamStats":\[.*?\]),"dictionary"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['displayName']
    for j in stats['teamStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['teamStats']):
        row = []
        row.append(i['team']['displayName'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def NFL_SpecialTeams():
    url = "https://www.espn.com/nfl/stats/team/_/view/special"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("teamStats":\[.*?\]),"dictionary"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['displayName']
    for j in stats['teamStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['teamStats']):
        row = []
        row.append(i['team']['displayName'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def NFL_Turnovers():
    url = "https://www.espn.com/nfl/stats/team/_/view/turnovers"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("teamStats":\[.*?\]),"dictionary"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['displayName']
    for j in stats['teamStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['teamStats']):
        row = []
        row.append(i['team']['displayName'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def Player_Passing():
    url = "https://www.espn.com/nfl/stats/player"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("playerStats":\[.*?\]),"teams"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['name', 'position']
    for j in stats['playerStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['playerStats']):
        row = []
        row.append(i['athlete']['name'])
        row.append(i['athlete']['position'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def Player_Rushing():
    url = "https://www.espn.com/nfl/stats/player/_/stat/rushing"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("playerStats":\[.*?\]),"teams"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['name', 'position']
    for j in stats['playerStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['playerStats']):
        row = []
        row.append(i['athlete']['name'])
        row.append(i['athlete']['position'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


def Player_Receiving():
    url = "https://www.espn.com/nfl/stats/player/_/stat/receiving"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.code)

    soup = BeautifulSoup(response.text, "html.parser")

    stats = re.search(r'("playerStats":\[.*?\]),"teams"', soup.prettify())
    stats = json.loads('{' + stats[1] + '}')

    rowTitles = ['name', 'position']
    for j in stats['playerStats'][0]['stats']:
        rowTitles.append(j['name'])

    rows = []
    for num, i in enumerate(stats['playerStats']):
        row = []
        row.append(i['athlete']['name'])
        row.append(i['athlete']['position'])
        for j in i['stats']:
            row.append(j['value'])
        rows.append(row)

    return pd.DataFrame(rows, columns=rowTitles)


print(len(Player_Receiving()))
