import html
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.login_check import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


@login_check('POST')
def topics(request, author_id):
  #http://127.0.0.1:5000/<username>/topic/release

  if request.method == 'POST':
  # 发布博客
    json_str = request.body
    if not json_str:
      result = {'code':302, 'error': 'Please give me data'}
      return JsonResponse(result)

    json_obj = json.loads(json_str)
    title = json_obj.get('title')
    #带html标签样式的文章内容 [颜色啊,..]
    content = json_obj.get('content')
    #纯文本的文章内容 用于截取简介
    content_text = json_obj.get('content_text')
    limit = json_obj.get('limit')
    category = json_obj.get('category')

    if not title:
      result = {'code':303, 'error': 'Please give me title !!'}
      return JsonResponse(result)
    #防止xss cross site script 攻击
    title = html.escape(title)

    if not content:
      result = {'code':304, 'error': 'Please give me content !!'}
      return JsonResponse(result)

    if not content_text:
      result = {'code':305, 'error': 'Please give me content text !!'}
      return JsonResponse(result)

    if not limit:
      result = {'code':306, 'error': 'Please give me limit !!'}
      return JsonResponse(result)

    if not category:
      result ={'code':307, 'error': 'Please give me category'}
      return JsonResponse(result)

    introduce = content_text[:30]
    if request.user.username != author_id:
      result = {'code':308, 'error': 'Can not touch me !!'}
      return JsonResponse(result)

    #创建数据
    try:
      Topic.objects.create(title=title,limit=limit,content=content,introduce=introduce,category=category,author_id=author_id)
    except Exception as e:
      print(11111111111)
      print(e)
      result = {'code':309, 'error':'Topic is busy'}
      return JsonResponse(result)

    result = {'code':200, 'username': request.user.username}

    return JsonResponse(result)

  elif request.method == 'GET':
    #获取author_id的文章
    #后端地址: /v1/topcis/<username>?category=tec|no-tec
    #前端地址: http://127.0.0.1:5000/<username>/topics
    #文档地址: 第二部分
    # 1, 访问者 visitor
    # 2, 博主/作者 author

    #查找我们的大博主
    authors = UserProfile.objects.filter(username=author_id)
    if not authors:
      result = {'code': 310, 'error':'The user is not existed !'}
      return JsonResponse(result)
    author = authors[0]

    #查找我们的访问者
    visitor = get_user_by_request(request)
    visitor_username = None
    if visitor:
      visitor_username = visitor.username

    #判断是否有查询字符串[category]
    category = request.GET.get('category')
    if category in ['tec', 'no-tec']:

      if visitor_username == author.username:
        # 博主访问自己的博客
        author_topics = Topic.objects.filter(author_id=author.username,category=category)
      else:
        # 陌生的访问者 访问 author 的博客
        author_topics = Topic.objects.filter(author_id=author.username, limit='public',category=category)
    else:
      if visitor_username == author.username:
        #博主访问自己的博客
        author_topics = Topic.objects.filter(author_id=author.username)
      else:
        #陌生的访问者 访问 author 的博客
        author_topics = Topic.objects.filter(author_id=author.username, limit='public')
    #生成返回值
    res = make_topics_res(author, author_topics)
    return JsonResponse(res)

  elif request.method == 'DELETE':
    #删除博客 [真删除]
    #查询字符串中 包含 topic_id ->
    #res返回值 {'code':200}

    topic_id = request.GET.get('topic_id')


    pass



def make_topics_res(author, author_topics):

  res = {'code':200, 'data':{}}
  topics_res = []
  for topic in author_topics:
    d = {}
    d['id'] = topic.id
    d['title'] = topic.title
    d['category'] = topic.category
    d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    d['introduce'] = topic.introduce
    d['author'] = author.nickname
    topics_res.append(d)
  res['data']['topics'] = topics_res
  res['data']['nickname'] = author.nickname

  return res






















































  return JsonResponse({'code':200})
