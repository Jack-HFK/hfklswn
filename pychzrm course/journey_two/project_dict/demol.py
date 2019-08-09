import getpass  # 隐藏输入
import hashlib  # 转换加密

# 输入隐藏  只支持重点输入密码
pwd = getpass.getpass("隐藏输入：")

# hash对象
# hash = hashlib.md5()   # 生成对象

# 算法加盐
hash = hashlib.md5("*#06l_".encode())   # 生成对象
hash.update(pwd.encode())   # 算法加密
pwd = hash.hexdigest()    # 提取加密密码
