# 08 시험 X

# 절차지향 프로그래밍(C언어)
# + 함수를 만들고 순차적으로 프로그램이 동작하는 방식
# + file 1개에 모든 코드를 넣고 위에서부터 아래로 실행
# + 함수 호출     함수 정의
#   함수 정의     함수 호출
#      (X)          (O)
# + 객체나 클래스 없이 바로 개발 가능(개발 속도 UP)
# + 코드 재사용과 유지보수가 어려움(비용 DOWN)


# 객체지향 프로그래밍(JAVA, Python)
# + 함수가 어디 있든 객체를 사용해서 호출 가능
# + 객체나 클래스를 사용하기 때문에 다량의 메모리 필요(개발 속도 DOWN)
# + 코드 재사용과 유지보수 용이

# Class(도면)
# + 객체 설계 도면

# Object(객체)
# + Class로 생성된 구체화된 객체 -> 인스턴스
# *****Python의 모든 것은 객체(인스턴스)
# - 기본자료형(프리미티브 타입) : 변수에 실제 값이 저장
# - 객체자료형(레퍼런스 타입) : 변수에 실제 값이 위치한 주소 저장
#   -> C      : 기본
#   -> JAVA   : 기본 + 객체
#   -> Python : 객체
#   cf) NULL : 참조할 대상이 없는 경우, 값이 없다.(X)
a = 4
b = a
print(id(a))    # id() : 값의 주소 출력
print(id(b))

# 프로그래밍 언어 메모리 영역
# - stack, Heap, Data, Code, ...

# ** 객체 사용 3단계 **
# Class(도면) -> 객체 생성 -> 인스턴스(결과물) -> 인스턴스 사용

# 1. Class(도면) 작성
# + 파스칼 표기법 사용
# + 멤버함수는 첫 번째 인자로 반드시 self를 사용
# + self : 인스턴스(결과물) 자기자신

class ChosunTest:
    def print_name(self):
        print("초롱")
        
# 2. 객체 생성
# + () 붙음 -> 함수(스네이크 표기법)
# + 생성자 하수() -> 예외적으로 클래스 이름과 동일(계속 파스칼 사용, 이 때문에 Class와 혼동 쉬움)
# + Class에 생성자 함수를 생략하면 디폴트 생성자 함수 자동 생성
# Class가 동일하더라도 생성된 인스턴스는 각각 다름
# 힐스테이트 수완점 봉선점 설계도면 같다고 같은 아파트로 보진 않잖음..결과적으로 다 다르게 나옴!test = ChosunTest()
test1 = ChosunTest()
test2 = ChosunTest()
# (X) test = test1 = test2
# print(id(test))
# print(id(test1))
# print(id(test2))
        
# 3. 객체 사용
test.print_name()

# 객체를 사용하면 좋은 점
# 1. 상속
class parent:
    def print_star(self):
        print("*")

class Child:
    pass     # = 이름 설계 도면만 만들고 아무 코드도 안 넣음

# 상속 X -> 쓸 수 있는 기능 X
#ch = Child()
#ch.          

# 상속 O -> 쓸 수 있는 기능 뜸, 코드 재사용성 UP
class Child(parent):
    pass

ch = Child()
ch.print_star()

# 이론 : class 어떻게 만들어야 할까?
# -> 모델링(객체모델링)
# cf) 모델링 : 현실세계 -> 컴퓨터 세계로 구현

# 현실세계
# -> 아이디, 이름, 나이를 입력하면 회원가입을 할 수 있다.

# 컴퓨터 세계
class Member:
# 필드(변수)
    id = "nkcd_1"
    name = "차연주"
    age = 21
# 멤버 함수
    def member_join(self, id, name, age):
        print("회원가입을 한다.")
        
mem = Member()
mem.member_join("ckduswn12", "너굴희", "20")