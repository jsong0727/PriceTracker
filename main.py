import requests
from bs4 import BeautifulSoup
import smtplib



url = "https://www.amazon.com/LEGO-Super-Destroyer-Discontinued-manufacturer/dp/B0050R0YB8/ref=sr_1_2?crid" \
      "=2X7DL8EAVIMJN&keywords=lego&qid=1657251105&sprefix=leg%2Caps%2C298&sr=8-2&ufe=app_do%3Aamzn1.fos.4dd97f68" \
      "-284f-40f5-a6f1-1e5b3de13370 "
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1].replace(",", "")
price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)
BUY_PRICE = 1000


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
