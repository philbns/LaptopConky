#!/usr/bin/python
#
# Fetches Weather info from Weather Underground
#
# Usage: ./wundergound.py zipcode
#
# International:
#  * Go to http://www.wunderground.com/
#  * Find your city
#  * Click the RSS icon
#  * Station ID is the number that follows /stations/ in the url
#
#

# Values are either True or False
metric=False
international=False

import sys
import feedparser

def usage():
    print("Usage:")
    if international:
        print("  ./wunderground.py StationID")
    else:
        print("  ./weunderground.py zipcode")
    sys.exit(1)

if not len(sys.argv) == 2:
    usage()

location=sys.argv[1]

if international:
    url="http://rss.wunderground.com/auto/rss_full/global/stations/"
else:
    url="http://rss.wunderground.com/auto/rss_full/"

feed=feedparser.parse(url+location)

if not feed.feed:
    # Assume Error
    print("Error")
    sys.exit(1)

current=feed['items'][0].title

if metric:
    temp=current.split(",")[0].split(":")[1].split("/")[1].strip()
else:
    temp=current.split(",")[0].split(":")[1].split("/")[0].strip()

condition=current.split(",")[1].split("-")[0].strip()

print(temp, "-", condition)
