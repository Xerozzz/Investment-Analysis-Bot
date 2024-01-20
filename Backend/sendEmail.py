from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import smtplib
from dotenv import load_dotenv
from datetime import date

load_dotenv()
today = date.today().strftime("%d%m%y")

def sendEmail(dirname):
    # Email yourself daily report
    Body_of_Email = MIMEText("""\
        Here is your stock report for the day!

        Sincerely,
        Your Computer
    """, 'plain')

    message = MIMEMultipart()
    filename = f'report_{today}.pdf'
    with open(f"{dirname}\\Daily_Stock_Report\\Reports\\{filename}", "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    message["To"] = email
    message["From"] = email
    message["Subject"] = 'Daily Stock Report'
    message.attach(Body_of_Email)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message.as_string())
    server.quit()
    print("Report sent!")
