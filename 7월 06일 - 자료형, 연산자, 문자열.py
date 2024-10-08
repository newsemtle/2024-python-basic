# 2. 자료형 - 숫자, 문자열, boolean,

# 2-1. 숫자 자료형

# print라는 함수를 써서 5를 출력해보자!, 파일 저장(Ctrl + s), 프로그램 실행(디버깅- Ctrl + F5)

print(5)
print(-10)
print(3.14)
print(5 + 3)  # 덧셈
print(5 * 3)  # 곱셈
print(3 * (3 + 1))  # 복잡한 연산


# 2-2. 문자열 자료형

print("이건호")
print("semtle")
print("바보바보바보바보")
print("바보" * 9)
print("바보 * 9")


# boolean 자료형 - True, False, not
# boolean은 참과 거짓에 대한 것.

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)


# 2-3. 변수
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

# 이렇게만 적어도 상관이 없다. 다만, 단어 하나가 바뀐다면 모든 코드의 단어를 손수 고쳐야 한다.
# 그걸 편하게 하기 위해서 변수를 쓴다. 변수는 어떤 것을 저장하는 공간이다.

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
# 문자열 사이에 정수 자료형이 들어갔으니, 변환해줌
print(name + "는 어른일까요?" + str(is_adult))
# 마찬가지. boolean을 str로 변환해줌

# 이렇게 하면 저 코드를 복사 붙여넣기 하여 변수에 넣는 것만 바꿔주면 됨!
# 중간에 변수명을 바꿔주면 그 시점부터는 바뀐 변수가 들어감


print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))


# 플러스 말고 쉼표로도 할 수 있음, 쉼표일 때는 자료형 변환을 안 해도 가능.
print("우리집 ", animal, "의 이름은 ", name, "에요")
print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아해요")
print(name, "는 어른일까요?", is_adult)

# 2-*. 자료형 변환


# 2-5. 주석 : 코드에 적혀 있지만 실행이 안 되는 문장. 컴파일러가 읽지 못함.
# #, ''' ''', Ctrl + /
# 추가 설명이나 기록, 이 코드가 무슨 의미인지 메모해둘 때 유용함.
# 여러 문장을 한 번에 하고 싶을 때, 작은 따옴표 세 개로 묶거나, Ctrl + /로 할 수 있음. 해지도 가능.


# 3-1. 연산자
print(1 + 1)  # 덧셈
print(3 - 2)  # 뺄셈
print(5 * 2)  # 곱셈
print(6 / 3)  # 나눗셈

print(2**3)  # 제곱
print(5 % 3)  # 나머지
print(5 // 3)  # 몫

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)  # not 표현
print(not (1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 < 7)

# 3-2. 간단한 수식

print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)

# 변수에 숫자 더하기
number = number + 2
print(number)

# 그걸 간략하게 하기
number += 2
print(number)
number *= 2
print(number)
number -= 2
print(number)
number /= 2
print(number)
number %= 2
print(number)

# 3-3. 숫자처리함수 : 절댓값, 제곱, 최댓값, 최솟값, 반올림

print(abs(-5))
print(pow(4, 2))  # 4^2
print(max(5, 12))
print(min(5, 12))
print(round(3.14))

# math 모듈 불러오기.
from math import *

print(floor(4.99))  # 내림
print(ceil(3.14))  # 올림
print(sqrt(16))  # 제곱근

# 다른 방법
import math

print(math.sqrt(16))

# 모듈은 클래스와 함수로 되어 있음.
# import 모듈, from 모듈 import 이름
# 보통 import는 모든 것, from은 모듈 안의 특정 함수만 사용하고 싶을 때 사용
# import로 모듈을 호출하면 모듈명.함수명(), from으로 모듈 호출하면 함수명()


# 3-4. 랜덤함수

from random import *

print(random())  # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 이상 10 미만의 임의의 정수 값 생성
print(int(random() * 10) + 1)  # 1이상 10 이하(11미만)의 임의의 정수 값 생성

print(int(random() * 45 + 1))  # 1이상 46미만의 임의의 정수 값 생성

