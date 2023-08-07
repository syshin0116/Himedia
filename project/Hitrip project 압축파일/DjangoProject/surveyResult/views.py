from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from AI.rarea import get_dataframe, cal_RMSE, get_recommendations, add_user
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
## http://127.0.0.1:8000/trip/surveyResult/newSurveyResult?answer1=20&answer2=%EB%82%A8%EC%9E%90&answer3=1&answer4=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&answer6=1&answer7=4&answer8=1&answer9=1&answer10=1&answer11=1&answer12=1&answer13=%EB%AF%B8%ED%98%BC&answer14=%EB%8C%80%ED%95%99%EC%83%9D&answer16=10000&answer17=%EC%A4%91%EC%86%8C%EB%8F%84%EC%8B%9C
from DB.connectDB import getSurvey, getSurveyResult, insertSurveyResult, deleteSurveyResult


@method_decorator(csrf_exempt, name='dispatch')
@csrf_exempt
def newSurveyResult(req):

    ## POST로 보낸 form 데이터 받음
    data = req.POST
    print(data)
    ## rarea용 데이터
    new = {
    'sessionID' : data['sessionID'],
    'userID' : [1000001],
    'age' : [int(data['answer1'])],
    'sex' : [data['answer2']],
    'living_area' : [data['answer4']],
    'living_area_size' : [data['answer22']],
    'occupation' : [data['answer20']],
    'family_size' : [int(str(data['answer9']).rstrip('명'))],
    'marry' : [data['answer19']],
    'income_per_year' : [int(str(data['answer21']).rstrip('만원 미만'))],
    }

    ## ractivity용 데이터
    answers = {
    # 'sessionID' : data['sessionID'],
    'age' : data['answer1'],
    'sex' : data['answer2'],
    'month' : data['answer3'],
    'living_area' : data['answer4'],
    'sleepnights' : data['answer5'],
    'accommodation1' : data['answer6'],
    'accommodation2': data['answer7'],
    'accommodation3': data['answer8'],
    'number_of_ppl' : data['answer9'],
    'number_of_children' : data['answer10'],
    'relationship' : data['answer11'],
    'reason1' : data['answer12'],
    'reason2' : data['answer13'],
    'reason3' : data['answer14'],
    'cost_total_trip' : data['answer15'],
    'transportation1' : data['answer16'],
    'transportation2' : data['answer17'],
    'transportation3' : data['answer18'],
    'marry': data['answer19'],
    'occupation' : data['answer20'],
    'income_per_year' : data['answer21'],
    'living_area_size' : data['answer22'],
    }
    answer_list = [*answers.values()]
    answer_db = ""
    for answer in answer_list:
        answer_db += answer + ","
    answer_db = answer_db.rstrip(",")
    new_list = [1000001, '남자', 20, '서울특별시', '중소도시', '대학생', 4, '미혼', 10000]
    userID = 1000001
    sessionID = data['sessionID']
    ## sessionID를 POST로 받아 django session에 저장
    req.session['sessionID'] = sessionID

    print("answer_list>>>>>", answer_list)
    print("answer_db>>>>>>>>", answer_db)
    ractivity = "자연 관광"


    ## Machine Learning 돌려서 값 받음
    user, area, rating = get_dataframe()
    user = add_user(user, new)
    algo, trainset, testset = cal_RMSE(rating)
    rarea = get_recommendations(userID, algo, user, rating, 50)

    ## DB에 넣기 위해 ,로 구분한 string으로 변환
    rarea_db = ""
    for area in rarea:
        rarea_db+=area + ","
    rarea_db = rarea_db.rstrip(",")

    print("recommendation:", rarea)

    surveyList = getSurvey()
    surveyResultList = getSurveyResult(sessionID)
    vo = (sessionID, ractivity, answer_db, rarea_db)
    insertSurveyResult(sessionID, ractivity, answer_db, rarea_db)

    answers = []
    for one in surveyResultList:
        answers.append(str(one[4]).split(','))

    choices = []
    for one in surveyList:
        choices.append(str(one[2]).split(","))

    choices_answers = zip(choices, answers[0])
    surveyList = zip(surveyList, answers[0])
    print("========answers", answers[0])
    print("========choices", choices)

    if sessionID == None or sessionID =="":
        header = "header.jsp"
    else:
        header = "header2.jsp"

    url = "http://localhost:8080/"

    result = {
        'sessionID': sessionID,
        'surveyResultList': surveyResultList,
        'surveyList': surveyList,
        "rarea": rarea,
        "ractivity": ractivity,
        'header': header,
        'url' : url,
    }
    return render(req, 'surveyResult/surveyResult.html', result)

def statistics(req):
    sessionID = req.session['sessionID']
    if sessionID == None or sessionID =="":
        header = "header.jsp"
    else:
        header = "header2.jsp"

    url = "http://localhost:8080/"
    data = {
        'sessionID' : sessionID,
        'header': header,
        'url' : url,
    }
    return render(req, 'surveyResult/statistics.html', data)

def delete(req, idx):
    sessionID = req.session['sessionID']
    result = deleteSurveyResult(idx)
    data = {
        'result': result
    }
    return data

def SurveyResult(req, sessionID):

    surveyList = getSurvey()
    surveyResultList = getSurveyResult(sessionID)
    print("sureyResultList length::::::", len(surveyResultList))
    answers = []
    for one in surveyResultList:
        answers.append(str(one[4]).split(','))

    choices = []
    for one in surveyList:
        choices.append(str(one[2]).split(","))
    choices_answers = zip(choices, answers)
    surveyList = zip(surveyList, answers[0], choices)
    print("========answers", answers[0])
    print("========choices", choices)

    if sessionID == None or sessionID =="":
        header = "header.jsp"
    else:
        header = "header2.jsp"

    ##배포시 바뀔 url
    url = "http://localhost:8080/"
    result = {
        'sessionID': sessionID,
        'surveyResultList': surveyResultList,
        'surveyList': surveyList,
        'header': header,
        'url' : url,
    }
    print("======================================")
    return render(req, 'surveyResult/surveyResult.html', result)
