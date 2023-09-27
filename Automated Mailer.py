import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

    
def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    text = MIMEText(body, 'plain')
    msg.attach(text)
    

    msg['Subject'] = subject
    msg['From'] = 'EMAIL ADDRESS HERE'
    msg['To'] = to_email


    # Attach Resume.pdf
    with open("Resume.pdf", "rb") as file:
        attach_file = MIMEApplication(file.read(), _subtype="pdf")
        attach_file.add_header('Content-Disposition', 'attachment', filename="Resume.pdf")
        msg.attach(attach_file)


    # Establish a connection to the Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    

    # Login to your Gmail account
    password = "PASSWORD HERE"  # Remember to use an application-specific password if you have 2-step verification enabled
    server.login('EMAIL ADDRESS HERE', password)  
    

    server.send_message(msg)  # Send the email
    server.quit()


def read_mail_body():
    with open("mailBody.txt", "r") as file:
        return file.read()


# Subject of the email
email_subject = "EMAIL BODY HERE"


# Read email addresses from the file and send emails
with open('emailAddresses.txt', 'r') as file:
    email_body = read_mail_body()
    for line in file:
        recipient = line.strip()
        send_email(email_subject, email_body, recipient)
