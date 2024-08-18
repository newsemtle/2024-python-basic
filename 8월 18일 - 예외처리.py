#에러란 : 예상치 못한 어떤 실책이나 실수, 또는 잘못된 무언가
#이런 에러 상황을 처리하는 것을 예외(Exception)이라고 함.
#컴퓨터에서 계산기 프로그램을 이용하려고 하는데 실수로 숫자 대신 문자를 입력받은 경우 
#등이 있을 수 있음

#이렇듯 프로그램에서는 많은 에러 상황이 발생할 수 있으며, 이를 어떻게 처리하느냐에 따라
#좋은 프로그램이 되거나, 
# 갑자기 응답 없음 상태로 있다가 강제 종료되어서 아무것도 안 되는 프로그램이 될 수도 있음


print("나누기 전용 계산기입니다.")

num1 = int(input("첫 숫자를 입력하라."))
num2 = int(input("둘째 숫자를 입력하라"))
print(f"{num1} / {num2} = {num1/num2}")


#그런데 만약 숫자가 아닌 문자를 입력하면 어떻게 될까?

#"삼"은 정수로 변환을 할 수 없는 문자라서 에러 발생함.

#에러에 대한 예외 처리는 다음과 같은 형태로 작성함

'''
try:
    실행명령문1
    실행명령문2

except 에러 종류 1:
    예외 처리 명령문1
    예외 처리 명령문2

except 에러 종류 2:
    예외 처리 명령문1
    예외 처리 명령문2

'''

#앞에서 발생한 에러 메시지 중 마지막 문장은
#ValueError임. 값이 잘못되어서 발생하는 에러인데 이에 대한 예외처리를 해보자.

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 숫자를 입력하라."))
    num2 = int(input("둘째 숫자를 입력하라"))
    print(f"{num1} / {num2} = {num1/num2}")
except ValueError:
    print("에러입니다. 잘못된 값 입력")

#삼을 넣으면 except쪽의 print문이 실행됨
#6과 0을 넣으면 ZeroDivisionError가 나옴. 0으로 나눌 수 없기 때문임
#이러면 예외구문을 추가해줌
#에러 뒤에 as 구문을 이용하여 에러에 이름을 지어줄 수 있음.
#이를 통해 에러 메시지를 직접 출력해보자


try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 숫자를 입력하라."))
    num2 = int(input("둘째 숫자를 입력하라"))
    print(f"{num1} / {num2} = {num1/num2}")
except ValueError:
    print("에러입니다. 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)

#또 다른 에러 발생시켜볼까?

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 숫자를 입력하라.")))
    nums.append(int(input("둘째 숫자를 입력하라")))
    #nums.append(int(nums[0]/nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러입니다. 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)

#Index 에러가 발생함.
#이렇듯 많은 에러가 발생할 수 있는데, 이런 에러 하나하나에 다 예외처리를 해주기 어려울 수 있음
#그럴 경우 except Exception as err: 구문을 추가해줌

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 숫자를 입력하라.")))
    nums.append(int(input("둘째 숫자를 입력하라")))
    #nums.append(int(nums[0]/nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError:
    print("에러입니다. 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러.")
    print(err)


#의도적으로 에러를 발생시킬 수도 있음. raise를 써줌

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


#사용자가 직접 에러를 정의하고 그에 대한 예외처리를 할 수 있음
#먼저 클래스를 만들어주고 Exception 클래스를 상속시켜줌. 이렇게 하면 새로운 형태의 Error 정의

class BigNumberError(Exception):
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError:
    print("에러 발생. 한 자리 숫자만 입력하시오.")


#이 BigNumberError의 코드를 보완해서 바꿀 수 있음
#__str__()메소드는 멤버변수 msg를 반환해줌
#try 구문 내에서는 Big

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러 발생. 한 자리 숫자만 입력하시오.")
    print(err)


#try 구문을 사용할 때는 finally라는 게 있음. finally는 try 구문 내에서 에러가 발생하건 말건
#try를 벗어나는 시점에 무조건 실행되는 구문임. try와 except 구문 맨 밑에 정의.

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError(f"입력값 : {num1}, {num2}")
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러 발생. 한 자리 숫자만 입력하시오.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
