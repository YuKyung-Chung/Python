# 문자열과 튜플 타입 관계
str = "파이썬 문자열"
print(str[0])   # 첫 번째 자리의 문자 출력
print(str[-1])  # 뒤에서 첫 번째 자리의 문자 출력
#str[-1] = '렬' # 뒤에서 첫 번째 자리의 문자값 수정할 수 없음(튜플이라서)

card = 'red', 4, 'python', True    # 튜플 선언
#card = ['red', 4, 'python', True] # List 선언

print(card)		# card 튜플 전체 출력
print(card[1])  # card 튜플의 첫 번째 요소 출력
#card[0] = 'blue' # card 튜플 첫 번째 요소 값 수정할 수 없음(튜플이라서)
