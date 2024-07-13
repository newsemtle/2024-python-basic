# %% [markdown]
# # 2일차
#

# %% [markdown]
# 참고할 수 있는 자료들
#
# - dir(): 객체가 가지고 있는 메소드 목록을 확인할 수 있음
# - id(): 객체가 저장되어 있는 주소를 확인할 수 있음
# - [Python 공식 문서](https://docs.python.org/3/index.html): 내장 함수, 클래스, 패키지 등에 대한 정보를 얻을 수 있음
# - inspect 패키지: 객체의 여러 정보를 확인할 수 있는 도구들이 포함된 패키지
#

# %%
print(dir(int))
print(dir(str))

# %% [markdown]
# ## 5. 자료구조
#

# %% [markdown]
# ### 5-1. 리스트
#
# [ value1, value2, ... ]
#

"""
index: 특정 값이 첫번째로 등장하는 위치를 반환함
append: 특정 값을 뒤에 추가함
insert: 특정 위치에 특정 값을 추가함
count: 특정 값이 등장하는 횟수를 반환함
pop: 값을 제거하고 반환함 (기본: 마지막 값)
clear: 비움
sort: 정렬 (기본: 오름차순)
reverse: 역순 정렬. sort(reverse=True) 와 동일
extend: 전달 받은 리스트를 기존에 더함
copy: 동일 내용의 리스트를 생성함
remove: 특정 값이 등장하는 첫번째 위치에서 해당 값을 제거함
"""

# %%
line = ["이재원", "이건호", "오성목"]
print(line)

print(line.index("이건호"))

line.append("이재원")
print(line)

line.insert(2, "제은찬")
print(line)

print(line.count("이재원"))

last_person = line.pop()
print(last_person)
print(line)

line.clear()
print(line)

# %%
single_type_list = [7, 3, 4]
print(single_type_list)

multiple_type_list = [10, 1.4, "string"]  # int, float, string
print(multiple_type_list)

# %%
single_type_list.sort()
print(single_type_list)

single_type_list.reverse()
print(single_type_list)

single_type_list.extend(multiple_type_list)
print(single_type_list)

single_type_list += multiple_type_list
print(single_type_list)

# %% [markdown]
# ### 5-2. 사전
#
# { key1: value1, key2: value2, ... }
#

"""
get: 특정 key 값의 value 를 반환함. (기본: 없는 key이면 None 반환)
keys: 모든 key 반환함
values: 모든 value 반환함
items: 모든 item을 (key, value) 형태로 반환함
pop: item 을 제거하고 value 를 반환함 (기본: 마지막 값)
popitem: item 을 제거하고 item 을 반환함 (기본: 마지막 값)
clear: 비움
copy: 동일한 내용의 사전을 생성함
setdefault: key 가 있으면 value 를 반환하고, key 가 없으면 새로운 key-value 를 추가함
update: key 가 있으면 value 를 수정하고, key 가 없으면 새로운 key-value 를 추가함
fromkeys: key 목록과 배정될 값을 전달하면 그에 맞는 사전을 새로 생성함. dict.fromkeys() 로 사용함
"""

# %%
cabinet = {3: "이재원", 100: "이건호", 153: "오성목"}
print(cabinet)

cabinet.setdefault()

print(cabinet[3])  # 없는 key이면 error
print(cabinet.get(3))  # 없는 key이면 None 반환
print(cabinet.get(5, "사용 가능"))  # 없는 key이면 "사용 가능" 반환

print(3 in cabinet)
print(5 in cabinet)

cabinet[52] = "제은찬"
print(cabinet)

# %%
print(cabinet.keys())  # type: dict_keys
print(cabinet.values())  # type: dict_values
print(cabinet.items())  # type: dict_items

result = cabinet.pop(153)  # 특정한 key를 가진 항목 제거, value 반환
print(result)
print(cabinet)

last_item = cabinet.popitem()  # 마지막 항목 제거, item 반환
print(last_item)
print(cabinet)

cabinet.clear()
print(cabinet)

# %%
single_type_dictionary = {"A-302": "이재원", "B-205": "이건호", "C-104": "오성목"}
multiple_type_dictionary = {"a": 3, 2: 0.1, 4.6: "b"}
print(single_type_dictionary["A-302"])
print(multiple_type_dictionary[4.6])

# %% [markdown]
# ### Quiz 1
#
# ```
# me = { 'name': 'jaewon', 'attack': 30, 'defense': 15 }
# enemy = { 'name': 'slime', 'attack': 20, 'defense': 10 }
# ```
#
# -   me에서 'name'의 값을 본인의 이름으로 수정하시오.
# -   me에 'hobby': 'game'을 추가하시오.
# -   me가 enemy를 공격했을 때 입힐 수 있는 피해를 계산하시오. (me의 공격력에서 enemy의 방어력을 빼면 된다.)
#

# %%
me = {"name": "sangzin", "attack": 30, "defense": 15}
enemy = {"name": "slime", "attack": 20, "defense": 10}

me["name"] = "이재원"
# me.update("name", "이재원")
me["hobby"] = "game"
# me.setdefault("hobby", "game")
print(me)
print(me["attack"] - enemy["defense"])

# %% [markdown]
# ### 5-3. 튜플
#
# ( value1, value2, ... ): 추가, 삭제, 변경 불가능
#

"""
count: 특정 값이 등장하는 횟수를 반환함
index: 특정 값이 첫번째로 등장하는 위치를 반환함
"""

