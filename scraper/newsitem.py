class NewsItem():
    def __init__(self, headline, source, publish_date, snippet, url, tags = []):
        self.headline = headline
        self.source = source
        self.publish_date = publish_date
        self.snippet = snippet
        self.url = url
        self.tags = tags

    def __repr__(self):
        return f"{self.source}: {self.headline} - {self.snippet.strip()} - {self.publish_date}"

