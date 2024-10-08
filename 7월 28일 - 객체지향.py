# 9-1 클래스와 객체지향

# 클래스란? 전반적인 "설계도"
# 설계도의 기본 틀을 정해 놓고, 세부사항만 따로 지정해주면 여러 상품(=객체)을 만들 수 있다!


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0


my_car = Car("Busan", "A1", 2024)

print(my_car.year)

# 9-2 메서드

# 설계도 내에서 "기능"을 정의하는 부분
# 함수 형태 (def __init__ 역시 메서드)


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0

    def get_descriptive_name(self):  # 새로운 기능(함수) = 메서드 추가
        return f"{self.year} {self.make} {self.model}"  # 메서드를 실행했을 때의 반환값.


my_car = Car("Busan", "A1", 2024)

print(my_car.get_descriptive_name())

# 9-3 멤버변수
# 클래스 내에서 정의된 변수. 클래스 내부 타 메서드에서 사용이 가능하다. self.xx형태


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0

    def get_descriptive_name(self):  # 새로운 기능(함수) = 메서드 추가
        return f"{self.year} {self.make} {self.model}"  # 메서드를 실행했을 때의 반환값.

    def update_odometer(self, mileage):  # 주행 거리를 업데이트하는 메서드
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 주행 거리를 증가시키는 메서드
        self.odometer_read += miles

    def read_odometer(self):  # 주행 거리 표시 메서드
        return f"This car has {self.odometer_read} miles on it."


my_car = Car("Busan", "A1", 2024)

# 초기 주행 거리 확인
print(my_car.read_odometer())  # 출력: This car has 0 miles on it.

# 주행 거리 업데이트
my_car.update_odometer(1500)
print(my_car.read_odometer())  # 출력: This car has 1500 miles on it.

# 주행 거리 증가
my_car.increment_odometer(100)
print(my_car.read_odometer())  # 출력: This car has 1600 miles on it.

# 9-4 상속
# 상위 클래스가 가지고 있는 속성을 하위 클래스에서 사용할 수 있게 하는 것.
# 상위 클래스의 파라미터, 메서드를 하위 클래스에서도 사용할 수 있게 된다.


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0

    def get_descriptive_name(self):  # 새로운 기능(함수) = 메서드 추가
        return f"{self.year} {self.make} {self.model}"  # 메서드를 실행했을 때의 반환값.

    def update_odometer(self, mileage):  # 주행 거리를 업데이트하는 메서드
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 주행 거리를 증가시키는 메서드
        self.odometer_read += miles

    def read_odometer(self):  # 주행 거리 표시 메서드
        return f"This car has {self.odometer_read} miles on it."


class ElectricCar(Car):  # 상위메서드를 괄호 안에 기입

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 상위 메서드의 초기화 메서드를 호출
        self.battery_size = 75

    def describe_battery(self):  # 배터리 사이즈를 알려주는 새 메서드
        return f"This car has a {self.battery_size}-kWh battery."


my_Seoul = ElectricCar("Seoul", "A3", 2025)
print(my_Seoul.get_descriptive_name())
print(my_Seoul.describe_battery())

# 부모 클래스의 메서드도 사용 가능
print(my_Seoul.read_odometer())
my_Seoul.update_odometer(500)
print(my_Seoul.read_odometer())

# 9-5 다중상속
# 한 클래스가 여러 가지의 클래스를 상속받는 것이다.
# ElectricCar클래스의 상위 클래스인 Battery 클래스를 정의하고, Car클래스와 같이 다중상속 해보자.


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0

    def get_descriptive_name(self):  # 새로운 기능(함수) = 메서드 추가
        return f"{self.year} {self.make} {self.model}"  # 메서드를 실행했을 때의 반환값.

    def update_odometer(self, mileage):  # 주행 거리를 업데이트하는 메서드
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 주행 거리를 증가시키는 메서드
        self.odometer_read += miles

    def read_odometer(self):  # 주행 거리 표시 메서드
        return f"This car has {self.odometer_read} miles on it."


class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


class ElectricCar(Car, Battery):  # 상위메서드(2개)를 괄호 안에 기입

    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)  # 상위 메서드의 초기화 메서드를 호출
        Battery.__init__(self, battery_size)  # 상위 메서드의 초기화 메서드를 호출
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


my_Seoul = ElectricCar("Seoul", "A3", 2025, 75)
print(my_Seoul.get_descriptive_name())
print(my_Seoul.describe_battery())

# 부모 클래스의 메서드도 사용 가능
print(my_Seoul.read_odometer())
my_Seoul.update_odometer(500)
print(my_Seoul.read_odometer())

# 9-6 메서드 오버라이딩
# 상위 클래스에서 정의된 메서드를 하위 클래스에서 재정의하는 행위.


class Car:

    def __init__(self, make, model, year):  # self는 필수, 뒤의 파라미터는 입력받을 속성 순서대로..

        self.make = make
        self.model = model
        self.year = year  # 입력받은 속성을 객체 내부에 저장함.
        self.odometer_read = 0

    def get_descriptive_name(self):  # 새로운 기능(함수) = 메서드 추가
        return f"{self.year} {self.make} {self.model}"  # 메서드를 실행했을 때의 반환값.

    def update_odometer(self, mileage):  # 주행 거리를 업데이트하는 메서드
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 주행 거리를 증가시키는 메서드
        self.odometer_read += miles

    def read_odometer(self):  # 주행 거리 표시 메서드
        return f"This car has {self.odometer_read} miles on it."


class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


class ElectricCar(Car, Battery):  # 상위메서드(2개)를 괄호 안에 기입

    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)  # 상위 메서드의 초기화 메서드를 호출
        Battery.__init__(self, battery_size)  # 상위 메서드의 초기화 메서드를 호출
        self.battery_size = battery_size

    def update_odometer(
        self, mileage
    ):  # Car 클래스에 있는 속도계 메서드를 하위 ElectricCar에서 새롭게 정의함 = 오버라이딩
        if mileage >= self.odometer_read:
            self.odometer_read = mileage
            print(f"Odometer updated to {self.odometer_read} miles.")
        else:
            print("You can't roll back an odometer!")

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


my_Seoul = ElectricCar("Seoul", "A3", 2025, 75)
print(my_Seoul.get_descriptive_name())
print(my_Seoul.describe_battery())

# 부모 클래스의 메서드도 사용 가능
print(my_Seoul.read_odometer())
my_Seoul.update_odometer(500)
print(my_Seoul.read_odometer())

# 9-7 super()
# 상위 클래스의 메서드를 호출할 때 사용
# 상속 과정에서 초기화 메서드 호출할 때 & 하위 메서드에서 상위 클래스의 특정 메서드를 사용하고 싶을 때


class ElectricCar(Car, Battery):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(
            make, model, year
        )  # 다중 상속에서는 가장 왼쪽의 부모 클래스의 초기화 메서드가 호출됨
        Battery.__init__(self, battery_size)

    def update_odometer(self, mileage):
        super().update_odometer(mileage)
        print(f"Odometer updated to {self.odometer_read} miles.")


my_Seoul.update_odometer(300)
# 출력: Odometer updated to 300 miles.
print(my_Seoul.read_odometer())  # 출력: This car has 300 miles on it.
