import test_module
import test_module as tm

# from test_module import *
from test_module import say_good_afternoon
from test_module import say_good_evening as ge
from test_module import say_good_morning

test_module.say_good_morning("이재원")
tm.say_good_morning("이재원")
say_good_morning("이재원")
say_good_afternoon("이재원")
ge("이재원")


import travel

china = travel.china.China()

import travel.china as tc
import travel.japan

japan1 = travel.japan.Japan()
china1 = tc.China()

from travel.china import China as ch
from travel.japan import Japan

japan2 = Japan()
china2 = ch()

from travel import Japan

# from travel import Travel

japan3 = Japan()


"""
Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

조건: 모듈 파일명은 byme.py 로 작성

(모듈 사용 예제)

import byme
byme.sign()

(출력 예제)

이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브: http://youtube.com
이메일: nadocoding@gmail.com
"""
