
from twilio.rest import Client

account_sid = "AC87989cfc77f6fb37dcf2bc73f3fcd012" # "AC60ed6d64c268b5ef497e14019513b6d1"
auth_token = "64082b5f60f74b6e59bc11eaa73bdc5a" #99610b508d3729d3e1da665b890c9731"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="this could be fun",
    to="+16129643055",
    from_="+17632519413")
print(message.sid)
