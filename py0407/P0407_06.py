# 인스턴스 변수 = 객체 변수, 객체를 선언할 때 만들어짐

class Student:
    # 변수는 있는만큼 메모리를 잡아먹기 때문에 쓸데없이 만들면 안됨, 나중에 필요할 변수를 미리 만드는 것은 ㄱㅊ??
    phone = ""     # 인스턴스 변수 - 객체변수 : 각각의 객체별로 사용되는 변수
    address = ""   
    count = 1   # 클래스변수 사용 - 모든 객체가 공용으로 사용하는 변수
    
    def __init__(self,name,kor,eng,math):
        self.no = Student.count  # 클래스변수
        Student.count += 1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    def s_total(self):
        self.total = self.kor+self.eng+self.math
    
    def s_avg(self):
        self.avg = self.total/3
    
    def s_print(self):
        print("학생 :",self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank)
        
# 객체선언    변수 - 생성자호출
# no 번호를 부여하지 않음.  = 1
s = Student("홍길동",100,100,99)
s.s_print()
# no 번호를 부여하지 않음   = 2
s2 = Student("유관순",90,91,99)
s2.s_print()
s3 = Student("이순신",80,80,88)
s3.s_print()

# 




# s.kor = 50
# s.s_total()
# s.s_avg()
# s.s_print()

# class의 장점 - 객체선언시 변수/함수 동시에 넣을 수 있음