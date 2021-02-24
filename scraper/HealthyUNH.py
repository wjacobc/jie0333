import feedparser
from newsitem import NewsItem
from datetime import datetime

def healthyUNH_rss():
    HealthyUNH = feedparser.parse("https://www.unh.edu/healthyunh/blog.xml")
    entries = HealthyUNH["entries"]

    newsitems = []
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %z")

        date_object = date_object.replace(tzinfo = None)

        headline = entry["title"]
        source = "Healthy UNH"
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