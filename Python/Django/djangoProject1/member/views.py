from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print('홈페이지 시작화면입니다.')
    #return HttpResponse('내가 시작하는 첫페이지..')
    return render(request, 'member/main.html')


def index1(request):
    print('홈페이지 시작화면입니다.')
    #return HttpResponse('내가 시작하는 첫페이지..')
    return render(request, 'member/index1.html')


def index2(request):
    print('홈페이지 시작화면입니다.')
    #return HttpResponse('내가 시작하는 첫페이지..')
    return HttpResponse(
        "<body bgcolor=yellow>" +
        "<h3>index 2 페이지입니다.</h3><hr color=red>" +
        "<h3>장고 홉페이지 index2 입니다.</h3>" +
        "-<a href= />main page로</a><br>" +
        "-<a href= /member/>member page로</a><br>" +
        "-<a href= /admin/>admin page로</a><br>" +
        "</body>"
    )


def index3(request):
    return render(request, 'member/index3.html')


def start(request):
    print('시작페이지 호출됨.')

    return HttpResponse(
        "-<a href= ../>main page로</a><br>" +
        '내가 리턴하는 내용임'
    )