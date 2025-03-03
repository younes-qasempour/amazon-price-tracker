import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

SET_VALUE = 100

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(live_url, headers=header)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = soup.find('span', class_='aok-offscreen').text.strip()
price = float(price.split()[0][1:])
title =soup.find('span', id="productTitle").text.strip()

if price < SET_VALUE:
    message = f"{title} is on sale for {price}!"
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
    connection.sendmail(
        from_addr=os.getenv("EMAIL"),
        to_addrs=os.getenv("TO_EMAIL"),
        msg= f"Subject:Amazon Price Alert!\n\n"
             f"{message}\n{live_url}".encode("utf-8")
    )