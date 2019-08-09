
from django.http import HttpResponse
from django.shortcuts import render



def shebao_view(request):
    if request.method == 'GET':
        return render(request, 'shebao.html')
    elif request.method == 'POST':
        base = int(request.POST.get('base', 0))
        yl_gr = base * 0.08  # 个人社保
        yl_gs = base * 0.19  # 公司社保
        is_city = request.POST.get('is_city', 0)
        if is_city == "1":
            sy_gr = base * 0.002  # 个人失业
        else:
            sy_gr = 0  # 个人失业(农村户口)
        sy_gs = base * 0.008  # 公司失业
        gs_gr = 0
        gs_gs = base * 0.005  # 公司工伤
        shengyu_gr = 0
        shengyu_gs = base * 0.008  # 公司生育
        yiliao_gr = base * 0.02 + 3
        yiliao_gs = base * 0.1  # 公司医疗
        gjj_gr = base * 0.12
        gjj_gs = base * 0.12  # 公司公积金

        # 个人的小计
        gr = yl_gr + sy_gr + gs_gr + shengyu_gr + yiliao_gr + gjj_gr
        # 公司的小计
        gs = yl_gs + sy_gs + gs_gs + shengyu_gs + yiliao_gs + gjj_gs
        total = gr + gs
        return render(request, 'shebao.html', locals())


