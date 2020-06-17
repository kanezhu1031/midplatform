# @Author  : kane.zhu
# @Time    : 2020/6/15 19:13
# @Software: PyCharm
import redis
from common import baseconfig
redishost= baseconfig.getconfig()['redisAddr']
redisPort= int(baseconfig.getconfig()['redisPort'])

redisPass= baseconfig.getconfig()['redisPass']
r = redis.Redis(host=redishost, port=redisPort, decode_responses=True, password=redisPass)
def keyset(**tokenserials):
    print(tokenserials)


    r.set(tokenserials['k'],tokenserials['v'],tokenserials['expire'])

def keyExists(key):
    """
    :param key: 登陆后得到的KEY
    :return: int 0 不存在 1 存在
    """
    res= r.exists(key)
    return res






