from keyword_processor import KeywordProcessor

try:
    import pandas as pd
except:
    print("missing module: pandas")

src = r"C:\Users\mohammed\Documents\Projects\tests\user_database.csv"  # add the path to the user database

try:
    f = open(src, 'x')
    f.write("Email ID,Keywords")
    f.close()
    database = pd.read_csv(src)
except FileExistsError:
    database = pd.read_csv(src)

df = pd.DataFrame(database)


def save():
    """
    saves changes to the user database
    """
    with open(src, 'w') as f_:
        df.to_csv(f_, index=False)


class AccountManager:
    def __init__(self, email_id, keywords):
        self.email_id = email_id.strip()
        self.keywords = keywords.strip()

    def subscribe(self):
        """
        subscribes the user to the mailing list
        """
        global df
        self.unsubscribe()  # to overwrite account preferences
        df = df.append({'Email ID': self.email_id, 'Keywords': self.keywords}, ignore_index=True)

        save()

    def unsubscribe(self):
        """
        unsubscribes the user from the mailing list\
        """
        global df
        filter_ = df["Email ID"] != self.email_id
        df.where(filter_, inplace=True)
        df.dropna(inplace=True)

        save()

    def get_articles(self):
        """
        returns a list of articles most relevant to he given keyword
        """
        article_list = []
        for keyword in self.keywords.split('-'):
            # print("Keyword/s:", keyword, '\n')
            kp = KeywordProcessor(keyword.strip())
            article_list.append(kp.most_relevant())
        return article_list

    def display_articles(self):
        """
        test function
        displays the articles and their links
        """
        article_list = self.get_articles()
        print("Best Article/s:")
        print("Keyword/s:", self.keywords, '\n')
        for article in article_list:
            print(article[0].title, '\n\n', article[0].text, '\n\n', article[1], '\n\n')
