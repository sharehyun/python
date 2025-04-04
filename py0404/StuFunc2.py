



# 3. 학생성적수정 - 과목 수정
def stu_fix(s,sub_list,choice,title,name):
    pre_score = s[sub_list[choice]]  # 이전 점수 입력
    print(f"현재 {title[choice+1]} 점수 :",pre_score)
    s[sub_list[choice]] = int(input(f"변경 {title[choice+1]} 점수 : "))
    s['total'] = s['kor']+s['eng']+s['math']
    s['avg'] = s['total']/3
    print(f"{name} 학생 {title[choice+1]}점수 {pre_score}점을 {s[sub_list[choice]]}점으로 변경했습니다.")
    
# 4. 등수처리
def stu_rank(students):
    print("[ 등수처리 ]")
    for s in students:
        num = 1
        for ss in students:
            if s['total']<ss['total']:
                num += 1
        s['rank'] = num
    print("등수처리가 완료되었습니다.")
    print()