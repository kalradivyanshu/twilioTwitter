from twilio.rest import Client
from sendEmail import send
# Your Account SID from twilio.com/console
#account_sid = "AC64d28ea27364763954e5ffc27a700572"
account_sid = "AC947dc6070826e83faab4cb6114330982"
# Your Auth Token from twilio.com/console
#auth_token  = "be96f4180e27d745142f9caff8cf820d"
auth_token = "bd54c80f1b2ead04c3efabffe28ba433"
client = Client(account_sid, auth_token)
#from_number = "+13345649396"
from_number = "+15005550006"
def sendMessage(number, from_number = from_number):
    message = client.messages.create(
        to="+"+str(number),
        from_=from_number,
        body="john")
    if message.status == "failed" or message.status == "undelivered":
        raise ValueError("Message failed/undelivered")
    send()
    return message
