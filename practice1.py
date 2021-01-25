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
