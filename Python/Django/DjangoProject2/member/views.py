from django.shortcuts import render

# Create your views here.

def index(request):
    print('홈페이지 시작화면입니다.')
    #return HttpResponse('내가 시작하는 첫페이지..')
    return render(request, 'member/main.html')

def start(request):
    return render(request, 'member/index.html')