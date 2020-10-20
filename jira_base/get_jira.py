import requests
import json
from configurations.config import *
from resources.resource import *

my_jira=[]

# session manager
session=requests.session()
session.auth=auth=('kaushbabbi@gmail.com','dNz948V9qSjRNqcSxsXTD88A')



retrive_issues_url=get_config()['API']['endpoint']+Resource.attachment





response=session.get(retrive_issues_url)
print(response.status_code)
res=response.json()



attachment_id=res['fields']['attachment'][0]['id']
print('the attachment id is :',attachment_id)


