import json
import redis
import time
from redis.cluster import RedisCluster 

r = RedisCluster(host='localhost', port=7000)

with open('../dataset/large-file.json') as f:
    data = json.load(f)

start_time = time.time()

for item in data:
    key = item['id']
    value = json.dumps(item)
    r.set(key, value)

end_time = time.time()
print(f"Data upload completed in {end_time - start_time:.2f} seconds.")
