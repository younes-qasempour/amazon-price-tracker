import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = soup.find('span', class_='aok-offscreen').text.strip()
price = float(price[1:])

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('<EMAIL>', '<PASSWORD>')