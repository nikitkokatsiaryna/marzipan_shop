import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

redis_client.set(name='qqq', value='kostya')

redis_client.close()
