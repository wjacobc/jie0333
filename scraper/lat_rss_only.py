import feedparser
import firebase_utils
from newsitem import NewsItem
from datetime import datetime

def nyt_rss():
    nyt = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml")
    entries = nyt["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")
        # remove the time zone offset so we can compare it to other newsitems
        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "The New York Times"
        publish_date = date_object
        # some NYT articles have empty snippets, should we skip these
        # or try to create one?
        snippet = entry["summary"]
        url = entry["link"]
        # NYT has tags in entry["tags"] - do we want to use these?
        # problem is they will likely not line up with the ones we generate

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems