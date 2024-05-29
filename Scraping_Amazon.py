#Amazon - Web Scarping

import requests
from bs4 import BeautifulSoup
import smtplib
import time
import datetime

#connect to website
url = 'https://www.amazon.com/Palace-Illusions-Chitra-Banerjee-Divakaruni/dp/1400096200/ref=sr_1_1?crid=2LVWS046RYOBG&dib=eyJ2IjoiMSJ9.K76pkiUaFLG20lprFZv2XAVjs69J6LUuYVjtHBlondryI-m1VguQJSvJotkqcdsHw2jbnO-sN8aUuYpY5ydrTVcWotwehD-LrbAcntefc3OeYaF24xDBZEK65yeCIWefib8d6rrBwpWkdoPLTNa-C8tDNMHQskxW7ULJcXZ5FClfk6jIJjbhaa6coafO_RMY0JLLM3LNKlNLNfsBDbrJWED1605--qpMvoG5G5iKCcw.AvHHnFWqYXSp2w1WoxBAvb2CWM2By4hpl1NwsI3i36g&dib_tag=se&keywords=palace+of+illusions+by+chitra+banerjee&qid=1716983626&sprefix=palace%2Caps%2C636&sr=8-1'
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-665717dd-7fc2abe470f0d1e72018c187"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#title = soup2.find(id="title").get_text()

#print(soup1)
print(soup2)
#print(title)