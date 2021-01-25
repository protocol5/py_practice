#표준 입출력
print("python","java")
print("pyhton","java", sep="vs",end="?")#sep 을통해 컴마를 띄어쓰기로 할지 붙여쓸지 정할 수 있음.
print("end를 통해 한줄로 붙여 쓰게함")
#end를 통해서는 한줄로 출력하게 만듬

import sys

print("python -> standard output", file=sys.stdout)
print("python -> logging data error",file= sys.stderr) 

scores= { "수학":0, "영어":50, "코딩":100}
for subjecet, score in scores.items(): #items()를통해 딕셔너리의 키값과 벨류값을 튜플로 리턴시킴.
    #print(subjecet, score)
    print(subjecet.ljust(8), str(score).rjust(4),sep=":") 
    #.ljust(8)는 왼쪽으로 8칸을 띄어서 정렬하라는 의미임.
    #socre는 int 타입이므로 스트링 타입으로 바꾼후 우측 4칸 정렬.
    #sep을 통해 ,컴마를 통해 생긴 공백을 지우고 대신 콜론을 집어넣음

#은행 순번 대기표 001, 002, 003...
#for num in range (1,21):
#    print("대기번호:"+ str(num).zfill(3)) #zfill은 문자열에서 나머지 부분을 ()안 숫자만큼 0으로 채워주는 기능을 한다. 

#표준입력

#answer = input("표준입력은 input으로 입력 대기")
#이때 input값이 담기는 answer는 항상 하 앙상 스트링형태다

#다양한 출력포맷
print("{0: >10}".format(500))#해석 스페이스바는 빈공간으로, >오른쪽으로, 10칸 띄어서 정렬
#양수일 땐 +로표시, 음수일 떈, -로 표시
print("{0: >+10}" .format(500)) #첫번째와 차이는 부호를 붙여야지만 양수 값에도 +가 붙어서 출력됨
print("{0: >-10}" .format(500)) #이건 그냥 500만 출력됨
print("{0: >+10}" .format(-500))

#왼쪽 정렬하고, 빈칸 _로 채움
print("{0:_<+10}" .format(500))

#3자리마다 콤마 찍기
print("{0:,}".format(1000000000))

#3자리마다 콤마 찍고, +-부호도 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

#3자리 마다 콤마 찍고, 부호붙이고, 자릿수 확보 ->30자리 자리 확보, 왼쪽 정렬, 빈공간 ^으로 표기
print("{0:^<+30,}".format(1000000000)) 

#소수점 출력
print("{0:}".format(5/3))#1.66666666666667
print("{0:f}".format(5/3))#1.666667
print("{0:.2f}".format(5/3))#1.67

# #파일입출력
# score_file = open("score.txt", "w", encoding="utf8") #utf8을 통해 한글 유니코드를 읽을 수 있게 해줌.
# #위의 w옵션은 덮어쓰기임.
# print("수학 : 0", file = score_file)
# print("영어 : 0", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding = "utf8") #a옵션은 append 즉, 이어쓰기임.
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") #print구문으로 글을 쓸때는, 자동으로 줄바꿈이 되지만 write로 쓰면 줄바꿈을 명시해줘야함
# score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file.close()

# print(score_file.readline())#줄별 읽기, 한 줄 일고 커서는 다음 줄로 이동
# print(score_file.readline(), end = "") #줄바꿈 x
# print(score_file.readline())

# #반복문으로 라인단위로 읽어오기
# while True :
#     line = score_file.readline()
#     if not line: #line에 내용이 없다면 탈출
#         break 
#     print(line, end = "")
    
# #리스트에 담아서 처리하기

lines = score_file.readlines() #파일의 모든내용을 가져와서 라인별로 list형태로 저장함
for line in lines:
    print()
    
score_file.close()
