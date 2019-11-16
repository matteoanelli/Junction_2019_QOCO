from email.mime.text import MIMEText
import smtplib


sender_email = "trackerbaggage@gmail.com"
receiver_email = "baggagecustomer@gmail.com"
password = "Abcd1234!" #input("Type your password and press enter:")


html = open("message.html")
msg = MIMEText(html.read(), 'html')
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Automatic Weekly Report"

debug = False
if debug:
    print(msg.as_string())
else:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()