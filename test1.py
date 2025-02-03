import requests
from bs4 import BeautifulSoup

print("Hello World!")

response = requests.get("https://www.tagesschau.de")
soup = BeautifulSoup(response.text, 'html.parser')
all_text = soup.get_text(separator='\n', strip=True)
#div_text=soup.find("div",{"class":"layout-container"}).get_text()
#article_text=soup.find("article").get_text(separator='\n', strip=True)
print(all_text[:200])