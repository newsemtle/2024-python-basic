# Module: 단일 파이썬 파일


def say_good_morning(name):
    print("Good morning, " + name)


def say_good_afternoon(name):
    print("Good afternoon, " + name)


def say_good_evening(name):
    print("Good evening, " + name)


print("이 모듈은 인사를 위한 모듈입니다.")

if __name__ == "__main__":
    print("이 코드는 이 모듈을 직접 실행하는 경우에만 실행됩니다.")
else:
    print("코드를 외부에서 실행하고 계시는 군요!")
