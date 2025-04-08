# 클래스함수

class Student:
    count = 1
    
    def __init__(self,name,kor,eng,math):  # 생성자함수??
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1
        
    def stu_total(self):  # 성적을 수정했을 때 다시 합계를 계산하기 위한 함수
        self.total = self.kor+self.eng+self.math
    def stu_avg(self):    # 성적을 수정했을 때 다시 평균을 계산하기 위한 함수
        self.avg = self.total/3
        
    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"
        


class Students:
    