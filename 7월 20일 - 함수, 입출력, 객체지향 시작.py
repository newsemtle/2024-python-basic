# %% [markdown]
# 7. 함수
#

# %% [markdown]
# 7-1. 함수
#


# %%
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()

# %% [markdown]
# 7-2. 전달값과 반환값
#


# %%
def deposit(balance, money):
    balance += money
    print(f"입금이 완료되었습니다. 잔액은 {balance} 원입니다.")
    return balance


balance = 0
balance = deposit(balance, 1000)
print(balance)


# %%
def withdraw(balance, money):
    if balance >= money:
        balance -= money
        print(f"출금이 완료되었습니다. 잔액은 {balance} 원입니다.")
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원입니다.")
    return balance


balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
print(balance)


# %%
def withdraw_night(balance, money):
    commission = 100
    print(f"야간 출금 수수료는 {commission} 원 입니다.")
    return withdraw(balance, money + commission)


balance = 0
balance = deposit(balance, 1000)

balance = withdraw_night(balance, 500)
print(balance)

# %% [markdown]
# 7-3. keyword 인자
#
# cf. Positional Arguemnts, Keyword Arguments
#


# %%
def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="A", main_lang="파이썬", age=22)
profile(main_lang="자바", age=25, name="B")
profile("C", main_lang="C++", age=24)  # keyword 로 전달하는 경우, 항상 일반 전달값 뒤에


# %%
def profile(name, age=20, main_lang="파이썬"):
    print(name, age, main_lang)


profile("A", 22, "파이썬")
profile("B", 25)
profile("C")
profile("D", main_lang="자바")

args = ("E", 26, "C++")

profile(*args)  # (positional) arguments

other = {"name": "F", "age": 27, "main_lang": "R"}

profile(**other)  # keyword arguments

# %% [markdown]
# Quiz 1
#
# 이름을 부르며 인사하는 함수를 만드시오.
#
# welcome("철수") -> "환영해, 철수" 라고 **출력**하도록
#
# 이름을 부르며 인사하는 함수에 다음 기능을 추가하시오.
#
# welcome() -> "환영해, 이름 없는 당신"이라고 **출력**하도록
#


# %%
def welcome(name="이름 없는 당신"):
    print(f"환영해, {name}")


welcome()
welcome("이재원")

# %% [markdown]
# 7-4. 가변인자
#
# cf. * 와 packing, unpacking
#


