import sys
import argparse
from tkinter import messagebox

import requests  # 알트+엔터(cmd+1)
from collections import Counter

# kakao연결 + 신청해놨던 키.
API_url = 'https://dapi.kakao.com/v2/vision/product/detect'
MYAPP_KEY = 'df5989bfdeb66e539382f8c9a0275d74'


# curl -v -X POST "https://dapi.kakao.com/v2/vision/product/detect" \
#     -H "Content-Type: application/x-www-form-urlencoded" \
#     -H "Authorization: KakaoAK ${REST_API_KEY}" \
#     --data-urlencode "image_url=https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/06.jpg"

def recog_product(image_url):
    product = []
    product_list = []
    header = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    img_data = {'image_url': image_url}
    response = requests.post(API_url, headers=header, data=img_data)
    print(response)
    json_result = response.json()
    print(json_result)
    result = json_result['result']
    print("result================", result)
    photo = result['objects']
    print("photo============", photo)
    for i in photo:
        print("i======", i)
        product_list.append(i.get('class'))

    print("product_list===", product_list)

    return product_list


if __name__ == '__main__':
    img_list = [
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_2979480%2F29794808846.1.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220218_84%2F1645126021422HNy7M_JPEG%2F46261856044409370_1633666740.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
        'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fscontent-icn1-1.cdninstagram.com%2Fvp%2F8ef5cd3b518b6234f40193e4649aa59a%2F5D4B2254%2Ft51.2885-15%2Ffr%2Fe15%2Fs1080x1080%2F53267140_125177811879131_3535660168275939536_n.jpg%3F_nc_ht%3Dscontent-icn1-1.cdninstagram.com&type=sc960_832',
        'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/00_06.jpg',
        'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/CLMAO062_02.jpg',
        'https://shopping-phinf.pstatic.net/main_3088161/30881617771.20220211012324.jpg?type=f640',
        'https://shopping-phinf.pstatic.net/main_2948027/29480270215.20211031213251.jpg?type=f640',
        'https://static.coupangcdn.com/image/vendor_inventory/c2ba/ec493de1c1ebd60e7c2914908433ce638b6e01cc9a0091f444b59daba2ee.jpg',
        'https://contents.lotteon.com/itemimage/LO/14/30/64/30/56/_1/43/06/43/05/7/LO1430643056_1430643057_1.jpg/dims/optimize/dims/resizemc/400x400',
        'http://openimage.interpark.com/goods_image_big/7/2/7/0/7068487270e_l.jpg',
        'http://openimage.interpark.com/goods_image_big/1/0/7/1/7455671071_l.jpg',
        'http://thumbnail.10x10.co.kr/webimage/image/basic600/367/B003676360.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false',
        'https://i.pinimg.com/550x/12/30/45/123045ca40e5aae6b4b5eb9d4fc163da.jpg',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210129_219%2F1611885704670Vh774_JPEG%2F155276_1.jpg&type=sc960_832',
        'https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FA5102502258.jpg%3Fut%3D20210413222430',
        'https://i.pinimg.com/474x/9d/4e/40/9d4e40244932b1e19c794f07fcb4c7a6.jpg'
    ]
    result_list = []
    for img in img_list:
        result_list += recog_product(img)

    print("----", result_list)
    count_result = Counter(result_list)
    print(count_result)
    print(count_result.get('사람'))

    print(count_result.most_common(5))
    # [('사람', 3), ('여러사람', 3), ('남성', 2), ('안경', 1)]

    order_5 = count_result.most_common(5)
    print(order_5[0])  # ('사람', 3)
    order_1 = order_5[0]
    print('제일 반도수가 높은 단어는', order_1[0], '빈도수는', order_1[1])  # 제일 반도수가 높은 단어는 사람 빈도수는 3

    tour = ''
    if order_1[0] == '사람':
        tour = '제주도'
    elif order_1[0] == '남성':
        tour = '등산'
    else:
        tour = '놀이공원'

