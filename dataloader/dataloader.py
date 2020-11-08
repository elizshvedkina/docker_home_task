import redis
import pandas as pd

r = redis.Redis(host='redis', port=6379)

df = pd.read_csv('file.csv')

redis_dict = dict(zip(df['a'], df['b']))

r.mset(redis_dict)
