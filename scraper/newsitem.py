class NewsItem():
    def __init__(self, headline, source, publish_date, snippet, url):
        self.headline = headline
        self.source = source
        self.publish_date = publish_date
        self.snippet = snippet
        self.url = url
        self.tags = []


    def __repr__(self):
        return f"{self.source}: {self.headline} - {self.snippet.strip()} - {self.publish_date}"


    def to_json(self):
        json_dict = {"headline": self.headline, "source": self.source, "publish_date": str(self.publish_date),
                        "snippet": self.snippet, "url": self.url, "tags": str(self.tags)}
        return json_dict
