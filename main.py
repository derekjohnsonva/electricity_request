
import secrets

import venmo_api
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Get my access token
access_token = venmo_api.Client.get_access_token(username=secrets.username,
                                        password=secrets.password)
# Make a client to perform requests
client = venmo_api.Client(access_token=access_token)
# Get the amount to charge
total_monthly_bill = 98.48
bill_per_person = total_monthly_bill/4

# Make the message to send to the user
now = datetime.now()
#   Subtract 1 months from a given datetime object
n = 1
past_date = now - relativedelta(months=n)
date_format_now = '%B, 17'
now_string = now.strftime(date_format_now)
date_format_past = '%B, 16'
past_date_string = past_date.strftime(date_format_past)

message = f'Internet Bill from {past_date_string} to {now_string}'

for user_id in secrets.user_ids.values():
    client.payment.request_money(.01, message, user_id)


client.log_out(access_token=access_token)