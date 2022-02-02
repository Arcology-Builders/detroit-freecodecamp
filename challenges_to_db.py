import json

import redis
r = redis.Redis(host='localhost', port=6379, db=0)

with open('./challenge-names.json') as file:
    json_string = file.read()
    json_obj = json.loads(json_string)
    nodes = json_obj['data']['allChallengeNode']['edges'] 
    count = len(nodes)
    for node in nodes:
        id = node['node']['id']
        title = node['node']['title']
        r.set(id, title)

