from django.http import HttpResponse
from django.shortcuts import render, redirect
from question.models import Question

# Create your views here.
from question import models


def main(request):
    return render(request, 'main.html')


def start(request):
    return render(request, 'question/index.html')


def update(request, id):
    print("id:", id)
    data = request.POST
    one = Question.objects.get(
        id=id
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
    }
    return render(request, 'question/update.html', result)


def update2(request):
    data = request.POST
    print(data)

    one = Question.objects.filter(
        id=data['id']
    )
    one.update(
        question_text=data['question_text'],
        question_writer=data['question_writer'],
    )
    result = {
        'one': one,
    }
    return redirect('/question/one22/' + data['id'])


def insert(request):
    return render(request, 'question/insert.html')


def insert2(request):
    data = request.POST
    print('서버에서 받은 데이터>>', data)
    one = Question.objects.create(
        question_text=data['question_text'],
        question_writer=data['question_writer'],
    )
    one.save()
    return HttpResponse("질문 입력 처리 페이지")


def delete(request):
    return render(request, 'question/delete.html')


def delete2(request):
    data = request.POST
    one = Question.objects.get(
        id=data['id']
    )
    one.delete()
    return HttpResponse("질문삭제 완료")


def one(request):
    return render(request, 'question/one.html')


def one2(request):
    data = request.POST
    one = Question.objects.get(
        id=data['id']
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
        'test': 100
    }
    ## controller 에서 template으로 값을 넘길때는
    ## dictionary 형태로 만들어서 넘긴다
    ## list, tuple도 가능
    return render(request, 'question/one2.html', result)


## def render(request, template, context): 형태로 되어있음

def one22(request, id):
    data = request.POST
    one = Question.objects.get(
        id=id
    )
    print("DB 검색한 결과: ", one)
    result = {
        'one': one,
        'test': 100
    }
    ## controller 에서 template으로 값을 넘길때는
    ## dictionary 형태로 만들어서 넘긴다
    ## list, tuple도 가능
    return render(request, 'question/one2.html', context=result)


def all(req):
    all = Question.objects.all()
    context = {'all': all}
    return render(req, 'question/all.html', context)
