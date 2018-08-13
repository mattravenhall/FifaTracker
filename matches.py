# World Cup API
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

# Read in teams (Will need just Player, Team, and Remaining Status)
teams = pd.read_csv('./static/data/PlayerTeams.csv')

## Pull match data from fifa website
fixtures_url = 'https://www.fifa.com/worldcup/matches/'
previous = BeautifulSoup(requests.get(fixtures_url).content).find_all('div', class_='fi-mu result')
fixtures = BeautifulSoup(requests.get(fixtures_url).content).find_all('div', class_='fi-mu fixture')

dates, teamsA, teamsB, scores, times = [], [], [], [], []
for match in previous:
	date = datetime.strptime(match.find_all('div', class_='fi-mu__info__datetime')[0].text.strip(),'%d %b %Y - %H:%M\r\n      Local time')
	teamA = match.find_all('span', class_='fi-t__nText')[0].text.strip()
	teamB = match.find_all('span', class_='fi-t__nText')[1].text.strip()
	score = match.find_all('span', class_='fi-s__scoreText')[0].text.strip()
	localTime = match.find_all('div', class_='fi-s__score')[0]['data-timeutc']
	time = (datetime.strptime(localTime,'%H:%M') + timedelta(hours=1)).time().strftime("%H:%M")

	dates.append(date)
	teamsA.append(teamA)
	teamsB.append(teamB)
	scores.append(score)
	times.append(time)

for match in fixtures:
	date = datetime.strptime(match.find_all('div', class_='fi-mu__info__datetime')[0].text.strip(),'%d %b %Y - %H:%M\r\n      Local time').date()
	teamA = match.find_all('span', class_='fi-t__nText')[0].text.strip()
	teamB = match.find_all('span', class_='fi-t__nText')[1].text.strip()
	score = match.find_all('span', class_='fi-s__scoreText')[0].text.strip()
	localTime = match.find_all('div', class_='fi-s__score')[0]['data-timeutc']
	time = (datetime.strptime(localTime,'%H:%M') + timedelta(hours=1)).time().strftime("%H:%M")
	date = str(date)+' '+str(time)

	dates.append(date)
	teamsA.append(teamA)
	teamsB.append(teamB)
	scores.append(score)
	times.append(time)

matches = pd.DataFrame({'Date': dates, 'Team A': teamsA, 'Team B': teamsB, 'Score': scores, 'Time': times})

# Add players to matches
matches = pd.merge(matches, teams[['Team','Player']], left_on='Team A', right_on='Team', how='left')
matches = matches.rename(columns = {'Player': 'Player A'})
matches = pd.merge(matches, teams[['Team','Player']], left_on='Team B', right_on='Team', how='left')
matches = matches.rename(columns = {'Player': 'Player B'})
matches = matches[['Date','Team A', 'Player A', 'Score', 'Player B', 'Team B','Time']]

matches.to_csv('./static/data/matches.csv', index=False)
