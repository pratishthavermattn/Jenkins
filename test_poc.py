# import pandas as pd
# import requests
# import os

# df = pd.read_csv('gocd.csv')
# df['job_name'] = df.app_name + '-' + df.env_name
# df.to_csv("gocd.csv", index=False)

# headers = {
#     'Authorization': 'bearer 7608ddb56f81bfe59f505337af6d2d6f9eddba87',
#     'Accept': 'application/vnd.go.cd.v1+json',
#     'Content-Type': 'application/json',
# }

# for x,y in zip(df['tag'], df['job_name']):
#     #t = df['job_name'].to_string(index=False)
#     #q = t+'_DOCKER_TAG'
#     #print(q)
#     #tag = os.environ[q]
#     #print(os.getenv(q))
#     data = '{ "environment_variables": [ { "name": "DOCKER_TAG", "secure": false, "value": "'+x+'" } ], "materials": [ { "fingerprint": "3f0eb2f8a536c4ae3ced311c1679ea0a6593e081c2a4d0286e28c9945ff7d8ea", "revision": "da2fc65f42e857ee969a68a6a6d7adef66644326" } ], "update_materials_before_scheduling": true }'
#     response = requests.post('http://localhost:8153/go/api/pipelines/'+y+'/schedule', headers=headers, data=data)

import requests
import json
import pandas as pd
import os

headers = {
    'Authorization': 'bearer 7608ddb56f81bfe59f505337af6d2d6f9eddba87',
    'Accept': 'application/vnd.go.cd.v1+json',
    'Content-Type': 'application/json',
}

df = pd.read_csv('gocd.csv')
df['job_name'] = df.app_name + '-' + df.env_name
df.to_csv("gocd.csv", index=False)

#history
response_history = requests.get('http://localhost:8153/go/api/pipelines/api-service-config-prod/history', headers=headers)

#resp is of type dict
resp_history = response_history.json()

#variables for current and previous revisions
var1 = resp_history['pipelines'][0]['build_cause']['material_revisions'][0]['modifications'][0]['revision']
var2 = resp_history['pipelines'][1]['build_cause']['material_revisions'][0]['modifications'][0]['revision']

for x,y,z in zip(df['tag'], df['job_name'], df['pipeline_group']):
    response_pipeline = requests.get(f"http://localhost:8153/go/api/admin/pipeline_groups/{z}", headers=headers)
    resp_pipeline = response_pipeline.json()
    utf8string = []
    for name in resp_pipeline['pipelines']:
        pipeline_name = name['name']
        utf8string.append(pipeline_name)
        print(utf8string)
        if y in utf8string:
            print("Present")
            data = '{ "environment_variables": [ { "name": "DOCKER_TAG", "secure": false, "value": "'+x+'" } ], "materials": [ { "fingerprint": "3f0eb2f8a536c4ae3ced311c1679ea0a6593e081c2a4d0286e28c9945ff7d8ea", "revision": "ghghghgh" } ], "update_materials_before_scheduling": true }'
            response = requests.post('http://localhost:8153/go/api/pipelines/'+y+'/schedule', headers=headers, data=data)
        else:
            print("Not present")
