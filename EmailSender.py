import smtplib

to = input("Enter The email of recipent:\n ")

content = input("Enter the content for mail:\n")

def sendmail(to,content):
    server= smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("senderemail@gmail.com", "1234")
    server.sendemail("senderemail@gmail.com", to, connect)
    server.close()


sendmail(to, content)
