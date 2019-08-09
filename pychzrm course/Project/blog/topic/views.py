"""
    file :topic/views.py
"""
import html
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.login_check import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


@login_check("POST","DELETE")
def topics_view(request, author_id):
    """

    :param request:
    :param author_id: 字典对应的值为用户名
    :return:
    """
    # print(author_id)
    # http://127.0.0.1:5000/<username>/topic/release
    #　发表博客
    if request.method == "POST":
        # 接收用户json数据，字节串需转换为字符串
        json_str = request.body
        if not json_str:
            result = {"code": 302, "error": "Please give me your json"}
            return JsonResponse(result)
        # json转换
        json_obj = json.loads(json_str)
        title = json_obj.get("title")
        category = json_obj.get("category")
        limit = json_obj.get("limit")
        # 带html标签样式的文章内容
        content = json_obj.get("content")
        # 纯文本的文章内容　用于截取简介
        content_text = json_obj.get("content_text")
        if not title:
            result = {"code": 303, "error": "Please give me title !!"}
            return JsonResponse(result)
        #防止 xss 跨站脚本攻击 cross site script
        title = html.escape(title)
        if not content:
            result = {"code": 304, "error": "Please give me content !!"}
            return JsonResponse(result)
        if not content_text:
            result = {"code": 305, "error": "Please give me content text !!"}
            return JsonResponse(result)
        if not limit:
            result = {"code": 306, "error": "Please give me content limit !!"}
            return JsonResponse(result)
        if not category:
            result = {"code": 307, "error": "Please give me content category !!"}
            return JsonResponse(result)

        introduce = content_text[:30]
        # 判断装饰器的username于传过来的author_id是否是同一个人
        if request.user.username != author_id:
            result = {"code": 308, "error": "Can not touch me !!"}
            return JsonResponse(result)
        # 创建数据
        try:
            Topic.objects.create(title=title,
                                 content=content,
                                 introduce=introduce,
                                 limit=limit,
                                 category=category,
                                 author_id=author_id)
        except Exception as e:
            result = {"code": 309, "error": "Sorry! Topic is rested !!"}
            return JsonResponse(result)
        result = {"code": 200, "username": request.user.username}
        return JsonResponse(result)
    # 获取数据
    elif request.method == "GET":
        # 获取author_id的文章
        # 后端地址　/v1/topcis/<username>?category=[tec|no-tec
        # 前端地址　http://127.0.0.1:5000/<username>/topics
        
        # 查找博客主人/作者　author
        authors = UserProfile.objects.filter(username=author_id)
        if not authors:
            result = {"code": 310, "error": "The user is not existed !!"}
            return JsonResponse(result)
        author = authors[0]
        
        # 查找访问者 visitor
        visitor = get_user_by_request(request)
        visitor_username = None
        if visitor:
            visitor_username = visitor.username

        #　获取t_id
        t_id = request.GET.get("t_id")
        if t_id:
            # 查询指定文章数据
            t_id = int(t_id)
            # 是否为博主访问自己博客
            is_self = False
            if visitor_username == author_id:
                # 博主访问自己
                is_self=True
                try:
                    author_topic = Topic.objects.get(id=t_id)
                except Exception as e:
                    result = {"code":311,"error":"No topic"}
                    return JsonResponse(result)
            else:
                # 陌生人访问博主的博客
                try:
                    author_topic = Topic.objects.get(id=t_id,limit="public")
                except Exception as e:
                    result = {"code":312,"error":"No topic !"}
                    return JsonResponse(result)

            res = make_topic_res(author,author_topic,is_self)
            # http://127.0.0.1:8000/hfktopics/detail
            return JsonResponse(res)
        else:
            # 没有t_id查询用户所有文章
            # 判断是否有查询字符串[category]
            category = request.GET.get("category")
            if category in ["tec", "no-tec"]:
                # 比较是否为博主自身访问
                if visitor_username == author.username:
                    author_topics = Topic.objects.filter(author_id=author.username,
                                                         category=category)
                else:
                    # 比较失败，判断为其他博客访问 author 的博客
                    author_topics = Topic.objects.filter(author_id=author.username,
                                                         limit="public",
                                                         category=category)
            else:
                # 比较是否为博主自身访问
                if visitor_username == author.username:
                    author_topics = Topic.objects.filter(author_id=author.username)
                else:
                    # 比较失败，判断为其他博客访问 author 的博客
                    author_topics = Topic.objects.filter(author_id=author.username,
                                                         limit="public")
        # 生成返回值
        res = make_topics_res(author, author_topics)
        return JsonResponse(res)

    elif request.method == "DELETE":
        # 删除博客
        # 查询字符串中 包含 topic_id
        # res 返回值 {"code":200}
        # 判断token 获取username
        get_user_by_request(request)
        t_id = request.GET.get("topic_id")
        if not t_id:
            result = {"code":401,"error":"This t_id is Empty !"}
            return JsonResponse(result)
        int(t_id)
        print(t_id)
        if not author_id:
            result={"code":403,"error":"The username is unlisted word !!"}
            return JsonResponse(result)
        if request.user.username != author_id:
            result = {"code":404,"error":"This author_id is not self !"}
            return JsonResponse(result)
        # 获取数据库中的文章内容
        article = Topic.objects.get(id=t_id)
        print(article)
        if not article:
            result = {"code":405,"error":"Topic is Empty !!"}
            return JsonResponse(result)
        article.delete()
        result = {"code":200}
        print(result)
        return JsonResponse(result)
            





