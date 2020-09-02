try:
	from newspaper import Article
	from googlesearch import search	
except:
	print("modules newspaper and/or googlesearch not installed")

class KeywordProcessor:
	def __init__(self,keyword):
		self.keyword = keyword
	
	def fetch_links(self):
		return search(self.keyword+" news", tld="co.in", num=5, stop=5, pause=2)
		
	def display_links(self):
		try:
			for link in self.fetch_links():
				print(link)
		except:
			pass
			
	def most_relevant(self):	
		most_relevant_site = ''
		
		for link in self.fetch_links():
			try:
				article = Article(link)
				article.download()
				
				most_relevant_site = link
				break
			except: 
				pass
				
		return most_relevant_site