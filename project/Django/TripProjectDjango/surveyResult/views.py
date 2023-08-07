from django.shortcuts import render

# Create your views here.
from surveyResult.models import SurveyResult
from survey.models import Survey

def newSurveyResult(req, session, answer0, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13, answer14, answer15, answer16):
    answer_list = [answer0, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13, answer14, answer15, answer16]
    print("session:", session)
    print("answers:", answer_list)


    surveyList = Survey.objects.filter(
        member_idx = session
    )
    surveyResultList = SurveyResult.objects.filter(
        member_idx = session
    )
    result = {
        "answer_list": answer_list,
        "session": session,
        'surveyResultList': surveyResultList,
        'surveyList': surveyList,
    }

    return render(req, 'surveyResult/all.html', result)

def test(req, sessionId, answer0, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13, answer14, answer15, answer16):
    answer_list = [answer0, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, answer11, answer12, answer13, answer14, answer15, answer16]
    print("session:", sessionId)
    print("answers:", answer_list)
    survey_list = Survey.objects.all()
    surveyResult_list = SurveyResult.objects.filter(
        member_idx=sessionId
    )
    print("surveyResult_list:", surveyResult_list)
    print("survey_list:", survey_list)
    result = {
        "answer_list": answer_list,
        "sessionId": sessionId,
        'surveyResult_list': surveyResult_list,
        'survey_list': survey_list,
    }
    return render(req, 'surveyResult/test.html', result)
