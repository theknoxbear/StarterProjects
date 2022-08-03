import os

import pandas as pd

import searchconsole

creds = 'client-secrets.json.json'
1
def authenticate(config='client_secrets.json', token='credentials.json'):
    """Authenticate GSC"""
    if os.path.isfile(token):
        account = searchconsole.authenticate(client_config=config,
                                             credentials=token)
    else:
        account = searchconsole.authenticate(client_config=config,
                                             serialize=token)
    return account

account = authenticate(config=creds)

site = 'https://whenopportunityknox.co.uk/'
months = -5

webproperty = account['https://whenopportunityknox.co.uk/']
report = webproperty.query \
    .range('today', months=months) \
    .dimension('page', 'query') \
    .get()

df = report.to_dataframe()
df.head()

print(report)

