class Student:
    # 인스턴스 변수 - 객체선언시 변수들 각각 변수들이 존재 : 공용으로 사용 안됨.
    # no = 1
    # name = "" # 인스턴스 변수
    count = 1   # 클래스변수 - 모든 객체가 공용으로 사용하는 변수
    
    # 생성자함수
    def __init__(self,name,kor,eng,math):
        self.no = Student.count     # 인스턴스 변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1         # 1증가
    
    def __str__(self):  # 특별함수?? 위에서 상속받아 진행, 오버라이딩
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"
        

class Students:
    def __init__(self):
        self.students = []
    
    def add(self,s):
        self.students.append(s)

    def __str__(self):   # 리턴을 무조건 문자열로 받아야 함
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""


# print(s)  # <__main__.Student object at 0x000001C531E16900>




# 매개변수가 있는 생성자를 활용해서 데이터 입력
# s = Student("홍길동",100,100,99)   # 매개변수가 있는 생성자 객체선언
# print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank,Student.count)  # 2
# s2 = Student("유관순",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,s2.total,s2.avg,s2.rank,Student.count)  # 3
# print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank,Student.count)  # 3
# s3 = Student("이순신",90,90,91)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,s3.total,s3.avg,s3.rank,Student.count)  # 4
# print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank,Student.count)  # 4




# a_list = [1,2]

# 기본생성자를 가지고 객체선언후 데이터 입력
# s = Student()   # 기본생성자
# s.name = "홍길동"
# print(s.no,s.name)

# s2 = Student()
# s2.no = 2
# s2.name = "이순신"
# print(s2.no,s2.name)