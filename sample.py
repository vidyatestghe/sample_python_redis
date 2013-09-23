import os, redis

redis_port = os.environ.get("SHIPPABLE_REDIS_PORT")
redis_server = redis.Redis("localhost", port = int(redis_port))
redis_server.set("name", "Shippable Redis Demo")
print redis_server.get("name")
