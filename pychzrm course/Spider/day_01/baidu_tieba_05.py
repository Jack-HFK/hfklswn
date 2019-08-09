"""
爬取百度贴吧，赵丽颖吧前三页贴吧内容
"""
import random
from urllib import request
from urllib import parse
import time

from Spider.day_01.User_Agents import user_agents


class BaiduSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"

    # 1.获取响应内容
    def get_html(self,url):
        heades= {"User-Agent": random.choice(user_agents)}
        rep = request.Request(url=url,headers=heades)
        res = request.urlopen(rep)
        html = res.read().decode("utf-8")
        return html

    # 2.提取所需数据
    def parse_html(self):
        pass

    # 3.保存提取的数据
    def write_html(self,filename,html):
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)

    # 4.主函数
    def main(self):
        name = input("请输入贴吧名")
        begin = int(input("请输入起始页"))
        end = int(input("请输入终止页"))
        # 处理请求编码
        param = parse.quote(name)
        for page in range(begin,end+1):
            pn = (page-1)*50
            url = self.url.format(param,pn)
            filename = "{}-第{}页.html".format(name,page)
            # 调用类内函数
            html = self.get_html(url)
            self.write_html(filename,html)
            # 没爬取一个页面随机休眠1到3秒
            time.sleep(random.randint(1,3))

            print("第{}页完成爬取".format(page))

if __name__ == "__main__":
    spider = BaiduSpider()

    spider.main()



