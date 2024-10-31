import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def find_file_with_today_date(directory):
    today = datetime.now().strftime('%Y-%m-%d')
    target_filename = f"pizza_sales_{today}.xlsx"
    for filename in os.listdir(directory):
        if filename == target_filename:
            return os.path.join(directory, filename)
    return None