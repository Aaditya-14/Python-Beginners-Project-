from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials (replace with your own)
account_sid = 'AC9a02660439cf91b54d770df127fdfe27'
auth_token = '6c7fa6cd7508295bb8158e1894f74208'
twilio_number = '+14155238886'  # e.g., '+1234567890'

# User input
name = input("Enter the recipient's name: ")
phone_number = input("Enter the recipient's phone number (with country code, e.g. +1...): ")
send_time_str = input("Enter the time to send the message (24-hour format HH:MM): ")

# Parse time
now = datetime.now()
send_time = datetime.strptime(send_time_str, "%H:%M").replace(
    year=now.year, month=now.month, day=now.day
)

# If time already passed today, send it tomorrow
if send_time < now:
    send_time += timedelta(days=1)

wait_seconds = (send_time - now).total_seconds()
print(f"Scheduled message to be sent in {int(wait_seconds)} seconds...")

# Wait until scheduled time
time.sleep(wait_seconds)

# Compose and send message
client = Client(account_sid, auth_token)
message_body = f"Hello {name}, this is your scheduled message!"

message = client.messages.create(
    body=message_body,
    from_=twilio_number,
    to=phone_number
)

print(f"Message sent to {name} at {send_time.strftime('%H:%M')} ✅")


# 34XLXKTX58HKN8TDUY5ZXUTY