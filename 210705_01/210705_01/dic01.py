# 딕셔너리 타입 변수 선언
dict = {'번호':10, '성명':'김태희', '나이':23, '사는곳':'서울'}
print(dict)
print(type(dict))

print(dict['나이'])   # 나이 key값으로 value값 출력
dict['나이'] = 24     # 나이 키 값 항목 변경
print(dict['나이'])

dict['직업'] = '배우' # 직업이라는 key값과 배우라는 value 항목 추가
print(dict)

print(dict.keys())	  # 키 값 전체 반환
print(dict.values())  # 값 전체 반환

print('사는곳' in dict) # 키 값 존재 여부 확인
del dict['사는곳']		# 키 값 삭제
print('사는곳' in dict) #dict에 사는곳이라는 키 값 존재 여부 출력
print(dict)