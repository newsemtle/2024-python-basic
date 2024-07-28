# %% [markdown]
# ### Quiz 1
#
# 정수를 매개변수로 받아 구구단의 해당 단을 출력하는 함수를 만드시오.
#
# -   조건1: 5를 곱한 값은 출력하지 않도록 하시오.
#     -   예를 들어 gugudan(3)이라고 실행시키면 3단을 출력하되, 3 x 5 = 15는 출력하지 않음.
# -   조건2: 2에서 9까지의 숫자가 아닌 너무 크거나 작은 숫자를 매개변수로 받으면 "Not available"이라고 출력하도록 하시오.
#


# %%
def gugudan(n):
    if n < 2 or n > 9:
        print("Not available")
        return
    for i in range(1, 10):
        if i == 5:
            continue
        print(f"{n} x {i} = {n * i}")


n = int(input("정수를 입력하세요 "))
gugudan(n)

# %% [markdown]
# ### Quiz 2
#
# scores = [70, 80, 90, 95]
#
# 평균을 구하는 함수를 만드시오.
# (리스트의 요소 개수는 len()으로 알 수 있다)
#
# list의 표준편차를 구하는 함수를 만드시오.
# (표준편차는 각 값과 평균의 차를 제곱한 값들의 평균을 낸 후 제곱근을 취하면 계산할 수 있다.)
# (또는, 각 값의 제곱들의 평균에서 평균값의 제곱을 뺀 후 제곱근을 취하면 계산할 수 있다.)
#
# 제급근은 `math` module 내부에 `sqrt` 함수를 사용하여 구하시오.
#

# %%
from math import sqrt

a = 9
print(sqrt(a))

# %%
from math import sqrt

scores = [70, 80, 90, 95]


def mean(values):
    return sum(values) / len(values)


def standard_deviation(values):
    mean_value = mean(values)
    variance = mean([(i - mean_value) ** 2 for i in values])
    return sqrt(variance)


def standard_deviation2(values):
    variance = mean([i**2 for i in values]) - mean(values) ** 2
    return sqrt(variance)


print(mean(scores))
print(standard_deviation(scores))
print(standard_deviation2(scores))

# %% [markdown]
# ### Quiz 3
#
# a = "University"
# b = "Highschool"
#
# 두 단어를 입력받아 소문자로 변환해서 첫번째 단어에만 존재하는 알파벳을 반환하는 함수를 만드시오.
#
# -   in_both(a, b) -> { "i", "s" } 라고 **반환**
# -   print(in_both(a, b)) -> 출력
#
# list 내부 메소드인 `sort`를 사용하거나, python 에 내장된 `sorted` 함수를 활용하여 정렬하시오
#

# %%
lst1 = [3, 2, 5, 1, 4]
lst2 = [4, 3, 2, 5, 1]

return_value = lst1.sort()
print(return_value)
print(lst1)

sorted_list = sorted(lst2)
print(lst2)
print(sorted_list)

# %%
a = "University"
b = "Highschool"


def in_both(word1, word2):
    return sorted(set(word1.lower()) - set(word2.lower()))


result = in_both(a, b)
print(result)
print(in_both(a, b))
