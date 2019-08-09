import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.login_check import login_check
from topic.models import Topic


@login_check("POST")
def messages_view(request,topic_id):
    """

    :param request:
    :param topic_id: 文章的id
    :return:
    """

    # POST －－>发布留言及回复
    # http://127.0.0.1:8000/v1/messages/<topic_id>
    # 请求格式 --->{"content":"留言内容","parent_id":1}
    # parent_id如果该字段存在，则证明当前是回复，否则为留言
    # 响应格式 -->{"code":200}
    #注意 post 需要检查token
    if request.method == "POST":
        # 发布留言及回复
        user = request.user  # 获取用户
        json_str = request.body.decode()
        if not json_str:
            result = {"code":402,"error":"Please give me json !!"}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        content = json_obj.get("content")
        parent_message = json_obj.get("parent_id",0)
        if not content:
            result = {"code":403,"error":"Please give me content !!"}
            return JsonResponse(result)
        # 获取topic
        topics = Topic.objects.filter(id=topic_id)
        if not topics:
            # 检查要留言的文章是否存在
            result = {"code":404,"error":"The topic is not existed !!"}
            return  JsonResponse(result)
        topic = topics[0]
        # 创建message
        Message.objects.create(content=content,  # 内容
                               topic=topic,     # 文章外键
                               parent_message=parent_message, #　判断留言或回复
                               publisher=user) # 用户外键　

        result = {"code":200}
        return JsonResponse(result)





