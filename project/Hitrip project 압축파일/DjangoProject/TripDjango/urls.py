"""TripDjango URL Configuration

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
from django.urls import path

import surveyResult.views

# string = ''
# for i in range(1, 18):
#     string += '/<answer'+str(i)+'>'
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trip/surveyResult/SurveyResult/<sessionID>', surveyResult.views.SurveyResult),
    path('trip/surveyResult/newSurveyResult', surveyResult.views.newSurveyResult),
    path('trip/surveyResult/statistics', surveyResult.views.statistics),
    path('trip/surveyResult/surveyResultDelete/<idx>', surveyResult.views.delete),
]
