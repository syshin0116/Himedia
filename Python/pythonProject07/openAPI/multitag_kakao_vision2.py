import sys
import argparse
from tkinter import messagebox

import requests #알트+엔터(cmd+1)
from collections import Counter

#kakao연결 + 신청해놨던 키.
API_url = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'df5989bfdeb66e539382f8c9a0275d74'

def multi_tag(image_url):
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
    return label_kr


if __name__ == '__main__':
    img_list = ['https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_2979480%2F29794808846.1.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220218_84%2F1645126021422HNy7M_JPEG%2F46261856044409370_1633666740.jpg&type=sc960_832',
                'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
                'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fscontent-icn1-1.cdninstagram.com%2Fvp%2F8ef5cd3b518b6234f40193e4649aa59a%2F5D4B2254%2Ft51.2885-15%2Ffr%2Fe15%2Fs1080x1080%2F53267140_125177811879131_3535660168275939536_n.jpg%3F_nc_ht%3Dscontent-icn1-1.cdninstagram.com&type=sc960_832',
                'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/00_06.jpg',
                'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/CLMAO062_02.jpg',
                'https://shopping-phinf.pstatic.net/main_3088161/30881617771.20220211012324.jpg?type=f640',
                'https://shopping-phinf.pstatic.net/main_2948027/29480270215.20211031213251.jpg?type=f640'
                ]
    result_list = []
    for img in img_list:
        result_list += multi_tag(img)

    print("----", result_list)
    count_result = Counter(result_list)
    print(count_result)
    print(count_result.get('사람'))

    print(count_result.most_common(5))#[('사람', 3), ('여러사람', 3), ('남성', 2), ('안경', 1)]

    order_5 = count_result.most_common(5)
    print(order_5[0]) #('사람', 3)
    order_1 = order_5[0]
    print('제일 반도수가 높은 단어는', order_1[0], '빈도수는', order_1[1]) # 제일 반도수가 높은 단어는 사람 빈도수는 3

    tour = ''
    if order_1[0] == '사람':
        tour = '제주도'
    elif order_1[0] == '남성':
        tour = '등산'
    else:
        tour = '놀이공원'
    messagebox.showinfo('추천', '당신에게 ' + tour + '를 추천합니다.')