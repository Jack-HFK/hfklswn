from django.http import HttpResponse


def test_view(request):
    return HttpResponse("测试链接效果")