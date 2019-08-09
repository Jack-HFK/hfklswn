import csv
import re
from urllib import request
from urllib import parse
import time
import random

from Spider.day_01.User_Agents import user_agents


class SpiderFilm(object):
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"

    # 获取爬取的响应内容
    def get_html(self,url):
        # 包装请求
        headers = {"User-Agent":random.choice(user_agents)}
        # 重构User-Agent
        rep = request.Request(url=url,headers=headers)
        # 向网站发起请求并获取响应对象
        res = request.urlopen(rep)
        # 读取接受的响应内容
        html = res.read().decode("utf-8")
        return html


    # 保存爬取的数据
    def write_data(self,file,html):
        with open(file,"w",encoding="utf-8") as f :
            f.write(html)


    # 从保存的数据中，提取需要的的数据,保存在csv文件中
    def get_data(self,html):

        film_name = re.compile(r"""<div class="board-item-content">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>""",re.S)
        film_list = film_name.findall(html)
        with open("热播电影排行榜.csv","a+",encoding="utf-8") as f:
            writer = csv.writer(f)
            list_data = []
            for film in film_list:
                l = [film[0].strip(),film[1].strip(),film[2].strip()]
                list_data.append(l)
            writer.writerows(list_data)

# 主程序
    def main_start(self):
        start = int(input("请输入查看的起始页"))
        stop = int(input("请输入查看的终止页"))
        for page in range(start,stop+1):
            pn = (page-1)*10
            # 拼接地址
            url = self.url.format(pn)
            # 发送请求
            html = self.get_html(url)
            # 保存爬取数据
            file = "电影排行榜:第{}页.html".format(page)
            self.write_data(file,html)
            print("第{}页爬取成功".format(page))
            # 设置爬取时间
            time.sleep(random.randint(1,3))

        # 提取需要的数据
        self.get_data(html)
        print("所需数据成功爬出山 !!")





if __name__ == "__main__":

    sf = SpiderFilm()

    sf.main_start()



