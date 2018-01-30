from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC64d28ea27364763954e5ffc27a700572"
# Your Auth Token from twilio.com/console
auth_token  = "be96f4180e27d745142f9caff8cf820d"

client = Client(account_sid, auth_token)

def sendMessage(number):
    message = client.messages.create(
        to="+"+str(number),
        from_="+13345649396",
        body="john")

    return message
