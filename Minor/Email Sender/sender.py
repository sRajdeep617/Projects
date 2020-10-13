import smtplib

receiver_email = input("Enter the receiver's email\n")
content = input("Enter the content\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # 2nd parameter is the port number
    server.ehlo()
    server.starttls() # this will start the session
    server.login('sender_email@gmail.com', '12345') # 2nd parameter is the password
    server.sendmail('sender_email@gmail.com', to, content)
    server.close() # this will close the connection

sendEmail(receiver_email, content)