# %%
menu = ("돈까스", "치즈돈까스", "고구마돈까스")
print(menu)
print(menu[0])

extra_menu = ("냉면", "비빔면")
menu += extra_menu
print(menu)

a, b, c = 1, 2, 3  # 양쪽 모두 tuple
print(a, b, c)

a, b, c = c, b, a  # tuple 형태로 하나씩 할당되므로 가능한 방법
print(a, b, c)


# %% [markdown]
# ### Quiz 2
#
# ```
# a = ( 5, 4, 3 )
# b = ( 1, 2, 3 )
# ```
#
# -   a와 b를 연결시킨 튜플을 c로 저장하시오.
# -   a의 앞에 6을 추가하시오.
#

# %%
a = (5, 4, 3)
b = (1, 2, 3)

c = a + b
print(c)

a = (6,) + a
print(a)

# %% [markdown]
# ### 5-4. 세트(집합)
#
# { value1, value2, ... }: 중복, 데이터 순서 모두 없음
#

"""
intersection: 교집합
union: 합집합
difference: 차집합
add: 특정 값 추가
update: 여러 값 추가
remove: 특정 값 제거. 없는 값이면 오류 발생
discard: 특정 값 제거. 없는 값이어도 오류 없음
clear: 비움
copy: 동일한 내용의 집합을 생성함
"""

# %%
set1 = {1, 2, 3, 4, 5}
set2 = {1, 4, 7, 10, 13}
print(set1)

print(set1 & set2)  # 교집찹
print(set1.intersection(set2))

print(set1 | set2)  # 합집합
print(set1.union(set2))

print(set1 - set2)  # 차집합
print(set1.difference(set2))

# %%
set1.add(100)  # 단일 element
set1.update([200, 201, 202])  # 여러 element
print(set1)

set1.remove(3)
set1.discard(400)  # error 없음
print(set1)

# %% [markdown]
# ### 5-5. 자료구조 변환
#

# %%
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# cf
sentence = "Hello World"
print(list(sentence))

# %% [markdown]
# ### Quiz 3
#
# ```
# a1 = { 1, 2, 3, 4, 5, 6, 7, 8 }
# a2 = { 2, 4, 6, 8, 9, 10 }
# a3 = { 2, 3, 4, 5, 6, 7 }
# ```
#
# -   3개 과제를 모두 제출한 학생 명단을 출력하시오.
# -   2번 과제는 제출했지만 3번 과제를 제출하지 않은 명단을 출력하시오.
# -   1번 또는 2번 과제를 제출했지만, 3번 과제를 제출하지 않은 명단을 출력하시오.
#

# %%
a1 = {1, 2, 3, 4, 5, 6, 7, 8}
a2 = {2, 4, 6, 8, 9, 10}
a3 = {2, 3, 4, 5, 6, 7}

print(a1 & a2 & a3)
print(a2 - a3)
print((a1 | a2) - a3)

# %% [markdown]
# ## 6. 흐름제어
#

# %% [markdown]
# ### 6-1. if
#
# if, elif, else
#

# %%
weather = input("오늘 날씨는 어떻습니까? ")
print(weather)

# '=' 두번, if 마지막 ':', 조건문 내에 속하는 코드는 반드시 들여쓰기
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" or "황사":
    print("마스크를 챙기세요")
else:
    print("필요한 준비물이 없습니다")

# %%
temperature = int(input("기온은 어떻습니까? "))

if temperature >= 30:
    print("너무 더워요. 나가지 마세요")
elif temperature >= 10 and temperature < 30:
    print("괜찮은 날씨입니다")
elif 0 <= temperature < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# %% [markdown]
# ### 6-2. for
#

# %%
for waiting_no in range(1, 6):  # [1, 2, 3, 4, 5]
    print(f"대기번호 : {waiting_no}")

starbucks = ["이재원", "이건호", "오성목"]

for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다")

# %% [markdown]
# ### Quiz 4
#
# 구구단을 출력하시오. ( hint: 이중 for문 이용 )
#

# %%
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()

# %% [markdown]
# ### Quiz 5
#
# 1부터 20까지 순서대로 출력하되 3의 배수는 숫자 대신 '짝'을 출력하시오. ( hint: `i % 3` )
#

# %%
for i in range(1, 21):
    if i % 3 == 0:
        print("짝")
    else:
        print(i)

# %% [markdown]
# ### 6-3. while
#

# %%
customer = "이재원"
index = 5

while index >= 1:
    print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요.")
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# %%
customer = "이재원"
person = "Unknown"

while person != customer:
    print(f"{customer}, 커피가 준비 되었습니다.")
    person = input("이름이 어떻게 되세요? ")
    if person == customer:
        print("커피가 준비 되었습니다, 맛있게 드세요")

# %% [markdown]
# ### 6-4. continue, break
#

# %%
absent = [2, 5]
no_book = [7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    print(f"{student}, 책 읽어봐")

# %% [markdown]
# ### 6-5. 한 줄 for (List Comprehension)
#
# cf. Python One-Liner
#

# %%
nums = [1, 2, 3, 4, 5]

nums_plus_100 = [i + 100 for i in nums]
print(nums_plus_100)  # [101, 102, 103, 104, 105]

names = ["Jacob Collier", "Quincy Jones", "Michael Jackson"]

name_lengths = [len(i) for i in names]
print(name_lengths)

name_uppers = [i.upper() for i in names]
print(name_uppers)
