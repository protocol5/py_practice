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