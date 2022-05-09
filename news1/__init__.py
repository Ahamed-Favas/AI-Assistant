from news1 import news
class nws:
    def news(self):
            """
            Fetch top news of the day from google news
            :return: news list of string if True, False if fail
            """
            return news.get_news()