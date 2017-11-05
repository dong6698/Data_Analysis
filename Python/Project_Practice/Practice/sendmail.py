import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(username, password, receiver, subject, mailcontents):
    gmail_user = username
    gmail_pwd = password
    FROM = username.split('@', 1)[0]
    TO = receiver
    SUBJECT = subject
    TEXT = mailcontents

# Build the message of Email
    message = MIMEText(TEXT)
    message['From'] = Header(FROM)
    message['To'] = Header(TO)
    message['Subject'] = Header(SUBJECT)
    print(message)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message.as_string())
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

user_name = str(input("Please input your user name of google.\n"))
password = str(input("Please input your password.\n"))
receiver = str(input("Plese input the address TO: \n"))
subject = str(input("Subject is : \n"))
contents = str(input("Contents: \n"))

# user_name = 'dongchen6698@gmail.com'
# password = 'dong1990403'
# receiver = 'chendong6698@gmail.com'
# subject = 'just test'
# contents = 'nothing'

send_email(user_name, password, receiver, subject, contents)