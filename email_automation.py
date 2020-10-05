import smtplib
import config
import time
import datetime
import csv
from account_manager import AccountManager
def fileOperation():
    filename = "test_final.csv"
    fields = []
    rows = []
    details={}
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
    except:
        print("File handling error!")
    for row in range(len(rows)):
        if not rows[row][0].isspace():
            details[rows[row][0]] = rows[row][-1]
    return details

class sendEmail:
    def getEmailandKey(self):
        self.details={}
        self.details=fileOperation()

    def send(self):
        while True:
            try:
                current_time = int(time.time())
                f_time=str(datetime.datetime.fromtimestamp(current_time).strftime("%I:%M:%S:%p"))
                if f_time=='01:19:30:AM':
                    try:
                        for self.key,self.value in self.details.items():
                            self.receiver=self.key
                            self.keyword=self.value
                            account_m_object = AccountManager(self.receiver,self.keyword)
                            article_object = account_m_object.get_articles()
                            self.msg=""
                            for obj in article_object:
                                Text = obj.summary
                                #print(obj.url,Text,obj.title)
                                self.msg+="\n"+obj.title+'.\n'+str(Text)+"\nTo know more about it follow the link- "+obj.url+"\n-----------------------------------------------\n"
                                #print(self.msg)
                            self.msg=self.msg.strip()
                            self.subject = "Never miss an update on your fav stuff"
                            self.message = 'Subject: {}\n\n{}'.format(self.subject, self.msg)
                            mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                            mailServer.starttls()
                            mailServer.login(config.email_address, config.email_password)
                            mailServer.sendmail(config.email_address, self.receiver, self.message.encode('utf-8'))
                            mailServer.quit()
                            print("Mail Sent!")
                        break
                    except:
                            print("Email Failed")
            except:
                print("Date Time error")
ob=sendEmail()
ob.getEmailandKey()
ob.send()

