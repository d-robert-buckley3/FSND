# Udacity Full Stack Web Developer nanodegree
# Programming Fundamentals
# Use Classes
# Send Text

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC36d34cd47bc49335a2a5e51cc4d1dd66"
# Your Auth Token from twilio.com/console
auth_token  = "8ece0fe844de1ce2b13b22b94ace7d7c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19513108356", 
    from_="+19095527479",
    body="Hello from Python!")

print(message.sid)