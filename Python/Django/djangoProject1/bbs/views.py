import bbs.models
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def start(request):
	return render(request, 'bbs/index.html')

def update(request):
	return render(request, 'bbs/update.html')

def update2(request):
	data = request.POST
	print(data)

	one = bbs.models.Bbs.objects.filter(
		no=data['no']
	)
	one.update(
		title=data['title']
	)
	return HttpResponse("ok")