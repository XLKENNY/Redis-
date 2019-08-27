# 发布
# -*- coding:utf-8 -*-
# redis_pub.py
# Redis demo
# kenny
 
import redis
 
client = redis.Redis()
channels = ['jay', 'she', 'mj']
 
 
def main():
    print("可以发布到任意一个频道")
    for i in channels:
        print(i)
    ch = input("输入发送的频道>>>")
    while True:
        msg = input("输入发送的信息（q: 退出）>>>")
        if msg == 'q':
            break
        else:
            client.publish(ch, msg)
 
        
if __name__ == "__main__":
    main(
 ———————————————— 
版权声明：本文为CSDN博主「被Python玩的Kenny」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42245157/article/details/100045361
