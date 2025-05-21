from bs4 import BeautifulSoup
import requests
import smtplib


username = YOUR_USERNAME
password = YOUR_PASSOWRD
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# ====================== Add Headers to the Request ===========================
# Full headers would look something like this
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

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }


response =requests.get(url=url)
soup = BeautifulSoup(response.text, features="html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").getText()
# print(price)

#We get hold of only the number excluding the currency
price_without_currency = price.split("$")[1]

#Coverting price as floating point number
price_as_float = float(price_without_currency)
# print(price_as_float)

# ================================= Send an Email ===========================
title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!!!"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username,password=password)
        connection.sendmail(from_addr=username,
                            to_addrs=TO_MAIL_ADDRESS,
                            msg = f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
                            )




