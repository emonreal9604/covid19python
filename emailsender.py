import smtplib
to = input("Enter the email of recipent:\n")
content() = input("Enter the content for mail")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ser')