"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.core.management import templates
from django.urls import path


import member.views
import question.views

urlpatterns = [
    path('', member.views.main),
    path('admin/', admin.site.urls),
    path('member/', member.views.index),
    path('member/update/<id>', member.views.update),
    path('member/update2', member.views.update2),
    path('member/insert', member.views.insert),
    path('member/insert2', member.views.insert2),
    path('member/delete', member.views.delete),
    path('member/delete2', member.views.delete2),
    path('member/one', member.views.one),
    path('member/one2', member.views.one2),
    path('member/one22/<id>', member.views.one22),
    path('member/all', member.views.all),
    path('member/login', member.views.login),
    path('member/login2', member.views.login2),

    path('question/', question.views.start),
    path('question/update/<id>', question.views.update),
    path('question/update2', question.views.update2),
    path('question/insert', question.views.insert),
    path('question/insert2', question.views.insert2),
    path('question/delete', question.views.delete),
    path('question/delete2', question.views.delete2),
    path('question/one', question.views.one),
    path('question/one2', question.views.one2),
    path('question/one22/<id>', question.views.one22),
    path('question/all', question.views.all),
]