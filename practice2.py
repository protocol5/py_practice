#연산자
print(2**3) # 2^3
print(5%3) # 나머지 구하기 2
print(10//3) #몫 구하기 3
print(10/3) #나눗셈 3.3333...
print(4>=7) #참거짓 판단
print(3+4 == 7)
print(7== 3+4) #연산 우선 확인
print(3!=3) # not 표현 false
print(3 and 5)
print(0 & 1) 
print(1 or 0)
print(1>0 | 1<0)
print( 5 > 4 > 7) #false

#간단한 수식
num = 12
print(num+12)
num /= 2
print(num)
num += 2
print(num)

#숫자처리 함수
print(abs(-5)) # 절대값
print(pow(4,2)) # 제곱승
print(max(5,12)) # min 은 최소
print(round(3.8123))#반올림

#매스 라이브러리 활용
from math import * # math 모듈의 모든 함수를 쓰겠다
print(floor(4.121)) #내림
print(ceil(4.121))#올림
print(sqrt(16))# 제곱근

#랜덤함수
from random import *
print(random()) #0.0 ~1.0 사이의 임의의 값 생성
print(random()*10) #곱해서 난수 범위를 정함
print(int(random()*10)) #타입 캐스팅을 통해 정수화
print(randrange(1, 46)) # 1부터 45까지의 숫자 랜덤 출력
print(randint(1,46)) # 1부터 46까지의 숫자 랜덤 출력

#quiz-2
#월 4회 스터디,  3회 온라인 1번 오프라인.
#오프라인 모임 날짜를 랜덤으로 정해주는 프로그램 작성.

day = randrange(3,29)
print("오프라인 스터디 모임날짜는 매월",str(day)+"일로 선정되었습니다.")