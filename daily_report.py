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


def send_daily_report(file_to_send):
    # Email server details
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Email content
    from_addr = smtp_username
    to_addr = os.getenv('TO_ADDR')
    subject = 'Daily Report'
    
    # HTML body content
    html_body = """
    <html>
      <head></head>
      <body>
        <p>Bonjour !<br>
           Voici le <b>rapport de vente de pizzas</b> pour aujourd'hui.<br>
           Veuillez trouver le rapport en pièce jointe.
        </p>
      </body>
    </html>
    """
    
    # Setup email
    msg = MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    
    # Attach HTML content
    part2 = MIMEText(html_body, 'html')
    msg.attach(part2)
    
    # Attaching the file
    if file_to_send:
        part = MIMEBase('application', 'octet-stream')
        with open(file_to_send, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(file_to_send))
        msg.attach(part)
    
    # Send email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()
    
    print("Email sent!")

if __name__ == '__main__':
    directory = 'E:\KETRIKA\daily_report\data'  # /chemin/vers/votre/dossier
    file_to_send = find_file_with_today_date(directory)
    if file_to_send:
        send_daily_report(file_to_send)
    else:
        print("No file found for today.")