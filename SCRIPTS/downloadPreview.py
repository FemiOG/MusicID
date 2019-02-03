import os
import sys
import urllib2
from xml.dom import minidom

def url_call(url):
    """
    Do a simple request to the 7digital API
    We assume we don't do intense querying, this function is not
    robust
    Return the answer as na xml document
    """
    stream = urllib2.urlopen(url)
    xmldoc = minidom.parse(stream).documentElement
    stream.close()
    return xmldoc

def get_trackid_from_text_search(title,artistname=''):
    """
    Search for an artist + title using 7digital search API
    Return None if there is a problem, or tuple (title,trackid)
    """
    url = 'http://api.7digital.com/1.2/track/search?'
    url += 'oauth_consumer_key=' #+ DIGITAL7_API_KEY
    query = title
    if artistname != '':
        query = artistname + ' ' + query
    query = urllib2.quote(query)
    url += '&q='+query
    xmldoc = url_call(url)
    status = xmldoc.getAttribute('status')
    if status != 'ok':
        return None
    resultelem = xmldoc.getElementsByTagName('searchResult')
    if len(resultelem) == 0:
        return None
    track = resultelem[0].getElementsByTagName('track')[0]
    tracktitle = track.getElementsByTagName('title')[0].firstChild.data
    trackid = int(track.getAttribute('id'))
    return (tracktitle,trackid)