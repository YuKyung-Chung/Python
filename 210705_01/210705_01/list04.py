aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d" %(aa[-1], aa[-2]))

print(aa[0:2])
print(aa[2:4])
print(aa[0:])

bb = [30, 10, 20]
print("현재의 리스트: %s" %bb)

bb.append(40) #요소 하나 추가
print("append 후의 리스트: %s" %bb)

bb.pop() # stack 알고리즘 적용(마지막 1개 꺼낸다)
print("리스트에서 꺼낸 값 : %s" %bb)

bb.sort() #정렬 후에 출력
print("sort후의 리스트 : %s" %bb)

bb.reverse() #역순 정렬 후에 출력
print("reverse후의 리스트 : %s" %bb)

bb.insert(2,222) # 세 번째 위치에 222값을 추가
print("insert(2,222)후의 리스트 : %s" %bb)
print("20값의 위치: %d" %bb.index(20))

bb.remove(222) #222 요소 값을 리스트에서 삭제
print("remove(222) 후의 리스트 : %s" %bb)

bb.extend([77,88,77]) #리스트 확장
print("extend([77,88,77]) 후의 리스트 : %s" %bb)

print("77값의 개수: %d" %bb.count(77)) # 리스트에서 77 요소 값이 몇개 있는지 출력


