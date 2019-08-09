import re
import random
import time
from urllib import request
from urllib import parse
import pymysql

from Spider.day_02.User_Agents import user_agents


class FilmSkySpider(object):
    def __init__(self):
        self.url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"

    def get_html(self, url):
        """
        获取html功能函数
        :return:
        """
        headers = {"User-Agent": random.choice(user_agents)}
        rep = request.Request(url=url, headers=headers)
        res = request.urlopen(rep)             # 通过网站查看网页源码，查看网站源码中charset="gb2312"查看其网站使用的解析码
        html = res.read().decode("gb18030")  # 如果像utf-8等主流的编码解析不了，添加第二个参数ignore编码表示解析不了忽略解析
        return html                         # decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码

    def re_func(self, re_dbs, html):
        """
        正则解析功能函数
        :param re_dbs: 正则表达式
        :param html: 一级页面响应内容
        :return:
        """
        pattern = re.compile(re_dbs, re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_page(self, html):
        """
        获取抓取数据中：所需数据：电影名称，电影连接
        :param html: 一级页面响应内容
        :return:
        """
        re_dbs = r"""<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">(.*?)</a>.*?</table>"""
        # 获取一级页面所需的数据
        one_page_list = self.re_func(re_dbs, html)
        item = {}
        for film in one_page_list:
            link = "https://www.dytt8.net"+film[0].strip()  # 二级页面链接地址
            item["name"] = film[1].strip()
            item["download"] = self.parse_two_page(link)
            print(item)
        return item


    def parse_two_page(self,link):
        """

        :param link: 二级页面链接地址
        :return:download
        """
        html = self.get_html(link)   # 获取html功能函数
        re_db = r"""<td style="WORD-WRAP.*?>.*?>(.*?)</a>"""
        two_page_list = self.re_func(re_db,html)  # 正则解析功能函数
        download = two_page_list[0].strip()

        return download

    def main(self):
        """
        主功能函数
        :return:
        """
        for page in range(0,10,):
            url = self.url.format(page)   # 拼接地址
            html = self.get_html(url)     # 获取爬取html内容
            self.parse_page(html)         # 获取所需内容
            # uniform 浮点数

            time.sleep(random.randint(1,3))



if __name__ == "__main__":
    spider = FilmSkySpider()

    spider.main()
