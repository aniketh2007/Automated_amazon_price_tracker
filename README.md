# 🛒 Automated Amazon Price Tracker
The goal of this project is to automatically track the price of a product on Amazon. When the product’s price drops below your target price, you will receive an email notification alerting you that it's time to buy.
-📌 Steps Involved:
- Step 1: Fetching the Webpage
Use the requests module to send a GET request to the product’s URL.Include custom headers (like User-Agent) to mimic a real browser and avoid being blocked by Amazon.

- Step 2: Web Scraping with BeautifulSoupUse the BeautifulSoup library to parse the HTML response.Extract the product price using the .find() method with the appropriate class name.Remove currency symbols (like ₹ or $) and commas to convert the string to a float.Also extract the product title for use in the email.

- Step 3: Set Target Price and Compare. Define a BUY_PRICE — the price at which you want to purchase the product.If the current product price is less than BUY_PRICE, prepare a message.

- Step 4: Send Email Notification. Use the smtplib module to send an email with the product name, current price, and purchase link.Email will be sent only if the price condition is met.
