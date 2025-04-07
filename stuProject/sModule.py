class Student:
    count = 1
    def __init__(self,name,kor,eng,math):  # self 붙이는 이유 - class 내에 들어가는 변수라고 선언. 점 앞 내용은 self 고정
        self.no = Student.count    # Student 내에 있는 count 변수를 불러옴. 1부터 시작하도록 위에 선언해야 함
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        Student.count += 1

    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"

class Students:
    def __init__(self):
        self.students = []

    def add(self,s):    # self.students에 객체변수를 더함
        self.students.append(s)

    def __str__(self):
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""   # return으로 꼭 문자열을 돌려받아야 함
