from youtube_tools import *

def yt(query):
    try:
        print "=> Searching for results ..."
        
        # PROCESS QUERY TO GENERATE PROPER LINK
        url = "https://www.youtube.com/results?search_query=%s" % "+".join([p for p in query.split(" ")])
        return get_videos(soup_url(url))
    except IOError as e:
        print e.strerror

