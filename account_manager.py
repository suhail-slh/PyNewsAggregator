from keyword_processor import KeywordProcessor
try:
	import pandas as pd
except:
	print("module pandas not installed")

src = r"user_database.csv" #add the path to the user database
src2 = r"" #add the path to the directory where the links will be stored

try:        
	f = open(src, 'x') 
	f.write("Email ID,Keywords")
	f.close()
	database = pd.read_csv(src);
except FileExistsError:
	database = pd.read_csv(src);

df = pd.DataFrame(database)

class AccountManager:
	def __init__(self):
		self.email_id = ''
		self.keywords = ''
		self.links = []
	
	def subscribe(self,email_id,keywords):
		self.email_id = email_id.strip()
		self.keywords = keywords.strip()
		
		global df
		df = df.append({'Email ID':self.email_id,'Keywords':self.keywords}, ignore_index=True)
		df.dropna(inplace = True)
		
		with open(src, 'w') as f:
			df.to_csv(f, index = False)
			
		self.get_links()
		
		with open(src2+"\\"+self.email_id.split('@')[0]+".txt", "a") as f:
			for link in self.links:
				f.write(link+",")
			
	def unsubscribe(self,email_id):
		global df
		filter = df["Email ID"]!=email_id.strip()
		df.where(filter, inplace = True)
		df.dropna(inplace = True)
		
		with open(src, 'w') as f:
			df.to_csv(f, index = False)
			
	def get_links(self):
		for keyword in self.keywords.split(','):
			KP = KeywordProcessor(keyword)
			self.links.append(KP.most_relevant())
		
	def __str__(self):
		pass