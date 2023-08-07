import sys
import argparse
import requests #알트+엔터(cmd+1)
from collections import Counter

#kakao연결 + 신청해놨던 키.
API_url = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'df5989bfdeb66e539382f8c9a0275d74'

def tag(image_url):
    header = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    img_data = {'image_url': image_url}
    response = requests.post(API_url, headers=header, data=img_data)
    print(response)
    json_result = response.json()
    print(json_result)
    result = json_result['result']
    print(result)
    label_kr = result['label_kr']
    print(label_kr)
    print(json_result['result']['label_kr'])


if __name__ == '__main__':
    tag('https://search.pstatic.net/common/?src=http%3A%2F%2Fimage.nmv.naver.net%2Fcafe_2022_02_13_438%2F8ff0045e-8c70-11ec-87d4-48df37ae3fca_01.jpg&type=sc960_832')
