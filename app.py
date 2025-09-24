import resms

resms.api_key = "your_api_key_here"

response = resms.sms.send(
    to="+33787195650",
    message="Welcome to ReSMS!"
)

print(response)