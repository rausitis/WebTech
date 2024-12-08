# import os
from twilio.rest import Client


# Sid Account and Auth Token here from twilio.com/console
account_sid = 'AC90be66cbe3b45e52343b4a86cb715858'
auth_token = 'a983749f9023ff81fa0c10eb186544eb'
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
        messaging_service_sid='MG9bc6785ee117a6090e16a1736ff889f2',
        body=f"Your verification code is {user_code}.",
        to=f'{phone_number}'
    )

    print(message.sid)
