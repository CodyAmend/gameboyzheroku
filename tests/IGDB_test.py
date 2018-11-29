from igdb_api_python.igdb import igdb
from decimal import Decimal
import requests
import json
import time,os
from twitch import TwitchClient


#igdb = igdb("03af7252c1029ac5f2235e4d92e9ab4d")
client = TwitchClient('16uol26q1pagoqotdmycwmtmes42xb')



"""


#Rounding Example

result2 = igdb.games({
    'ids': 1942,
    'expand': "developers",
    'fields': ['developers.name', 'name', 'total_rating', 'total_rating_count']
})
game2 = result2.body[0]['total_rating']

for game in result2.body:
    print(game2)

x = round(result2.body[0]['total_rating'],2)
print (x)

"""



"""

#Standard example

result = igdb.games({
        'ids': 8173,
        'fields': ['name', 'total_rating', 'total_rating_count']
    })

game1 = json.dumps(result.body[0]['total_rating_count'])
games1 = json.loads(game1)

for game in result.body:
    print(games1)
"""

"""
# Processing 

x = str(games1) #json dict to string
x2 = x.split(': ') #splits string based on character
x2 = str(x2[2]) #focuses on what we want
x2 = x2.strip("'}]") #strips extra objects
print(x2)

xr = round(games1,2) #rounds total_ratings
print(xr)



"""

"""

#TWITCH Examples

ov_vid_d = json.dumps(client.videos.get_top(1, 0, 'Overwatch', 'week', 'highlight')[0]['id'])
ov_vid_l = json.loads(ov_vid_d)
ov_vid_s = str(ov_vid_l)
ov_vid_s = ov_vid_s.strip("v")
ov_vid_url = "https://player.twitch.tv/?video=" + ov_vid_s + "&autoplay=false"

print(ov_vid_url)

"""