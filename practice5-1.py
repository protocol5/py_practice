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