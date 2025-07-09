import asyncio
import re
import smtplib
from email.message import EmailMessage
from typing import Collection, List, Tuple, Union
import dotenv
import aiosmtplib
import os
from dotenv import load_dotenv

HOST = "smpt.gmail.com"

CARRIER_MAP = {
    "verizon": "vtext.com",
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

        print(email)
        print(pswd)

        car = carrier.lower()
        subject = "BOGO Notification"

        phoneEmail = str(phoneNum) + "@vtext.com"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, pswd)
        server.sendmail(email, phoneEmail, message)
        server.quit()




    async def sendTxt(self,
            num: Union[str, int], carrier: str, email: str, pword: str, msg: str, subj: str
    ) -> Tuple[dict, str]:
        to_email = CARRIER_MAP[carrier]

        # build message
        message = EmailMessage()
        message["From"] = email
        message["To"] = f"{num}@{to_email}"
        message["Subject"] = subj
        message.set_content(msg)

        # send
        send_kws = dict(username=email, password=pword, hostname=HOST, port=587, start_tls=True)
        res = await aiosmtplib.send(message, **send_kws)  # type: ignore
        msg = "failed" if not re.search(r"\sOK\s", res[1]) else "succeeded"
        print(msg)
        return res



if __name__ == "__main__":
    sms = SMS()
    message = "hi"

    coro = sms.sendNotification(6085093061, "Verizon", message)

    asyncio.run(coro)
