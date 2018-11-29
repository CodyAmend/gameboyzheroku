from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACdb4a615b456bcb58f019a5de49166625"
# Your Auth Token from twilio.com/console
auth_token  = "80e4e9e9163cf30489a622ac17c74953"

client = Client(account_sid, auth_token)

TwilioNumber = "+17122013458"

message = client.messages.create(
    to="+14026571789", 
    from_=TwilioNumber,
    body="Hello from Python!")

print(message.sid)