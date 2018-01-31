from common.common import make_tags


# 포스트 내용 리스트 = 30개
list_content = ['워너원 강다니엘 멋있어'
                , '강다니엘 춤선 최고'
                , '강다니엘 콘서트 축하해'
                , '워너원 강다니엘 완전 섹시해'
                , '노래도 잘하는 울 강다니엘~~'
                , '강다니엘~ 워너블이 응원해요!!'
                , '아놔,, 강다니엘 넘 완벽한거 아님?'
                , '콘서트 대박! 강다니엘 대박!!'
                , '강다니엘보고 왔어요!! 울 녜리~~ 넘 잘생겼어요!!'
                , '워너원 중에서도 강다니엘이 단연 돋보여요ㅋㅋ'
                , '국민픽 강다니엘 센터는 너야너'
                , '강다니엘 옹성우 황민현 짱'
                , '와~~ 강다니엘 실물 캡 짱 잘생김'
                , '태평양 어깨 강다니엘!!'
                , '녤뭉이 울 강다니엘, 멍뭉미 흘러 넘친다 진짜ㅋㅋ'
                , '우리 녤이 오늘도 완벽했어! 역시 강다니엘'
                , '옹녤윙딥환황 모두를 한꺼번에 보다니..ㅎ 그중에서도 단연 강다니엘'
                , '다녤 춤선 너무 아름다워요. 멋있고 섹시한데 귀여워. 강다니엘!!'
                , '아 그 많은 인원중에 강다니엘만 눈에 들어오더라구요ㅠ 강단이 없인 못살아'
                , '스피드, 정확도, 유연함, 표정 하나까지.. 강다니엘의 춤세계에 깊이 빠짐'
                , '저 녤뭉이가 겨우 데뷔 5개월된 신인이란걸 누가 믿을까요. 강다니엘 대단해'
                , '정말 완전 리얼 대박 강다니엘! 녤뭉이 보러 또 올게요~'
                , '대박 짱 귀여워!! 강초딩 강다니엘ㅋㅋ'
                , '강다니엘 다니엘 니엘이 녤 녤뭉이 강초딩 다알렛 강단이'
                , '꽃길만 걸어요 강다니엘! 울 강단이 하고 싶은거 다해♥'
                , '서 있기만 해도 듬직하구낭~~ 어깨 깡패 강다니엘'
                , '강다니엘 어깨 비결은 하루 한 번 팔굽혀펴기 백 번과 윗몸 일으키기.. 또..'
                , '복근 지존 강다니엘! 역시 워너원의 피지컬답네요ㅋㅋ'
                , '워너블과 워너원이 만나는 자리. 콘서트에서 빛나는 강다니엘'
                , '웃음장벽 제로 - 미소가 아름다운 강다니엘^▽^'
                ]

list_content2 = ['트와이스 완전 이뻐'
                , '트와이스 정연 최고'
                , '트와이스 콘서트 축하해'
                , '시그널 노래 좋당~ 트와이스 완전 섹시해'
                , '노래도 잘하는 울 트와이스~~'
                , '트와이스~ 남팬들이 응원해요!!'
                , '아놔,, 트와이스 애들 비율 넘 완벽한거 아님?'
                , '콘서트 대박! 트와이스 대박!!'
                , '트와이스보고 왔어요!! 넘 이뻤어요!!'
                , '트와이스 중에서도 정연이 단연 돋보여요ㅋㅋ'
                , '걸그룹 트와이스,, 울 트둥이들  파이팅'
                , '트와이스 짱'
                , '와~~ 트와이스 실물 캡 짱 이쁨'
                , '학다리 개미허리 트와이스!!'
                , '울 트와이스, 매력 흘러 넘친다 진짜ㅋㅋ'
                , '우리 트둥이 오늘도 완벽했어! 역시 트와이스'
                , '트와이스 모두를 한꺼번에 보다니..ㅎ 그중에서도 단연 나연'
                , '모모 춤선 너무 아름다워요. 섹시한데 귀여워. 트와이스!!'
                , '아 그 많은 인원중에 트와이스만 눈에 들어오더라구요ㅠ 사나 없인 못살아'
                , '갈수록 빠져드는 트와이스의 춤세계!! 다현이와 미나에 깊이 빠짐'
                , '저 트둥이가 겨우 데뷔 2년차된 걸그룹인걸 누가 믿을까요. 트와이스 대단해'
                , '정말 완전 리얼 대박 트와이스! 트둥이 보러 또 올게요~'
                , '대박 짱 귀여워!! 트와이스ㅋㅋ'
                , '트와이스 나연, 정연, 모모, 사나, 지효, 미나, 다현, 채영, 쯔위'
                , '꽃길만 걸어요 트와이스! 울 다현이 하고 싶은거 다해♥'
                , '서 있기만 해도 이쁘구낭~~ 몸매 종결자 트와이스'
                , '트와이스 피부 비결은 1일1팩과 춤으로 다져진 운동, 또..'
                , '여자 복근 지존 트와이스! 역시 걸그룹의 피지컬답네요ㅋㅋ'
                , '트와이스와이 남팬들이 만나는 자리. 콘서트에서 빛나는 트와이스'
                , '미소가 아름다운 트와이스^▽^'
                ]

# 이미지 파일명 리스트 = 40개
list_imagename = ['kdnl_01.jpg', 'kdnl_02.jpg', 'kdnl_03.jpg', 'kdnl_04.jpg', 'kdnl_05.jpg',
                  'kdnl_06.jpg', 'kdnl_07.jpg', 'kdnl_08.jpg', 'kdnl_09.jpg', 'kdnl_10.jpg',
                  'kdnl_11.jpg', 'kdnl_12.jpg', 'kdnl_13.jpg', 'kdnl_14.jpg', 'kdnl_15.jpg',
                  'kdnl_16.jpg', 'kdnl_17.jpg', 'kdnl_18.jpg', 'kdnl_19.jpg', 'kdnl_20.jpg',
                  'kdnl_21.jpg', 'kdnl_22.jpg', 'kdnl_23.jpg', 'kdnl_24.jpg', 'kdnl_25.jpg',
                  'kdnl_26.jpg', 'kdnl_27.jpg', 'kdnl_28.jpg', 'kdnl_29.jpg', 'kdnl_30.jpg',
                  'kdnl_31.jpg', 'kdnl_32.jpg', 'kdnl_33.jpg', 'kdnl_34.jpg', 'kdnl_35.jpg',
                  'kdnl_36.gif', 'kdnl_37.gif', 'kdnl_38.gif', 'kdnl_39.gif', 'kdnl_40.gif'
                  ]

list_imagename2 = ['twc_01.jpg', 'twc_02.jpg', 'twc_03.jpg', 'twc_04.jpg', 'twc_05.jpg',
                  'twc_06.jpg', 'twc_07.jpg', 'twc_08.jpg', 'twc_09.jpg', 'twc_10.jpg'
                  ]


# 포스트 내용에 대한 형태소 분석(해시태그 추출)
def list_tags(dataType):
    return_list = []
    return_str = ""

    for content in list_content:
        return_list.append(make_tags(content))
    # if(dataType=="kang"):
    #     return_str = "#강다니엘"
    # elif(dataType=="twice"):
    #     return_str = "#트와이스"
    return_val = return_list

    return return_val

