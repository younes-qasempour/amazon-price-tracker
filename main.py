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

message = "Hello"


smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
smtp.sendmail(
    from_addr=os.getenv("EMAIL"),
    to_addrs=os.getenv("TO_EMAIL"),
    msg=f"subject:HI\n\n{message}"
)