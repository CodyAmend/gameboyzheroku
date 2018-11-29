from twitch import TwitchClient
from django.shortcuts import render, get_object_or_404
from .models import Stream
from igdb_api_python.igdb import igdb

import json

#API Keys
igdb = igdb("03af7252c1029ac5f2235e4d92e9ab4d")
client = TwitchClient('16uol26q1pagoqotdmycwmtmes42xb')

def Streaming_Landing(request):


    #Model availability:

    stream_model = Stream.objects.all()


    return render(request, 'Streaming_Landing.html',
                  {
                      'stream_model': stream_model,
                  })



def Streaming(request, slug):

    stream_get = get_object_or_404(Stream,
                                slug=slug)
    #Model availability:

    stream_model = Stream.objects.all()

    #twitch

    ov_vid_d = json.dumps(client.videos.get_top(1, 0, 'Overwatch', 'week', 'highlight')[0]['id'])
    ov_vid_l = json.loads(ov_vid_d)
    ov_vid_s = str(ov_vid_l)
    ov_vid_s = ov_vid_s.strip("v")
    ov_vid_url = "https://player.twitch.tv/?video=" + ov_vid_s + "&autoplay=false"

    rdr_vid_d = json.dumps(client.videos.get_top(1, 0, 'Red Dead Redemption 2', 'week', 'highlight')[0]['id'])
    rdr_vid_l = json.loads(rdr_vid_d)
    rdr_vid_s = str(rdr_vid_l)
    rdr_vid_s = rdr_vid_s.strip("v")
    rdr_vid_url = "https://player.twitch.tv/?video=" + rdr_vid_s + "&autoplay=false"

    gow_vid_d = json.dumps(client.videos.get_top(1, 0, 'God of War', 'week', 'highlight')[0]['id'])
    gow_vid_l = json.loads(gow_vid_d)
    gow_vid_s = str(gow_vid_l)
    gow_vid_s = gow_vid_s.strip("v")
    gow_vid_url = "https://player.twitch.tv/?video=" + gow_vid_s + "&autoplay=false"

    fort_vid_d = json.dumps(client.videos.get_top(1, 0, 'Fortnite', 'week', 'highlight')[0]['id'])
    fort_vid_l = json.loads(fort_vid_d)
    fort_vid_s = str(fort_vid_l)
    fort_vid_s = fort_vid_s.strip("v")
    fort_vid_url = "https://player.twitch.tv/?video=" + fort_vid_s + "&autoplay=false"

    botw_vid_d = json.dumps(client.videos.get_top(1, 0, 'The Legend of Zelda: Breath of the Wild', 'week', 'highlight')[0]['id'])
    botw_vid_l = json.loads(botw_vid_d)
    botw_vid_s = str(botw_vid_l)
    botw_vid_s = botw_vid_s.strip("v")
    botw_vid_url = "https://player.twitch.tv/?video=" + botw_vid_s + "&autoplay=false"


    #Overwatch (8713), RDR2 (25076), God of War (19560), BOTW (7346), Fortnite (1905)
    result = igdb.games({
        'ids': [8173, 25076, 19560, 7346, 1905],
        'expand': "developers",
        'fields': ['name', 'total_rating', 'total_rating_count', 'summary', 'popularity', 'developers.name']
    })

    #overwatch dumps / loads
    ov_name_d = json.dumps(result.body[0]['name'])
    ov_name_l = json.loads(ov_name_d)
    ov_tr_d = json.dumps(result.body[0]['total_rating'])
    ov_tr_l = json.loads(ov_tr_d)
    ov_trc_d = json.dumps(result.body[0]['total_rating_count'])
    ov_trc_l = json.loads(ov_trc_d)
    ov_sum_d = json.dumps(result.body[0]['summary'])
    ov_sum_l = json.loads(ov_sum_d)
    ov_pop_d = json.dumps(result.body[0]['popularity'])
    ov_pop_l = json.loads(ov_pop_d)
    ov_dev_d = json.dumps(result.body[0]['developers'])
    ov_dev_l = json.loads(ov_dev_d)
    ov_date = 'May 24 2016'

    #overwatch input processing

    ov_tr_r = round(ov_tr_l)
    ov_trc_r = round(ov_trc_l)
    ov_pop_r = round(ov_pop_l)
    ov_dev_s = str(ov_dev_l)
    ov_dev_s = ov_dev_s.split(': ')
    ov_dev_s = str(ov_dev_s[2])
    ov_dev_s = ov_dev_s.strip("'}]")

    #RDR2 dumps / loads
    rdr_name_d = json.dumps(result.body[1]['name'])
    rdr_name_l = json.loads(rdr_name_d)
    rdr_tr_d = json.dumps(result.body[1]['total_rating'])
    rdr_tr_l = json.loads(rdr_tr_d)
    rdr_trc_d = json.dumps(result.body[1]['total_rating_count'])
    rdr_trc_l = json.loads(rdr_trc_d)
    rdr_sum_d = json.dumps(result.body[1]['summary'])
    rdr_sum_l = json.loads(rdr_sum_d)
    rdr_pop_d = json.dumps(result.body[1]['popularity'])
    rdr_pop_l = json.loads(rdr_pop_d)
    rdr_dev_d = json.dumps(result.body[1]['developers'])
    rdr_dev_l = json.loads(rdr_dev_d)
    rdr_date = "October 26th 2018"

    #RDR2 input processing

    rdr_tr_r = round(rdr_tr_l)
    rdr_trc_r = round(rdr_trc_l)
    rdr_pop_r = round(rdr_pop_l)
    rdr_dev_s = str(rdr_dev_l)
    rdr_dev_s = rdr_dev_s.split(': ')
    rdr_dev_s = str(rdr_dev_s[2])
    rdr_dev_s = rdr_dev_s.strip("'}]")

    #GOW dumps / loads
    gow_name_d = json.dumps(result.body[2]['name'])
    gow_name_l = json.loads(gow_name_d)
    gow_tr_d = json.dumps(result.body[2]['total_rating'])
    gow_tr_l = json.loads(gow_tr_d)
    gow_trc_d = json.dumps(result.body[2]['total_rating_count'])
    gow_trc_l = json.loads(gow_trc_d)
    gow_sum_d = json.dumps(result.body[2]['summary'])
    gow_sum_l = json.loads(gow_sum_d)
    gow_pop_d = json.dumps(result.body[2]['popularity'])
    gow_pop_l = json.loads(gow_pop_d)
    gow_dev_d = json.dumps(result.body[2]['developers'])
    gow_dev_l = json.loads(gow_dev_d)
    gow_date = "April 20th 2018"

    #GOW input processing

    gow_tr_r = round(gow_tr_l)
    gow_trc_r = round(gow_trc_l)
    gow_pop_r = round(gow_pop_l)
    gow_dev_s = str(gow_dev_l)
    gow_dev_s = gow_dev_s.split(': ')
    gow_dev_s = str(gow_dev_s[2])
    gow_dev_s = gow_dev_s.strip("'}]")

    # BOTW dumps / loads

    botw_name_d = json.dumps(result.body[3]['name'])
    botw_name_l = json.loads(botw_name_d)
    botw_tr_d = json.dumps(result.body[3]['total_rating'])
    botw_tr_l = json.loads(botw_tr_d)
    botw_trc_d = json.dumps(result.body[3]['total_rating_count'])
    botw_trc_l = json.loads(botw_trc_d)
    botw_sum_d = json.dumps(result.body[3]['summary'])
    botw_sum_l = json.loads(botw_sum_d)
    botw_pop_d = json.dumps(result.body[3]['popularity'])
    botw_pop_l = json.loads(botw_pop_d)
    botw_dev_d = json.dumps(result.body[3]['developers'])
    botw_dev_l = json.loads(botw_dev_d)
    botw_date = "March 3rd 2017"

    # BOTW input processing

    botw_tr_r = round(botw_tr_l)
    botw_trc_r = round(botw_trc_l)
    botw_pop_r = round(botw_pop_l)
    botw_dev_s = str(botw_dev_l)
    botw_dev_s = botw_dev_s.split(': ')
    botw_dev_s = str(botw_dev_s[2])
    botw_dev_s = botw_dev_s.strip("'}]")

    # Fortnite dumps / loads

    fort_name_d = json.dumps(result.body[4]['name'])
    fort_name_l = json.loads(fort_name_d)
    fort_tr_d = json.dumps(result.body[4]['total_rating'])
    fort_tr_l = json.loads(fort_tr_d)
    fort_trc_d = json.dumps(result.body[4]['total_rating_count'])
    fort_trc_l = json.loads(fort_trc_d)
    fort_sum_d = json.dumps(result.body[4]['summary'])
    fort_sum_l = json.loads(fort_sum_d)
    fort_pop_d = json.dumps(result.body[4]['popularity'])
    fort_pop_l = json.loads(fort_pop_d)
    fort_dev_d = json.dumps(result.body[4]['developers'])
    fort_dev_l = json.loads(fort_dev_d)
    fort_date = "July 25 2017"

    # Fortnite input processing

    fort_tr_r = round(fort_tr_l)
    fort_trc_r = round(fort_trc_l)
    fort_pop_r = round(fort_pop_l)
    fort_dev_s = str(fort_dev_l)
    fort_dev_s = fort_dev_s.split(': ')
    fort_dev_s = str(fort_dev_s[2])
    fort_dev_s = fort_dev_s.strip("'}]")

    #if statements

    if slug == 'fortnite':
        name = fort_name_l
        total_r = fort_tr_r
        total_rc = fort_trc_r
        summary = fort_sum_l
        popularity = fort_pop_r
        developer = fort_dev_s
        rel_date = fort_date
        url_link = fort_vid_url
    elif slug == 'god-war':
        name = gow_name_l
        total_r = gow_tr_r
        total_rc = gow_trc_r
        summary = gow_sum_l
        popularity = gow_pop_r
        developer = gow_dev_s
        rel_date = gow_date
        url_link = gow_vid_url
    elif slug == 'overwatch':
        name = ov_name_l
        total_r = ov_tr_r
        total_rc = ov_trc_r
        summary = ov_sum_l
        popularity = ov_pop_r
        developer = ov_dev_s
        rel_date = ov_date
        url_link = ov_vid_url
    elif slug == 'red-dead-redemption-2':
        name = rdr_name_l
        total_r = rdr_tr_r
        total_rc = rdr_trc_r
        summary = rdr_sum_l
        popularity = rdr_pop_r
        developer = rdr_dev_s
        rel_date = rdr_date
        url_link = rdr_vid_url
    elif slug == 'zelda-breath-wild':
        name = botw_name_l
        total_r = botw_tr_r
        total_rc = botw_trc_r
        summary = botw_sum_l
        popularity = botw_pop_r
        developer = botw_dev_s
        rel_date = botw_date
        url_link = botw_vid_url
    else:
        name = 'ERROR'
        total_r = 'ERROR'
        total_rc = 'ERROR'
        summary = 'ERROR'
        popularity = 'ERROR'
        developer = 'ERROR'
        rel_date = 'ERROR'
        url_link = 'ERROR'

    return render(request, 'videos.html',
                  {
                   'stream_get': stream_get,
                   'stream_model' : stream_model,
                   'developer' : developer,
                   'name': name,
                   'total_r': total_r,
                   'total_rc': total_rc,
                   'summary': summary,
                   'rel_date': rel_date,
                   'popularity': popularity,
                   'url_link': url_link
                   })

















