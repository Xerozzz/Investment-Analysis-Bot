import yfinance as yf, pandas as pd, shutil, os, time, glob, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def sendEmail(dirname):
    # Email yourself daily report
    analysis = pd.read_csv(os.path.join(dirname, 'Daily_Stock_Report\\OBV_Ranked.csv'))
    top10 = analysis.head(10)
    bottom10 = analysis.tail(10)
    Body_of_Email = MIMEText("""\
        Your highest ranked OBV stocks of the day:
        """ + top10.to_string(index=False) + """\
        Your lowest ranked OBV stocks of the day:
        """ + bottom10.to_string(index=False) + """\
        Sincerely,
        Your Computer
    """, 'plain')

    message = MIMEMultipart()
    message["To"] = os.getenv('EMAIL')
    message["From"] = os.getenv('EMAIL')
    message["Subject"] = 'Daily Stock Report'
    message.attach(Body_of_Email)
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(email,password)
    fromaddr = os.getenv('EMAIL')
    toaddrs  = os.getenv('EMAIL')
    server.sendmail(fromaddr,toaddrs,message.as_string())
    server.quit()