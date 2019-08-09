from urllib import request
from urllib import parse


# 拼接URL地址
def get_URL(word):
    url = "http://www.baidu.com/?wd={}"
    # 接受的参数进行编码处理
    parse_request = parse.quote(word)
    url = url.format(parse_request)
    return url

# 发送请求，保存到本地文件
def request_url(url,filename):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    # 创建请求对象
    req = request.Request(url=url,headers=headers)

    # 获取响应内容
    res = request.urlopen(req)

    # 提取响应内容
    html = res.read().decode("utf-8")

    # 保存到本地文件
        # 字符编码问题       # windows默认创建文件识别国标语言gb18030： encoding="gb18030"
                           # linux默认创建文件识别国际通用utf-8 : encoding = "utf-8
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)




if __name__ == "__main__":
    word = input("请输入搜索内容：")
    url = get_URL(word)

    filename = word + ".html"

    request_url(url,filename)
