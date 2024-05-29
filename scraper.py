import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(req.content, "html.parser")

title_txt = soup.title
txt = soup.head



print('Title of Website: ', title_txt.get_text())
#print(txt.prettify())
#print(soup.get_text())