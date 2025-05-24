import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import schedule
import time


# ==== CONFIGURATION ====
URL = 'https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX3TW6X/ref=sr_1_5?crid=16ZGP67Q1UYCE&dib=eyJ2IjoiMSJ9.8-aKrERwPzdGyJWfWOa56I4wwdlI59jT8Bz9mNMoRuI2jxaiHGLt-9jMmKFSoG5ONSKetZieynA4mmtx_3AZYAEfT2m18MhLSs0r25dX9PEPXqZm3XRr5pZtoMfVviCmA29dTIn3eRxZPIS3fQ86NwRHMYINUCT68oPmQtFynWgh6dta9Aj5sKEP_xEcZsjQdiEWDzPGZTwlmt58vsKp_JiuJozsS7smXJXJ_W1hcQk.Cz4OyjDPVUdNe6DC-yHFbb_UZVagWizAVRoSdDi2TTQ&dib_tag=se&keywords=iphone%2B15&qid=1748081053&sprefix=iphone%2B15%2Caps%2C316&sr=8-5&th=1'  # Replace with your product URL
TARGET_PRICE = 50000  # Set your target price in INR
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def check_price():
    try:
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try multiple possible price tags (Amazon changes often)
        price_string = (
            soup.find(id="priceblock_ourprice") or
            soup.find(id="priceblock_dealprice") or
            soup.find("span", class_="a-price-whole")
        )

        if not price_string:
            print("❌ Could not find the price on the page.")
            return

        price = float(price_string.get_text().replace(",", "").replace("₹", "").strip())

        print(f"✅ Current Price: ₹{price}")

        if price <= TARGET_PRICE:
            send_email(price)

    except Exception as e:
        print(f"❌ Error checking price: {e}")

def send_email(current_price):
    try:
        subject = "📉 Price Alert: Your Amazon Product is Now ₹{:.2f}".format(current_price)
        body = f"Your product is now ₹{current_price}.\nCheck it here: {URL}"

        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📧 Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Run once for testing
# check_price()

# Schedule it to run once daily at 9:00 AM (you can change the time)
schedule.every().day.at("09:00").do(check_price)

print("📅 Running daily Amazon price check...")

while True:
    schedule.run_pending()
    time.sleep(60)  # check every 60 seconds

