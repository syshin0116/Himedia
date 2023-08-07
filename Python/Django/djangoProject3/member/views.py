from django.http import HttpResponse
from django.shortcuts import render, redirect
from member.models import Test

# Create your views here.
from member import models


def main(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'member/index.html')


def update(request, id):
    print("id:",id)
    data = request.POST
    one = Test.objects.get(
        id=id
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
    }
    return render(request, 'member/update.html', result)


def update2(request):
    data = request.POST
    print(data)

    one = Test.objects.filter(
        id=data['id']
    )
    one.update(
        name=data['name'],
        tel=data['tel'],
        addr=data['addr']
    )
    result = {
        'one': one,
    }
    return redirect('/member/one22/' + data['id'])

def insert(request):
    return render(request, 'member/insert.html')


def insert2(request):
    data = request.POST
    print('서버에서 받은 데이터>>', data)
    print(data['name'], data['tel'], data['addr'])
    one = Test.objects.create(
        name = data['name'],
        tel = data['tel'],
        addr = data['addr']
    )
    one.save()
    return HttpResponse("회원 가입 처리 페이지")

def delete(request):
    return render(request, 'member/delete.html')


def delete2(request):
    data = request.POST
    one = Test.objects.get(
        id = data['id']
    )
    one.delete()
    return HttpResponse("회원삭제 완료")


def one(request):
    return render(request, 'member/one.html')

def one2(request):
    data = request.POST
    one = Test.objects.get(
        id = data['id']
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
        'test': 100
    }
    ## controller 에서 template으로 값을 넘길때는
    ## dictionary 형태로 만들어서 넘긴다
    ## list, tuple도 가능
    return render(request, 'member/one2.html', result)

## def render(request, template, context): 형태로 되어있음

def one22(request, id):
    data = request.POST
    one = Test.objects.get(
        id = id
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
        'test': 100
    }
    ## controller 에서 template으로 값을 넘길때는
    ## dictionary 형태로 만들어서 넘긴다
    ## list, tuple도 가능
    return render(request, 'member/one2.html', context = result)

def all(req):
    all = Test.objects.all()
    context = {'all' : all}
    return render(req, 'member/all.html', context)

def login(req):
    return render(req, 'member/login.html')

def login2(req):
    one = Test.objects.get(id=req.POST['id'])
    print('db검색한 결과: ', one)
    if one != None:
        result = '로그인 성공'
        req.session['logid'] = req.POST['id']
    else:
        result = '로그인 실패'
    print(result)
    # controller에서 template으로 값을 넘길때는
    # dictionary를 만들어 전달한다.
    return redirect('/member/')