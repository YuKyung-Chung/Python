def mydef01():					# 인수 없는 함수 선언
	print("함수를 선언합니다.") # 들여쓰기를 통해 함수 구현 부분
mydef01()						# 함수 호출

def mydef02(str="인수함수를 선언합니다."): # 인수 있는 함수 선언
	print(str)							   # 인수로 받은 변수를 출력
mydef02()
mydef02("인수를 넣습니다.")