def make_topics_res(author, author_topics):
    res = {"code": 200, "data": {}}
    topics_res = []
    for topic in author_topics:
        d = {}
        d["id"] = topic.id
        d["title"] = topic.title
        d["category"] = topic.category
        d["created_time"] = topic.created_time.strftime("Y%-%m-%d %H:%M:%S")
        d["introduce"] = topic.introduce
        d["author"] = author.nickname
        topics_res.append(d)
    res["data"]["topics"] = topics_res
    res["data"]["nickname"] = author.nickname
    return res

def make_topic_res(author,author_topic,is_self):
    """
    生成 topic　详情数据
    :param author: 用户
    :param author_topic:　当前文章
    :param is_self: 是否为本人访问自己博客  True /false
    :return:
    """
    if is_self:
        # 博主访问自己博客
        # 取出ID大于当前博客ID的数据的第一个 <---当前文章下一篇
        next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                          author=author).first()
        # 取出ID小于当前博客ID的数据的最后一个 <---当前文章上一篇
        last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                          author=author).last()
    else:
        # 陌生人访问当前博客
        next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                          author=author,limit="public").first()
        # 取出ID小于当前博客ID的数据的最后一个 <---当前文章上一篇
        last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                          author=author,
                                          limit="public").last()
    # 下一篇
    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None
    # 上一篇
    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None
    result = {"code":200,"data":{}}
    result["data"]["nickname"] = author.nickname
    result["data"]["title"] = author_topic.title
    result["data"]["category"] = author_topic.category
    result["data"]["created_time"] = author_topic.created_time.strftime("Y%-%m-%d %H:%M:%S")
    result["data"]["content"] = author_topic.content
    result["data"]["introduce"] = author_topic.introduce
    result["data"]["author"] = author.nickname
    result["data"]["next_id"] = next_id
    result["data"]["next_title"] = next_title
    result["data"]["last_id"] = last_id
    result["data"]["last_title"] = last_title
    # 留言和回复数据
    # 获取所有的留言和回复
    all_messages = Message.objects.filter(topic=author_topic).order_by("-created_time")
    # {1:[{"回复"},{"回复"}]}
    # [{"留言"},{"留言"}]
    msg_dict = {}
    msg_list = []
    m_count = 0
    for all_message in all_messages:
        m_count += 1
        if all_message.parent_message:
            # 回复
            if all_message.parent_message in msg_dict:
                msg_dict[all_message.parent_message].append({"msg_id":all_message.id,
                                                             "publisher":all_message.publisher.nickname,
                                                             "publisher_avatar":str(all_message.publisher.avatar),
                                                             "content":all_message.content,
                                                             "created_time":all_message.created_time.strftime("%Y-%m-%d %H:%M:%S")})
            else:
                msg_dict[all_message.parent_message] = []
                msg_dict[all_message.parent_message].append({"msg_id":all_message.id,
                                                             "publisher":all_message.publisher.nickname,
                                                             "publisher_avatar":str(all_message.publisher.avatar),
                                                             "content":all_message.content,
                                                             "created_time":all_message.created_time.strftime("%Y-%m-%d %H:%M:%S")})
        else:
            # 留言
            msg_list.append({"id":all_message.id,"content":all_message.content,
                             "publisher":all_message.publisher.nickname,
                             "publisher_avatar":str(all_message.publisher.avatar),
                             "created_time":all_message.created_time.strftime("%Y-%m-%d %H:%M:%S"),
                             "reply":[]})
    # 关联留言和对应的回复
    # msg_list [{"留言相关的信息","reply" : []}]
    for m in msg_list:
        if m["id"] in msg_dict:
            # 证明当前留言有回复信息
            m["reply"] = msg_dict[m["id"]]

    result["data"]["messages"] = msg_list
    result["data"]["messages_count"] = m_count
    
    return result



