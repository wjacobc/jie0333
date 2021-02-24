import feedparser
from newsitem import NewsItem
from datetime import datetime


def nejm_rss():
    nejm = feedparser.parse(
        "https://www.nejm.org/action/showFeed?jc=nejm&type=etoc&feed=rss")
    # print(nejm['entries'].keys)
    entries = nejm["entries"]

    newsitems = []
    for entry in entries:
        # convert the string date representation into a python datetime object
        date_object = datetime.strptime(
            entry["updated"], "%Y-%m-%dT%H:%M:%SZ"
        )
        headline = entry["title"]
        source = "New England Journal of Medicine"
        publish_date = date_object
        snippet = entry["summary"]
        url = entry["link"]

        newsitem = NewsItem(headline, source, publish_date, snippet, url)
        newsitems.append(newsitem)

    return newsitems
