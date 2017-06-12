# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Send Text

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "****"
# Your Auth Token from twilio.com/console
auth_token  = "****"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9095554411", 
    from_="+19095554411",
    body="Hello from Python!")

print(message.sid)
