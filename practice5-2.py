#continue 와 break

absent = [2, 5] #결석
no_book = [7] #책을 놓고옴
for student in range (1,11) : 
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기 까지. {0}는 교무실로 따라와" .format(student))
        break
    print("{0}번, 책을 읽어봐" .format(student))

#한줄 for문
students = range(1,6)
students = list(students)
print(students)
students = [i + 100 for i in students] 
#ㄴ> 뒤에서 부터 해석하자. 스튜던트 리스트에 있는 i값들에 100씩더한 리스트를 만들어 스튜던트 리스트에 담드는다.
print(students)

#학생이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students1 = [len(i) for i in students]
print(students1)

#학생이름을 대문자로 변환해보자
students2= [i.upper() for i in students]
print(students2)

#quiz - 5
#50명의 승객에 대해서 탑승 승객을 구하라
#조건 1 운행소요시간은 5분~50분 사이 난수이다
#조건2 나느 소요시간 5~15분 사이 손니만 매칭한다
from random import *
# times = range(1,51)
# times = list(times)

# for customers in times :
#     time = int(random()*50)
#     if 5 <=time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))
#     elif 15 < time <=50 :
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(customers, time))

cnt = 0 #탑승승객
for i in range(1,11): #1~50이라는 승객
    time = randrange(5,51)
    if 5 <=time <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
        cnt +=1
    elif 15 < time <=50 :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))

print("총 탑승승객", cnt)
