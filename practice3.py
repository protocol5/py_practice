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