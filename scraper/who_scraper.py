import feedparser
from newsitem import NewsItem
from datetime import datetime

def who_rss():
    who=feedparser.parse("https://www.who.int/feeds/entity/csr/don/en/rss.xml")
    entries=who["entries"]
    newsitems=[]
    for entry in entries:
        date_object = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %Z")
        date_object=date_object.replace(tzinfo=None)
        headline = entry["title"]
        source = "World Health Organization"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem_entry = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem_entry)

    return newsitems

if __name__=="__main__":
    print(who_rss())
