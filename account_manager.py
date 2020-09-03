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
    with open(src, 'w') as f_:
        df.to_csv(f_, index=False)


class AccountManager:
    def __init__(self, email_id, keywords):
        self.email_id = email_id.strip()
        self.keywords = keywords.strip()
        self.links = []

    def subscribe(self):
        global df
        self.unsubscribe()  # to overwrite account preferences
        df = df.append({'Email ID': self.email_id, 'Keywords': self.keywords}, ignore_index=True)

        save()

        self.get_links()

        # replace with send_mail function
        print("Keywords:", self.keywords)
        for link in self.links:
            print(link)

    def unsubscribe(self):
        global df
        filter_ = df["Email ID"] != self.email_id
        df.where(filter_, inplace=True)
        df.dropna(inplace=True)

        save()

    def get_links(self):
        for keyword in self.keywords.split(','):
            kp = KeywordProcessor(keyword.strip())
            self.links.append(kp.most_relevant())
