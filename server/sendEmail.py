import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.starttls()
server.login("kalradivyanshu@gmail.com", "xzkhrenrylkhlqcf")

def send():
    msg = """
    John!"""
    server.sendmail("kalradivyanshu@gmail.com", "kalradivyanshu@gmail.com", msg)