# %%
def profile(name, age, lang1, lang2, lang3, lang4, lang5):  # 기본 인자
    print(name, age, end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile("A", 20, "Python", "Java", "C", "C++", "C#")
profile("B", 25, "Kotlin", "Swift", "", "", "")


# %%
def profile(name, age, *language):  # 기본 인자 + 가변 인자
    print(f"이름: {name}, 나이: {age}, ", end="")

    print("언어: ", end="")
    for lang in language:
        print(lang, end=" ")
    # print(*language, end="")
    print()
    # print(type(language))


profile("A", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("B", 25, "Kotlin", "Swift")

# unpacking
lang_list = ("C", "C++")
profile("C", 30, *lang_list)  # profile("C", 30, "C", "C++")

params = ("D", 27, "Go", "Rust")
profile(*params)  # profile("D", 27, "Go", "Rust")

print(*params)


# %%
def profile(name, age, *language, **other):  # 기본 인자 + 가변 인자 + 가변 키워드 인자
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Languages: {', '.join(language)}")

    for key, value in other.items():
        print(f"{key.capitalize()}: {value}")


profile("A", 25, "Python", "Java", "C++", country="Korea", hobby="Programming")
print()

langs = ["Python", "Java", "C++"]
others = {"country": "Korea", "hobby": "Programming"}
profile("A", 25, *langs, **others)
# profile("A", 25, "Python", "Java", "C++", country="Korea", hobby="Programming")
print()

profile("C", 21, "Python", country="Korea")

# %% [markdown]
# 7-5. 지역변수, 전역변수
#

# %%
bread = 10


def sell(customers):
    bread -= customers
    print(f"[함수 내] 남은 빵 : {bread}")


print(f"전체 빵 : {bread}")
sell(2)
print(f"남은 빵 : {bread}")

# %%
bread = 10


def sell(customers):
    bread = 20
    bread -= customers
    print(f"[함수 내] 남은 빵 : {bread}")


print(f"전체 빵 : {bread}")
sell(2)
print(f"남은 빵 : {bread}")

# %%
bread = 10


def sell(customers):
    global bread
    bread -= customers
    print(f"[함수 내] 남은 빵 : {bread}")


print(f"전체 빵 : {bread}")
sell(2)
print(f"남은 빵 : {bread}")

# %%
bread = 10


def sell_ret(bread, customers):
    bread -= customers
    print(f"[함수 내] 남은 빵 : {bread}")
    return bread


print(f"전체 빵 : {bread}")
bread = sell_ret(bread, 2)
print(f"남은 빵 : {bread}")


# %%
def increase1():
    global a
    b = 20
    a += 1
    b += 1


def increase2(x):
    x += 1
    return x


a = 10
b = 20
increase1()
c = 30
d = 40
increase2(c)
d = increase2(d)
print(a, b, c, d)

# %% [markdown]
# Quiz 2
#
# 표준 체중을 구하는 프로그램을 작성하시오
#
# > 남자 : 키(m)^2 x 22
# > 여자 : 키(m)^2 x 21
#
# -   조건1 : 표준 체중은 별도의 함수 내에서 계산
#     -   함수명 : `std_weight`
#     -   전달값 : 키(`height`), 성별(`gender`)
# -   조건2 : 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
#


# %%
def std_weight(height, gender):
    if gender == "남자":
        return height**2 * 22
    elif gender == "여자":
        return height**2 * 21
    else:
        return -1


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")

# %% [markdown]
# 8-1. 표준 입력 : input() 함수를 통해 사용자로부터 데이터를 받는 과정

# input() : 괄호 안의 내용을 print -> 사용자로부터 내용 입력받음 -> 입력값은 "문자열"로 반환됨.

# %%
name = input("이름을 입력하세요")
print(name + "님, 안녕하세요!")

# %% [markdown]
# 8-2 표준 출력 : 프로그램의 결과를 화면에 출력하는 과정

# print() : 괄호 안의 내용을 화면에 출력함.

# print()에 사용되는 파라미터

# %%
# 1) sep : 변수 사이에 들어갈 문자 지정 / end : 출력값 끝에 들어갈 문자 지정(기본은 \n)

print("셈틀", "인제대")
print("셈틀", "인제대", sep="그리고")
print("인제대", end="에서 ")
print("밥을", "먹는다")

# %%
# 2) 문자열 포맷팅 : 1강 참고.

# %%
# 3) zfill : 지정 길이만큼 0을 채워줌.
# ljust(길이, 문자) : 지정 길이만큼 문자를 채워줌. 기존 문자열은 좌로 정렬됨.
# rjust(길이, 문자) : 지정 길이만큼 문자를 채워줌. 기존 문자열은 우로 정렬됨.

ex = "def"
print(ex.zfill(4))
print(ex.rjust(5))
print(ex.ljust(5, "a"))

# %%
# 4) .format() 기타 포맷팅
print("{0: <10}".format(10))  # 좌정렬
print("{0: >10}".format(10))  # 우정렬
print("{0: ^10}".format(10))  # 중앙정렬
print("{0: <10}/{1}".format(2, 5))

print("{:f}".format(5 / 3))  # 소수점 출력
print("{:.2f}".format(5 / 3))  # 소수점 n번째까지 출력

# %% [markdown]
# 8-3 파일 입출력

# 1) open() : 특정 파일을 만들거나, 내용을 덧붙이거나, 읽어올 수 있음.
# open("파일이름", "사용방식", encoding = "utf8")
# 사용방식 "w": 만들기(쓰기) / "a" : 덧붙이기 / "r" : 읽어오기

# %%
food_file = open("foods.txt", "w", encoding="utf8")
print("돈까스: 10000원", file=food_file)
print("냉면: 12000원", file=food_file)
food_file.close()


food_file2 = open("foods.txt", "a", encoding="utf8")
food_file2.write("스파게티: 9000원")  # 공백문자 추가해야 됨..
food_file2.write("라멘: 9500원")
food_file2.close()

food_file3 = open("foods.txt", "r", encoding="utf8")
print(food_file3.read())
food_file3.close()

food_file4 = open("foods.txt", "r", encoding="utf8")
print(food_file4.readline())  # 줄별로 읽기, 커서는 다음 줄로 이동함.
print(food_file4.readline())
food_file4.close()

food_file5 = open("foods.txt", "r", encoding="utf8")
lines = food_file5.readlines()  # list형식으로 저장함.
for line in lines:
    print(line, end="")
food_file5.close()

# %% [markdown]
# 8-4 : pickle 모듈
# 객체 자체를 저장함. (텍스트로 변환 저장 X)

# %%
import pickle as pk

profile_f = open("profile.pk", "wb")
profile = {"이름": "제은찬", "나이": 21, "취미": ["악기", "코딩"]}
print(profile)
pk.dump(profile, profile_f)
profile_f.close()

profile_f2 = open("profile.pk", "rb")
profile2 = pk.load(profile_f2)
print(profile2)
profile_f2.close()

# %% [markdown]
# 8-5 with문

# 파일을 열고, 닫는 것을 간결화함.
# with open() as 변수:
# 내용
# 변수 = open()

# %%
food_file = open("foods.txt", "r", encoding="utf8")
with open("foods.txt", "r", encoding="utf8") as food_file:
    print(food_file.read())

# %% [markdown]
# 9-1 클래스와 객체지향

# 클래스란? 전반적인 "설계도"
# 설계도의 기본 틀을 정해 놓고, 세부사항만 따로 지정해주면 여러 상품(=객체)을 만들 수 있다!


# %%
class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0


my_car = Car("Busan", "A1", 2024)

print(my_car.year)
