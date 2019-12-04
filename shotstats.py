#Requires DATABASE_URL setup as system variable

import pandas as pd
import requests
import json
import psycopg2 as psy
from flask_sqlalchemy import SQLAlchemy
import os 
from sqlalchemy import create_engine, MetaData, Table


db_url = os.environ['DATABASE_URL']

team = 'sixers'

engine = create_engine(db_url)
metadata = MetaData(bind=engine)

sqlstarters = "select player from starters where team = '" + team + "';"

starters=[]

with engine.connect() as con:

    rs = con.execute(sqlstarters)

    for row in rs:
        starters.append(row[0])

con.close()

playerfiln = 'LEFT(DISPLAY_FIRST_LAST, 1) || \'. \' ||LEFT(DISPLAY_LAST_COMMA_FIRST, POSITION(\',\' IN DISPLAY_LAST_COMMA_FIRST)-1)'
                                             
with engine.connect() as con:

    playerids=[]

    for player in starters:

        sqlplayerid = 'select PERSON_ID from players where ' + playerfiln + '=\'' +  player + '\''

        rs = con.execute(sqlplayerid)

        for row in rs:
            playerids.append(row[0])
        
con.close()
  
con = engine.connect()
con.execute('truncate table shots;')
con.close()

with engine.connect() as con:

    for playerid in playerids:
        url = url = 'https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=2018-19&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=' + str(playerid) + '&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response = requests.get(url, headers=headers)

        header = response.json()['resultSets'][0]['headers']
        shots = response.json()['resultSets'][0]['rowSet']

        for shot in shots:
            sqlshot = 'INSERT INTO shots (GRID_TYPE,GAME_ID,GAME_EVENT_ID,PLAYER_ID,PLAYER_NAME,TEAM_ID,TEAM_NAME,PERIOD,MINUTES_REMAINING,SECONDS_REMAINING,EVENT_TYPE,ACTION_TYPE,SHOT_TYPE,SHOT_ZONE_BASIC,SHOT_ZONE_AREA,SHOT_ZONE_RANGE,SHOT_DISTANCE,LOC_X,LOC_Y,SHOT_ATTEMPTED_FLAG,SHOT_MADE_FLAG,GAME_DATE,HTM,VTM) VALUES (' + str(shot)[1:len(str(shot))-1] + ');'
            con.execute(sqlshot)
con.close()