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
