try:
	from GoogleNews import GoogleNews
	import datetime	
	import re
except:
	print("missing module/s: GoogleNews and/or datetime")

class KeywordProcessor:
	def __init__(self,keyword):
		self.keyword = keyword
	
	def fetch_links(self):
		try:
			currentdate = datetime.datetime.now()
			fromdate = currentdate - datetime.timedelta(days=1) 

			currentdate = str(currentdate.month)+'/'+str(currentdate.day)+'/'+str(currentdate.year)
			fromdate = str(fromdate.month)+'/'+str(fromdate.day)+'/'+str(fromdate.year)
			
			googlenews = GoogleNews()

			googlenews.setlang('en')
			googlenews.setTimeRange(fromdate, currentdate)

			googlenews.search(self.keyword)
			
			return googlenews.result()
		except:
			return ''
		
	def display_links(self):
		try:
			for link in self.fetch_links():
				print(link.get('link',''))
		except:
			pass
			
	def most_relevant(self):
		pattern = self.keyword
		max_matches = 0
		most_relevant_site = ''
		for link in self.fetch_links():
			try:
				matches = re.findall(pattern, link.get('desc',''), re.IGNORECASE)
				if len(matches) > max_matches:
					max_matches = len(matches)
					most_relevant_site = link.get('link','')
			except:
				pass
		return most_relevant_site
