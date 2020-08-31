from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

if __name__ == '__main__':
    API_KEY = '567ebf2d5a7b597bc3950ec8b0fc2156'
    URL_TO_SCRAPE = 'https://httpbin.org/ip'

# Path of chromedriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

contents = list()

search = input('Enter topic to search: ')

# Run google searches
# driver.get('https://www.google.com/search?q=' + search)

if search == 'sports' :
    driver.get('https://timesofindia.indiatimes.com/sports/more-sports/top-stories/lateststories/4719148.cms')
    
    try:
        # waits for the page to load until the presence of content tag is found but for a maximum of 10 sec
        content = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "content"))
        )
        
        print(content.text)
        # driver.quit()
    except  :
        driver.quit()


# For IP Rotation
payload = {'api_key': API_KEY, 'url': URL_TO_SCRAPE}
r = requests.get('http://api.scraperapi.com', params=payload, timeout=60)
print(r.text)
while True: pass