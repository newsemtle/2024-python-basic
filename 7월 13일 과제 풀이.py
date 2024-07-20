# %% [markdown]
# ### Quiz 1
#
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
#
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : `random` 모듈의 `shuffle`, `sample` 을 활용
#
# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --
#

# %%
import random

lst = [1, 2, 3, 4, 5]
print(lst)

random.shuffle(lst)
print(lst)

print(random.sample(lst, 1))

# %%
from random import sample, shuffle

commenters = list(range(1, 21))

# chicken = sample(commenters, 1)[0]
# commenters.remove(chicken)
# coffee = sample(commenters, 3)

chicken, *coffee = sample(commenters, 4)

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {chicken}")
print(f"커피 당첨자 : {coffee}")
print("-- 축하합니다 --")

# %% [markdown]
# ### Quiz 2
#
# 당신은 카카오택시를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
#
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [-] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [-] 50번째 손님 (소요시간 : 16분)
#
# 총 탑승 승객 : 2 분
#

# %%
from random import randrange

total_passengers = 0

for i in range(1, 51):
    travel_time = randrange(5, 51)

    if 5 <= travel_time <= 15:
        print(f"[O] {i}번째 손님 (소요시간 : {travel_time}분)")
        total_passengers += 1
    else:
        print(f"[-] {i}번째 손님 (소요시간 : {travel_time}분)")

print(f"총 탑승 승객 : {total_passengers}분")

# %% [markdown]
# ### Quiz 3
#
# 정수형 숫자 A, B를 입력받아 크기를 비교한 뒤 다음과 같이 출력하시오.
#
# -   A가 B보다 10 이상 크면 "A가 B보다 많이 큽니다."
# -   A가 B보다 1~9 크면 "A가 B보다 약간 큽니다."
# -   A와 B가 같으면 "A와 B가 같습니다."
# -   A가 B보다 1~9 작으면 "A가 B보다 약간 작습니다."
# -   A가 B보다 10 이상 작으면 "A가 B보다 많이 작습니다."
#

# %%
A = int(input("A = "))
B = int(input("B = "))
gap = A - B

if gap >= 10:
    print("A가 B보다 많이 큽니다.")
elif gap > 0:
    print("A가 B보다 약간 큽니다.")
elif gap == 0:
    print("A와 B가 같습니다.")
elif gap > -10:
    print("A가 B보다 약간 작습니다.")
elif gap <= -10:
    print("A가 B보다 많이 작습니다.")

# %% [markdown]
# ### Quiz 4
#
# 주사위 2개를 던져 나올 수 있는 조합의 경우의 수를 모두 출력하시오.
# 단, (1,2)와 (2,1)처럼 순서가 다르더라도 같은 숫자로 이루어진 조합은 동일한 조합으로 간주해 둘 중 한 가지만 출력한다.
#

# %%
for i in range(1, 7):
    for j in range(1, 7):
        if i > j:
            continue
        print(i, j)

# %%
for i in range(1, 7):
    for j in range(i, 7):
        print(i, j)

# %%
from itertools import combinations_with_replacement

dice = [1, 2, 3, 4, 5, 6]

for case in combinations_with_replacement(dice, 2):
    print(case)
