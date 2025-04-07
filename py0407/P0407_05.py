# 변수, 함수 집합체 - 변수에 대한 그룹핑 kor,eng,math
# list, dict타입 - 함수까지 sum,avg,rank
# 입력받을때...처리. 수정할때... 직접처리
# 특정데이터 값이 들어왔을때... 잘못된 데이터는 입력이 안되도록 구현
# class는 정의해야 할 것은 list에 비해 많지만(프로그램 복잡성), 파일 정보에 대한 보안성은 class가 상위


class Car:
    def __init__(self,color,tire,door):  # 생성자 __init__
        self.color = color  # self.color : Car변수, color : 요청받은 변수
        self.tire = tire
        self.door = door
        self.speed = 0
    
    # 속도
    def speedUp(self,s):
        self.speed += s
    def speedDown(self,s):
        self.speed -= s


# 생성자를 사용한 객체선언과 동시에 데이터 입력
c = Car("red",5,4)

# 기본형태 객체선언 후 데이터 입력
# a2 = Car()   # 차를 구매한후 색칠도 다시하고, 문짝도 달고, 타이어도 달고... 생성자를 만들기
# a2.color = 'red'
# a2.tire = 5
# a2.door = 4

c2 = Car("blue",5,5)



# class Car:
#     color = "white"
#     tire = 4   # 기본값은 미리 세팅
#     door = 5
#     speed = 0
    
#     # 속도
#     def speedUp(self,s):
#         self.speed += s
#     def speedDown(self,s):
#         self.speed -= s


# # 리스트 선언
# a_list = [1,2,3,4,5]
# # 리스트 값 입력
# a_list[0] = 50
# # 리스트 출력
# print(a_list)

# # 클래스 객체선언
# a = Car()
# # 클래스 변수에 값 입력 - 참조변수.변수명
# a.speed = 50  
# # 클래스 변수 값 출력 - 참조변수.변수명
# print(a.speed)

# # 함수 사용방법 - 참조변수.함수명
# a.speedUp(20)
# print(a.speed)

# a_list2 = [1,2,3,4,5]
# a_list2 = a_list  # 얕은복사
# a_list2 = [*a_list]

# # class는 구현한 뒤 사용이 많을수록 편리함. 선언만 하면 똑같이 만들어지지만, 다른 변수
# # 각각의 변수, 함수가 됨. 깊은 복사

# # red,5,4
# a2 = Car()   # 차를 구매한후 색칠도 다시하고, 문짝도 달고, 타이어도 달고... 생성자를 만들기
# a2.color = 'red'
# a2.tire = 5
# a2.door = 4

# # blue,5,5
# a3 = Car()
# a2.color = 'blue'
# a2.tire = 5
