import csv
import re
import random
import time
from urllib import request

import pymysql

from Spider.day_02.User_Agents import user_agents


class MaoyanSpider(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        # 计数
        self.num = 0
        # 创建数据库连接，获取对象
        self.db = pymysql.connect("localhost","root","123456","maoyandb",charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()

    def get_html(self, url):
        headers = {"User-Agent": random.choice(user_agents)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        re_str = r"""<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>"""
        pattern = re.compile(re_str, re.S)
        # film_list [("电影名","主演","上映时间")]
        film_list = pattern.findall(html)
        # 直接调用写入模式
        self.write_html(film_list)



    def write_html(self,film_list):
        L = []
        ins = "insert into filmtab values(%s,%s,%s)"
        for film in film_list:
            l = [film[0].strip(),
                 film[1].strip(),
                 film[2].strip()[5:15]
                 ]
            L.append(l)
            self.cursor.executemany(ins,l)
            self.db.commit()

    def main(self):
        for offset in range(0, 31, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.randint(1, 2))

        # 关闭数据库和游标对象
        self.cursor.close()
        self.db.close()
if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
