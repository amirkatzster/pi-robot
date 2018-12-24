import redis

class cache:

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def set(self,key,val):
        self.r.set(key,val)

    def get(self,key):
        return self.r.get(key)

