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


