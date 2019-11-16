import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("trackerbaggage@gmail.com", "Abcd1234!")


#Send the mail
msg = "BIG CHUNGUS"
server.sendmail("trackerbaggage@gmail.com", "baggagecustomer@gmail.com", msg)