import json
import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

with open('large-file.json') as f:
    data = json.load(f)

start_time = time.time()

for item in data:
    key = item['id']
    value = json.dumps(item)
    r.set(key, value)

end_time = time.time()
print(f"Data upload completed in {end_time - start_time:.2f} seconds.")
