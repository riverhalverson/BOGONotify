import asyncio
import re
import smtplib
from email.message import EmailMessage
from typing import Collection, List, Tuple, Union
import dotenv
import aiosmtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

HOST = "smpt.gmail.com"

CARRIER_MAP = {
    "verizon": "@vzwpix.com",
    "tmobile": "tmomail.net",
    "sprint": "messaging.sprintpcs.com",
    "at&t": "txt.att.net",
    "boost": "smsmyboostmobile.com",
    "cricket": "sms.cricketwireless.net",
    "uscellular": "email.uscc.net",
}

class SMS:

    def sendNotification(self, phoneNum, carrier, message):
        load_dotenv()

        email = os.getenv("EMAILAD")
        pswd = os.getenv("EMAILPS")

        car = carrier.lower()
        subject = "BOGO Notification"

        msg = MIMEMultipart()
        msg['Subject'] = "BOGO Notifier"
        msg['From'] = "riverhalverson@gmail.com"
        body = message

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        phoneEmail = str(phoneNum) + "@vzwpix.com"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, pswd)
        server.sendmail(email, phoneEmail, msg.as_string())
        server.quit()

    def sendEmail(self, message):
        load_dotenv()

        email = os.getenv("EMAILAD")
        pswd = os.getenv("EMAILPS")

        msg = MIMEMultipart()
        msg['Subject'] = "BOGO Notifier"
        msg['From'] = "riverhalverson@gmail.com"
        body = message

        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, pswd)
        server.sendmail(email, "riverhalverson@gmail.com", msg.as_string())
        server.quit()