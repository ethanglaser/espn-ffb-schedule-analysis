import json
import requests
from pprint import pprint
import pandas as pd
import sys

leagueId = sys.argv[3]
seasonId = sys.argv[4]
swid = sys.argv[2]
espn_s2 = sys.argv[1]
url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + str(seasonId) + '/segments/0/leagues/'  + str(leagueId) + '?'
url2 = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/' + str(seasonId) + '/segments/0/leagues/'  + str(leagueId) + '?view=mMatchup'

r = requests.get(url, cookies={"swid": swid, "espn_s2": espn_s2})
data = (json.loads(r.content))
teams = {}
for team in data['teams']:
    teams[team['id']] = {}
    teams[team['id']]['name'] = team['location'] + team['nickname']
    teams[team['id']]['scores'] = []
    teams[team['id']]['opponents'] = []
r2 = requests.get(url2, cookies={"swid": swid, "espn_s2": espn_s2})
data = json.loads(r2.content)
for game in data['schedule'][:13 * int(len(teams) / 2)]:
    teams[game['away']['teamId']]['scores'].append(game['away']['totalPoints'])
    teams[game['away']['teamId']]['opponents'].append(game['home']['teamId'])
    teams[game['home']['teamId']]['scores'].append(game['home']['totalPoints'])
    teams[game['home']['teamId']]['opponents'].append(game['away']['teamId'])
scheduleinfo = {}
for team1 in teams.keys():
    headtohead = []
    sameschedule = []
    for team2 in teams.keys():
        scores1 = teams[team1]['scores']
        scores2 = teams[team2]['scores']
        scores3 = []
        for index, opp in enumerate(teams[team2]['opponents']):
            scores3.append(teams[opp]['scores'][index])
        records = []
        for scores in [scores2, scores3]:
            wins = 0
            losses = 0
            ties = 0
            for score1, score2 in zip(scores1, scores):
                if score1 > score2:
                    wins += 1
                elif score1 < score2:
                    losses += 1
                else:
                    ties += 1
            record = str(wins) + '-' + str(losses)
            #if ties:
            #    record +=  '-' + str(ties)
            records.append(record)
        headtohead.append(records[0])
        sameschedule.append(records[1])
    scheduleinfo[team1] = {}
    scheduleinfo[team1]['name'] = teams[team1]['name']
    scheduleinfo[team1]['headtohead'] = headtohead
    scheduleinfo[team1]['sameschedule'] = sameschedule

h = [scheduleinfo[key]['headtohead'] for key in sorted(scheduleinfo.keys())]
s = [scheduleinfo[key]['sameschedule'] for key in sorted(scheduleinfo.keys())]
t = [scheduleinfo[key]['name'] for key in sorted(scheduleinfo.keys())]
hdf = pd.DataFrame(h, columns = t, index = t)
sdf = pd.DataFrame(s, columns = t, index = t)
hdf.to_excel(leagueId + '-' + seasonId + '-' + 'HeadToHeadRecords.xlsx')
sdf.to_excel(leagueId + '-' + seasonId + '-' + 'SameScheduleRecords.xlsx')
