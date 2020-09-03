try:
    from GoogleNews import GoogleNews
    import datetime
    import re
except:
    print("missing module/s: GoogleNews and/or datetime")


class KeywordProcessor:
    def __init__(self, keyword):
        self.keyword = keyword

    def fetch_links(self):
        try:
            to_date = datetime.datetime.now()
            from_date = to_date - datetime.timedelta(days=1)

            to_date = str(to_date.month) + '/' + str(to_date.day) + '/' + str(to_date.year)
            from_date = str(from_date.month) + '/' + str(from_date.day) + '/' + str(from_date.year)

            google_news = GoogleNews()

            google_news.setlang('en')
            google_news.setTimeRange(from_date, to_date)

            google_news.search(self.keyword)

            return google_news.result()
        except:
            return ''

    def display_links(self):
        try:
            for link in self.fetch_links():
                print(link.get('link', ''))
        except:
            pass

    def most_relevant(self):
        pattern = self.keyword
        max_matches = 0
        most_relevant_site = ''
        for link in self.fetch_links():
            try:
                matches = re.findall(pattern, link.get('desc', ''), re.IGNORECASE)
                if len(matches) > max_matches:
                    max_matches = len(matches)
                    most_relevant_site = link.get('link', '')
            except:
                pass
        return most_relevant_site
