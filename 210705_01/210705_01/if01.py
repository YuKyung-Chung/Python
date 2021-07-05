number = int(input('숫자를 입력하세요 : '))
if number < 50 :
	print('50보다 작은 값 입니다.')
else :
	print('50 이상인 값 입니다.')
	 
for i in range(0, 5, 1): #for문 선언 변수 i의 초기값은 0이고 범위는 5이고 1씩 증가
	print(i)		  	 # 세로로 출력
print("--------------")

for i in range(0, 5, 1): #end=' ' 추가하면 가로로 출력
	print(i, end=' ')
print("--------------")

for j in [1,3,5,7,9]: #for문 처리할 목록에는 리스트 변수 선언
	print(j)
print("--------------")

for j in [1,3,5,7,9]:
	print(j, end=' ')
print("--------------")

for k in range(0, 3, 1):
	print("꿈은 이루어 진다.")

#for문 이용하여 1에서 10까지의 합 구하기
sum = 0
for i in range(1, 11, 1):
	sum += i
print("sum : %d" %sum)
print("--------------")

#for문 이용하여 1에서 10까지 식과 합 구하기
sum = 0
for i in range(1, 11, 1):
	if i<10:
		print("%d +" %i, end = ' ')
	elif i == 10:
		print("%d = " %i, end = ' ')
	sum += i
print("%d" %sum)

str = "꿈은 이루어진다."
i = 0
while i<3:
	print(str)
	i = i + 1
print("-------------------------")

#while문으로 입력한 숫자만큼 str 반복 출력하기
i =int(input("반복 횟수 숫자를 입력 : "))
j = 1
flag =True
while flag:
	j = j + 1
	if i < j:
		flag = False
	print(str)

#break문
#for문과 break문을 이용하여 1에서 20까지 합이 100보다 가장 가깝고 작은 합을 구하시오
sum, i = 0, 0
for i in range(1, 20, 1):
	sum += i
	if sum > 100:
		break;
sum -= i
print("%d" %sum)
print("----------------")

#while문과 break문을 이용하여 입력한 1에서 숫자만큼 합을 구하시오
sum, i = 0, 0
j = int(input("숫자를 입력합니다: "))
while True:
	if i<j:
		i = i + 1
		sum += i;
	elif i == j:
		break
print("1에서 %d까지의 합은 %d입니다." %(j, sum))
