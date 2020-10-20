import requests
import json
from configurations.config import *
from resources.resource import *

my_jira=[]

# session manager
session=requests.session()
session.auth=auth=('kaushbabbi@gmail.com','dNz948V9qSjRNqcSxsXTD88A')

retrive_issues_url=get_config()['API']['endpoint']+Resource.resource


response=session.get(retrive_issues_url)
print(response.status_code)

res=response.json()
print(res)

print(len(res['issues']))

for i in range(len(res['issues'])):
    my_jira.append(res['issues'][i]['key'])


print(my_jira)

# retriving the logs from the issue