print(randrange(1, 46))  # 1이상 46미만의 임의의 정수 값 생성
print(randint(1, 45))  # 1이상 45이하의 임의의 정수값 생성


# 4-1. 문자열 : 문자들의 집합

sentence1 = "나는 소년입니다"
print(sentence1)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 세따옴표 앞에 변수가 있다면 여러 줄에 걸친 문자열로, 없으면 주석으로 인식됨


# 4-2. 슬라이싱
# 데이터를 원하는 만큼 잘라서 가져두는 것
# 여러 문자의 집합으로 구성된 문자열 등은 n번쨰 인덱스에 있는 문자 하나만을 가져올 수 있음
# 이때 사용하는 게 대괄호

jumin = "990120-1234567"
print("성별:" + jumin[7])

# 인덱스값은 0부터 시작됨.

print("연:" + jumin[0:2])
print("월:" + jumin[2:4])
print("일:" + jumin[4:6])

# 변수명[:인덱스] -> 처음부터 인덱스 직전까지 슬라이싱
# 변수명[인덱스:] -> 인덱스부터 끝까지 슬라이싱
# 변수명[:] -> 처음부터 끝까지 슬라이싱

print("생년월일:" + jumin[:6])
print("뒤 7자리:" + jumin[7:])

print("뒤 7자리(뒤에서부터):" + jumin[-7:])


# 4-3. 문자열처리함수

"""
lower : 소문자로 변환
upper : 대문자로 변환
isupper : 대문자인지 확인
islower : 소문자인지 확인
replace : 문자열 바꾸기 
index : 찾으려는 문자열의 인덱스(없으면 에러)
find : 찾으려는 문자열의 인덱스(없으면 -1)
count : 문자열이 나온 횟수
"""

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 처음으로 발견된 n의 인덱스
print(index)
index = python.index("n", index + 1)  # 6번째 인덱스 이후에 처음으로 발견된 n의 인덱스
print(index)

find = python.find("n")
print(find)
find = python.find("n", find + 1)
print(find)

# print(python.index("Java")) #없으면 에러 발생하여 프로그램 종료
print(python.find("Java"))  # 없으면 -1 반환(출력)하며 프로그램 계속 수행

print(python.count("n"))  # 찾으려는 문자열이 총 몇 번 사용되었는지


# 4-4. 문자열포맷
print("a" + "b")  # ab
print("a", "b")  # a b

# 방법 1: %
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)  # %s로도 정수값 표현 가능

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2: .format()
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3: {이름}.format

print("나는 {age}살이며, {color}새글 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}새글 좋아해요.".format(color="빨간", age=20))

# 방법 4: f-string

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


# 4-5. 탈출문자

print("백문이 불여일견 백견이 불여일타")

# print("백문이 불여일견
#      백문이 불여일타")

print("백문이 불여일견\n백견이 불여일타")

print("저는 '이건호'입니다.")
print('저는 "이건호"입니다.')

print('저는 "이건호"입니다.')
print("저는 '이건호'입니다.")

# \r : 커서를 맨 앞으로 이동시킴
# \b : 앞 글자 하나를 Backspace
# \t : 키보드 Tab(탭)과 같이 여러 칸을 띄어줌


print("Red Apple\rPine")
print("Redd\bApple")
print("Red\tApple")


"""
#퀴즈1. 
키(kg)과 몸무게(cm)를 입력받아 BMI(Body mass index)를 계산하는 코드를 만드세요.

BMI = weight(kg) / height(m)^2

#퀴즈2.
a = 'Inja University'
문자열의 마지막 4글자를 출력하시오.
i가 며 번 출현하는지 출력하시오.
인자대학교를 인제대학교로 수정하시오.

b = '010-1234-5678'
전화번호의 마지막 4자리를 ****으로 수정해 c로 저장하시오.

"""

# 퀴즈1
weight = 70
height = 178

BMI = weight / (height / 100) ** 2

print("당신의 BMI는", int(BMI), "입니다.")

# 퀴즈2
a = "Inja University"

print(a[-4:])
lower_a = a.lower()
print(lower_a.count("i"))
a = a.replace("Inja", "Inje")
print(a)

b = "010-1234-5678"
c = b.replace(b[-4:], "****")
print(c)
