import requests
from bs4 import BeautifulSoup
import time


def scraper():
    url = 'https://sports.yahoo.com/nba/scoreboard/'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'html.parser')
    teamNames = data.findAll('span', attrs={
        "class": "YahooSans Fw(700)! Fz(14px)!"})
    teamScores = data.findAll('span', attrs={
        "class": "YahooSans Fw(700)! Va(m) Fz(24px)!"})
    quarters = data.findAll('div', attrs={
        "class": "Ta(end) Cl(b) Fw(b) YahooSans Fw(700)! Fz(11px)!"
    })

    teams = []
    scores = []

    for team in teamNames:
        if team not in teams:
            teams.append(team.text)

    for score in teamScores:
        scores.append(score.text)

    scoreboard = {}
    for team in range(len(teams)):
        if team >= len(scores):
            scoreboard[teams[team]] = 0
        else:
            scoreboard[teams[team]] = scores[team]

    scoreboards = []
    for count in range(0, len(scoreboard) - 1, 2):
        temp = []
        temp.append(f'{teams[count]}: {scoreboard[teams[count]]}')
        temp.append(f'{teams[count+1]}: {scoreboard[teams[count+1]]}')
        scoreboards.append(temp)
    # print(scoreboards)
    return scoreboards


def refresh():
    try:
        while True:
            scraper()
            time.sleep(10)
    except KeyboardInterrupt:
        print('Thanks for using this live score scraper!')


# scraper()
