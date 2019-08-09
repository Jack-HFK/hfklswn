"""
separators参数：
指定序列化后的JSON字符串格式，第一个参数指每个键值对之间的连接符号，第二个参数指的是每一个键和键之间的连接符号
"""
import base64
import copy
import hashlib
import hmac
import json
import time


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        header = {'alg': 'HS256', 'typ': 'Jwt'}
        #sort_keys=True 从字典得到的字符串，将字符串序列化的进行排序
        header_json = json.dumps(header, separators=(",", ":"), sort_keys=True)
        # 　生成b64 header
        header_bs = Jwt.b64encode(header_json.encode())

        # 参数中的payload = {"username":"aaa"}
        payload = copy.deepcopy(payload)
        # 添加公有声明 -exp 且值为未来时间戳
        payload["exp"] = int(time.time()) + exp
        payload_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # 签名
        # isinstance判断传入的key类型
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b"." + payload_bs, digestmod="SHA256")
        hm_bs = Jwt.b64encode(hm.digest())
        return header_bs + b"." + payload_bs + b"." + hm_bs

    # b64方法封装函数，静态方法其他类方法不能使用
    @staticmethod
    def b64encode(j_s):
        # 去掉 = 只是维护b64的整体长度，节约因为=造成的流量增加
        # 生成b64并替换生成出来的b64串中的占位符 = ,replace(字符串,替换后的字符串)：替换指定对象
        return base64.urlsafe_b64encode(j_s).replace(b"=", b"")

    @staticmethod
    def b64decode(b64_s):
        rem = len(b64_s) % 4
        if rem > 0:
            b64_s += b"=" * (4 - rem)
        return base64.urlsafe_b64decode(b64_s)

    @staticmethod
    def decode(token, key):
        # 检验两次签名结果
        # 检查exp公有声明的有效性
        # 注意b64 = 号要补全
        # 校验成功　返回 payload　字典对象　失败的话　raise　抛出异常
        header_b, payload_b, sign = token.split(b".")
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_b + b"." + payload_b, digestmod="SHA256")
        if sign != Jwt.b64encode(hm.digest()):
            raise JwtSignEroor("--------sign error")
        # 获取payload
        payload_json = Jwt.b64decode(payload_b)
        payload = json.loads(payload_json.decode())
        # 检验exp是否过期
        exp = payload["exp"]
        now = time.time()
        # 若果 now当前时间 > 过期时间exp
        if now > exp:
            raise JwtExpireError("---- The token is past due")
        return payload


# 自定义异常类
class JwtSignEroor(Exception):

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return "<JwtSignEroor is %s>" % self.error_msg


class JwtExpireError(Exception):

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return "<JwtExpireEroor is %s>" % self.error_msg


if __name__ == "__main__":
    s = Jwt.encode({"username": "hfk"}, "swn", exp=300)
    print(s)


