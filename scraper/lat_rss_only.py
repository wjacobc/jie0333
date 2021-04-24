import feedparser
import firebase_utils
from newsitem import NewsItem
from datetime import datetime

def lat_rss():
    lat = feedparser.parse("https://www.latimes.com/science/rss2.0.xml")
    entries = lat["entries"]

    newsitems = []
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")

        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "The Los Angeles Times"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems