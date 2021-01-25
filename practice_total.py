#숫자 자료형
print(5)
print(-10)
print(3.14)
print(3+2*8)

#문자 자료형
print('풍선')
print("나비")
print("반복"*9)

#참거짓
print(5>19)
print(132==132)
print(not 10)
print(not True)

#변수정의
animal = "강아지"
name = "바둑이"
age = 4 
is_adult = age >= 3 #불리안, 정수형은 str()로 감싸야함

print(animal+" 이름은 "+name+" 이고 " + str(age) + " 이다.")
name = "이름 바꾸기"
print(name, "는 어른인가? :",  str(is_adult))# 컴마 , 는  띄어쓰기와 단어를 이어주는 +로 사용가능함.

#주석
'''여러문장을
한번에 주석 가능'''

"""
adsasd
"""

#quiz-1
station="사당"
print(station,"행 열차가 들어오고 있습니다.")
station= "신도림"
print(station,"행 열차가 들어오고 있습니다.")

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
#round(함수, 자릿수) 

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

#문자열
sentnce = """
여러 줄에 걸쳐서
문자열 적기
세 따옴표를 이용한
"""
print(sentnce)

#슬라이싱
ID = "950804-1234567"#문자열의 필요한 부분만을 잘라오는것
print("성별 : ", ID[7]) # 문자열 7번째의 문자를가져옴
print("년도 : ", ID[0:2]) #0부터 2직전까지 (0~1까지)
print("월 : ", ID[2:4]) #2부터 4직전까지 2~3까지.
print("생년월일 :  "+ID[:6]) # :6 처음부터 6직전까지, 즉 0~5까지
print("뒤 7자리 : ",ID[7:14],ID[7:]) #끝을 비우면 끝까지.

print("뒤에서부터 가져오기",ID[-7:],ID[-14:-7]) #-는 뒤에서 몇칸 앞으로 오는지.

#문자열 처리함수 
py="Python Is Amazing"
print(py.lower())
print(py.upper()) #문자열을 대문자로 바꿔줌
print(py[0].isupper()) #문자열의 첫번째는 대문자인가?
print(len(py)) #문자열 길이반환
print(py.replace("Python","Java")) #지정한 단어를 원하는 단어로 바꿈

index2 = py.index("n") #py 센텐스에서 n이 위치한 숫자를 반환
print(index2)

index2 = py.index("n",index2 + 1) # 찾은 n다음으로 나오는 n의 위치
print(index2)

print(py.find("n")) # n이 포함된 위치를 알려줌. 맨처음꺼를 리턴
print(py.find("kotlin")) #포함되지 않은 단어인경우 -1 를 리턴
#print(py.index("kotlin")) - > index에서는 포함되지 않는 단어가 있을 경우 에러를 뱉고 죽음.
print(py.count("n")) #해당 문자열에서 n이 몇번 등장하는지 세어준다.

#문자열포맷
print('정수 %d 출력 ' % 22)
print('나는 %s을 좋아해요' %"문자열")
print('하나의 %c을 출력'%'c')
print('다중 문자열 출력은 %s 와 %s'%('이렇게','저렇게'))
print("포맷을 활용하여 출력도 가능하다. 정수 :{}와 문자열:{}".format(20,'문자열'))
print("포맷의 순서를 바꿔줄 수도 있다 예를들어 {2}-1번, {1}-2번, {0}-3번" .format(1,2,3))
print("변수를 활용한 포맷 나이:{age}, 색상:{color}" .format(color='red', age =12))

#외부 변수 선언과 함께 문자열 앞 f로 포맷임을 알림
age= 20
color ="red"
print(f"나이 {age}, 색상 {color}")

#탈출문자
#\n 줄바꿈, "다중 문자열 '에이비씨' 가나다", "다중 \"문자열\""
#\\ -> 문장내에서 하나의 역슬래쉬
#\r 커서를 맨앞으로보냄
print("Red--Apple \rpine")
#\b백스페이스 한글자 삭제
print("Redd\bapple")
#t 탭

#quiz -3

url="https://naver.com"
rule=url.replace("https://","")#or rule=url[8:]
print("규칙1:",rule)
dot_index=rule.index(".")
rule=rule[:dot_index]
print("규칙2:",rule)
pw=rule[:3]+str(len(rule))+str(rule.count("e"))+"!"
print("{1}에서의 비밀번호는 {0}이다.".format(pw,url))
print("생성된 비밀번호: {rule}{len}{e}{c}" .format(rule = rule[:3], len=len(rule), e= rule.count("e"), c='!'))
print("생성된 비밀번호: %s%s%s%c" %(rule[:3],len(rule),rule.count('e'),'!'))

print('\n\n')
#리스트[] 순서를가지는 객체의 집합
subway=[10,"김모모","김모모","20",True]
print(subway)
#리스트 내의 객체 위치
print(subway.index("20"))
#추가하기
subway.append("김봉남")
print(subway)
#끼워넣기
subway.insert(1,"사이에넣기")
print(subway)
#빼내기
print(subway.pop())
print(subway)
#같은객체를 찾기
print(subway.count("김모모"))

#리스트 정렬
num_list=[4,6,1,2,6]
num_list.sort()
print(num_list)
#리스트 뒤집기가능
num_list.reverse()
print(num_list)
#모두지우기
num_list.clear()
print(num_list)

#리스트는 자료형에 영향을 받지 않음!_!
#리스트 합치기,또는 확장
num_list.append("a")#append 인자는 한개.
num_list.extend(subway)
print(num_list)

#딕셔너리
#!키는 중복이 되지않음.
cabinet={3:"유재석",100:"김태호"}
print(cabinet[3],cabinet[100])
print(cabinet.get(3)) #get을 통해서도 키에 해당하는 밸류를 가져올 수 있음.
#print(cabinet[5]) - >없는 키번호를 요구하면 에러뱉고 죽음.
print(cabinet.get(5)) # get은 없는 키번호를 none으로 리턴
print(cabinet.get(5,"비어있는 열쇠")) #가져오려고 시도하고 비어있으면 뒤의 문자열 출력

print(3 in cabinet) #해당하는 키값에 대한 참거짓 리턴

#키값읜 정수형 아니고 문자열로도 가능함.
cabinet2={"A-1":"배고파","C-10":"치킨"}
print(cabinet2["A-1"])
#키와 밸류 추가
cabinet[4]="피자"
print(cabinet)
#키값 지우기
del cabinet[100]
print(cabinet)
#키값만 출력
print(cabinet.keys())
#벨류값만 출력
print(cabinet.values())
#쌍으로 출력
print(cabinet.items())
#리스트와 동일하게 claer를 통해 비울수있음
cabinet.clear()
print(cabinet)

#튜플 - 값을 추가하거나 변경하지못하고 초기에 고정된 값만을 활용가능함
menu=("돈까스","치즈까스")
print(menu[1])
#menu.add -> XXXX안됨

name, age, hobby = "홍길동", 100, "밥먹기"
print(name, age, hobby)

#집합 (set)
#집합은 중복이 안된다. 순서가 없다는 점.
myset={4,1,3,2,3,3,3}
print(myset)

java={"a","B","C"}
python=set(["D","B"]) #리스트를 만들고 세트로 타입 캐스팅 가능

#교집합 출력하기
print(java &python)
print(java.intersection(python))

#합집합 출력하기
print(java or python) # 앞에있는 세트를 출력함. 합집합과 다름.
print(python or java) # 문자 or 와 |는 다르게 출력되는점!
print(java | python)
print(python.union(java))

#차집합
print(java - python)
print(java.difference(python))

#추가
python.add("Z")
print(python)

java.remove("C")
print(java)

#자료구조의 변경

menu={"커피","우유","주스"}
print(menu,type(menu))

menu=list(menu)
print(menu, type(menu))

menu=tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu,type(menu))


#quiz-4
#1명은 치킨 3명은 커피 쿠폰을 받는 추첨 프로그램
#조건1 댓글은 20개, 아이디는 1~20
#조건2 무작위 추첨 및 중복 x
#조건3 랜덤 모듈의 shuffle 과 sample활용

from random import *
lst=range(1,21) # 1부터 21직전까지
#해당 타입은 레인지 타입이다. 이를 리스트로 변환해줘야함.
print(lst)
print(type(lst))
lst = list(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
print(lst)
chicken=lst.pop()

print(chicken)
#lst.remove(chicken)
coffee=sample(lst,3)

print('--당첨자 발표 --')
print('치킨 당첨자 :',chicken)
print('커피 당첨자 :',coffee)
print('--축하합니다--')
#------------------------------
print('--당첨자 발표 --')
print('치킨 당첨자 : {0}' .format(chicken))
print('커피 당첨자 : {0}' .format(coffee))
print('--축하합니다--')


#if 

weather = "눈"
#weather = input("날씨를 입력하시오. : ") #input은 사용자 입력을 기다림.
if weather == "비" or weather == "눈" :
    print("우산을 챙기시오 ")
elif weather == "미세먼지" :
    print("미세먼지")
else :
    print("아무것도 아님")

#input은 스트링 형태로 값을 받기 때문에 상황에 맞는 타입 캐스팅이 필요함.

temp = 10
#temp  = int(input("기온이 몇도인가요?"))

if 30<= temp :
    print("너무 덥습니다.")
elif 10<=temp and temp <30 :
    print("날씨가 쾌적합니다.")
elif 0<=temp < 10 :
    print("매우 춥네요")
else :
    print("매우매우매우 춥스니다.")


#반복문

#기본적인 리스트 활용
# for watting_no in [0,1,2,3,4] :
for watting_no in range(1,6): #range 활용 1~5R까지
    print("대기번호 : {0}" .format(watting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starbucks :
    print("{0},커피가 준비되었습니다." .format(customer))

#while 반복문

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았엉요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

person = "unknown"
while person != customer :
    print("{0},커피가 준비되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요 ? ")

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

#함수
def open_account() :
    print("새로운 계좌가 생성됨.")

def deposit(balance, money):
    print("입금 완료. 잔액 {0}".format(balance + money))
    return balance+money

def withdraw(balance, money):
    if balance >= money : #잔액이 출금액보다 많으면
        print("출금 완료. 잔액 {0}.".format(balance-money))
        return balance - money
    else :
        print("잔액이 부족합니다. 잔액 {0}".format(balance))
        return balance

def withdraw_night(balance, money): #저녁출금
    commission = 500 #수수료 오백원
    return commission, balance - money - commission

balance = 12000 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 3000)
commission, balance = withdraw_night(balance, 2000)
print("수수료는 {0}원 이며, 잔액은 {1}원 입니다." .format(commission, balance))


#함수 기본값

def profile(name, age=17, main_lang="자바"): #변수에 값을 넣어두면 기본값을 된다. 특정값을 호출하지 않으면 지정된 기본값이 호출됨
    print("이름:{0} \t 나이:{1}\t 주 사용 언어:{2}" \
        .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("유재석")

#키워드값을 이요한 함수호출 -> 순서가 뒤바껴있어도 원하는대로 호출 가능함.
def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name="유재석", main_lang="파이썬",age=33)
profile2(main_lang="자바", age =24, name="김태호")

#가변인자

def profile3(name, age, lang1, lang2, lang3, lang4, lang5): #보통은 알맞는 인자 갯수에 맞춰서 넣어야함.
    print("이름:{0} \t 나이:{1}".format(name, age), end=" ") #end를 넣으면 줄바꿈이 일어나지 않는다.!
    print(lang1, lang2, lang3, lang4, lang5)

profile3("유재석", 20, "python", "java", "C", "C++", "C#")
profile3("김태호", 39, "kotlin", "Swift", "", "", "")#없더라도 빈칸이라도 나머지 3개의 인자 갯수를 맞춰줘야함 

#하지만 가변인자는 유연하게 작용가능

def profile4(name, age, *lang):
    print("이름:{0} \t 나이:{1}".format(name, age), end=" ") #end를 넣으면 줄바꿈이 일어나지 않는다.!
    for l in lang :
        print(l, end=" ")
    print() #줄 바꿈 용

profile4("유재석", 20, "python", "java", "C", "C++", "C#","Java Script")
profile4("김태호", 39, "kotlin", "Swift")

#지역 변수와 전역변수
gun = 10

def checkpoint(soldiers): 
    global gun #전역 공간에 있는 gun 사용 , 만일 글로벌을 써주지 않으면 지역변수로 판단하게됨
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))

def chekcpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
    return gun

print("전체 총 : {0} " .format(gun))
checkpoint(2) # 2명이 경계근무 나감
gun = chekcpoint_ret(gun, 3)
print("남은 총 : {0}".format(gun))


#quiz - 6
#표준 체중을 구하는 프로그램
# 공식 남자 : 키 x 키 x 22
#      여자 : 키 x 키 x 21

#조건 : 표준 체중은 별도의 함수 내에서 계산
#   *함수명 : std_weight
#   *전달값 : 키(height) 성별 (gender)
#조건2 : 표준 체중은 소수점 둘째자리까지 표시

height = int(input("키(cm)를 입력 하세요. : "))
gender = input("성별을 입력 하세요. (남자 or 여자) : ")
weight = 0

def std_weight(height, gender):
    global weight
    if gender == "남자":
        weight = ((height**2)*22)/10000
        
    elif gender == "여자":
        weight = (height**2)*21/10000

    else :
        print("잘못된 성별을 입력하셨습니다.")

std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, round(weight,2)))


