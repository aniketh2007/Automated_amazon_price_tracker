# Automated_amazon_price_tracker
- The main aim of this product is when the price of a product comes down to your required price then you will get the email that you could buy that product
- Step 1: First we use requests module API to send an API request then get the data.
- Step 2: we use beautiful soup module for web scrapping and get hold that data and use find() method and getText() method with class name to get hold of the price. Then we use strip method to seperate from $ symbol. Also we get hold of the title or the product name using find() method and getting hold of class name and using getText() method.
- Step 3 : We then set a price to which the user desires for it. If the price is met then you will use the smtplib module to send the person an email stating that the price has been met and the person can buy it.
- Step 4: We use the concept of headers because we don't want amazon think that we are bot like language:eu-us and so on.
