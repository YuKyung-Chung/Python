Variable = 100
Variable = "문자"

print(Variable)
print("%s" %Variable)
a = type(Variable)
print(a)

print("Variable의 Type : %s" % type(Variable))

a, b, c, d = 100, "apple", 3.14, 'melon'
print("a의 Value: %d" %a)
print("a의 Type:  %s" %type(a))

print("b의 Value: %s" %b)
print("b의 Type:  %s" %type(b))

print("c의 Value: %f" %c)
print("c의 Type:  %s" %type(c))

print("d의 Value: %s" %d)
print("d의 Type:  %s" %type(d))

aList = [100, 200, 300, 400] # C#의 경우 int[4]
print('aList : %d,%d,%d,%d' %(aList[0], aList[1], aList[2], aList[3]));