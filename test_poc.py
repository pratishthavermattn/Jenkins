import pandas as pd
import requests

df = pd.read_csv('/home/ubuntu/gocd.csv')
df['job_name'] = df.app_name + '-' + df.env_name
df.to_csv("gocd.csv", index=False)

headers = {
    'Authorization': 'bearer 7608ddb56f81bfe59f505337af6d2d6f9eddba87',
    'Accept': 'application/vnd.go.cd.v1+json',
    'Content-Type': 'application/json',
}

for x,y in zip(df['tag'], df['job_name']):
    data = '{ "environment_variables": [ { "name": "DOCKER_TAG", "secure": false, "value": "'+x+'" } ], "materials": [ { "fingerprint": "ce9a42e6af4ef32a1d5169c7a16ee5b2f398265631ce6144c3f81e4ed7bd8854", "revision": "f91fd59bfcefd6db86254d7ddc243a9bef8f5b65" } ], "update_materials_before_scheduling": true }'
    response = requests.post('http://localhost:8153/go/api/pipelines/'+y+'/schedule', headers=headers, data=data)