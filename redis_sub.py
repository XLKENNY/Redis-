# 订阅
# -*- coding:utf-8 -*-
# redis_sub.py
# Redis demo
# kenny
 
import redis
 
client = redis.StrictRedis()
channels = ['jay', 'she', 'mj']
 
# 得到pubsub对象
# 订阅频道
# listen监听
 
 
def subscribe():
    s1 = client.pubsub()
    s1.subscribe(channels)
 
    s2 = client.pubsub()
    s2.subscribe('she')
 
    s3 = client.pubsub()
    s3.subscribe(channels[:2])
 
    show_msg(s1, 's1')
    show_msg(s2, 's2')
    show_msg(s3, 's3')
 
 
def show_msg(sub_obj, sub_name):
    for msg in sub_obj.listen():
        if msg["type"] == "message":
            print(f"{sub_name} get message {msg['data'].decode()} from {msg['channel']}")
 
 
def main():
    subscribe()
if __name__ == "__main__":
    main()
