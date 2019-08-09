import re

html = """<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>"""


# 第一步 查找对象整体爬取
pattern = re.compile(r"""<div class="animal">.*?<a title="(.*?)".*?content">(.*?)</p>""",re.S)

r_list = pattern.findall(html)

if r_list:
    print(r_list)

for r in r_list:    # strip()去掉字符串两旁空格,换行,制表格等符号
    print("动物名称",r[0].strip())
    print("动物描述",r[1].strip())