import re
import random
import time
from urllib import request

from Spider.day_02.User_Agents import user_agents


class MaoyanSpider(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        # 计数
        self.num = 0

    def get_html(self,url):
        headers = {"User-Agent":random.choice(user_agents)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        # 直接调用解析函数
        self.parse_html(html)
    
    def parse_html(self,html):
        re_str = r"""<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>"""
        pattern = re.compile(re_str,re.S)
        # film_list [("电影名","主演","上映时间")]
        film_list = pattern.findall(html)
        # 直接调用写入模式
        self.write_html(film_list)
    
    def write_html(self,film_list):
        film_dict = {}
        for film in film_list:
            self.num += 1
            film_dict["number"] = self.num
            film_dict["name"] = film[0].strip()
            film_dict["star"] = film[1].strip()
            film_dict["time"] = film[2].strip()[5:15]
            print(film_dict)
    
    def main(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.randint(1,2))



    
if __name__=="__main__":
    
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f"%(end-start))
    
    