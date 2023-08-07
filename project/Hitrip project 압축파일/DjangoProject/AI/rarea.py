import surprise
## 고유값(특이값)분해 방법
from surprise import SVD
## SGD(Stochastic 통계적인 Gradient 경사 하강법)
from surprise import Dataset, Reader
from surprise import accuracy
from surprise.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import pandas as pd
import numpy as np


def get_dataframe():
    rating = pd.read_csv('/Users/syshin/Desktop/Himedia/Himedia_project/Django/TripDjango/AI/ratings_trip.csv', index_col=0)
    area = pd.read_csv('/Users/syshin/Desktop/Himedia/Himedia_project/Django/TripDjango/AI/place_trip.csv', index_col=0)
    user = pd.read_csv('/Users/syshin/Desktop/Himedia/Himedia_project/Django/TripDjango/AI/user_trip.csv', index_col=0)
    return user, area, rating


def add_user(user, new):
    new_df = pd.DataFrame(new)

    user = pd.concat([user, new_df], ignore_index=True, axis=0)
    return user


def cal_RMSE(rating):
    algo = SVD()
    reader = Reader(rating_scale=(1,5.0)) # 1단위, 최대값 5
    data = Dataset.load_from_df(rating[['userID', 'area', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.25, random_state=0)
    algo.fit(trainset)
    predictions = algo.test(testset)
    print(accuracy.rmse(predictions))
    return (algo, trainset, testset)


def get_recommendations(userID, algo, user, rating, num_of_ppl=50):
    # model 호출
    # 간단 전처리
    user_df = pd.get_dummies(user)
    col_data = user_df.iloc[:, 1:].columns
    user_matrix = user_df.iloc[:, 1:].to_numpy()
    cosine_sim = cosine_similarity(user_matrix, user_matrix)

    # 선택한 유저의 id로부터 해당 유저의 인덱스를 받아온다.
    userID_to_index = dict(zip(user_df['userID'], user.index))
    idx = userID_to_index[userID]

    # 해당 유저와 모든 유저와의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 유저들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 50개의 유저를 받아온다.
    sim_scores = sim_scores[1:num_of_ppl + 1]

    # 가장 유사한 10개의 유저의 인덱스를 얻는다.
    user_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 10개의 유저의 id을 r_list에 저장.
    rlist = list(user_df['userID'].iloc[user_indices])
    print("가장 유사한", num_of_ppl, "명의 userID:\n", rlist)
    ##비슷한 유저 num_of_ppl명
    similar_users = user_df[user_df['userID'].isin(rlist)]

    similarity = cosine_similarity(similar_users, similar_users)
    print("\n\n")
    print("비슷한 유저", num_of_ppl, "명을 비교한 cosine similarity:\n", similarity)

    ## 비슷한 사람들 20명이 4이상 점수를 준 여행지역
    df_sim = rating[(rating['userID'].isin(rlist)) & (rating['rating'] >= 4)]
    print("\n\n비슷한 사람들", num_of_ppl, "명이 4이상 점수를 준 여행지역:\n", df_sim)

    ## 유저가 여행지역에 줄 점수 예측
    result = [(algo.predict(userID, str(one), verbose=False)) for one in df_sim['area']]
    print("\n\nuserID:", userID, "유저가 여행지역에 줄 점수 예측:")
    for i in result:
        print(i)

    result_est = [pred.est for pred in result]
    result_est = list(set(result_est))
    # print(result_est)

    ## 여행지역중 최대 평점 예측되는 지역 top 5
    top5 = sorted(range(len(result_est)), key=lambda i: result_est[i])[-5:]
    top5.reverse()

    ## top5여행지에 대한 유저 평가 예측
    recommendation = []
    print("\n\ntop5 여행지에 대한 유저 평가 예측:")
    for i in top5:
        print(result[i])
        recommendation.append(result[i][1])

    print("\n\n추천여행지 5곳:")
    print(recommendation)
    return recommendation
