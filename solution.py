#Задача №1
def function1(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
function1(16)

#Задача №2
def funcrion2(a,b):
    return a * b

#Задача №3
def function3(x):
    if x > 0:
        return -abs(x)
    else:
        return x


#Задача №4
def function4(arr):
    return sum(x for x in arr if x > 0)

#Задача №5
def function5(string):
    return string(::-1)

#Задача №6
def function6(num):
    return str(num)

#Задача №7
def function7(arr):
    return sum(x*x for x in arr)

#Задача №8
def function8(string):
    if len(string) <= 2:
        return ''
    else:
        return string[1:-1]

#Задача №9 
def function9(x):
   return -x

#Задача №10
def function10(n,s):
    return str(s) * n 


#Задача №11
def function11(arr):
    arr.sort()
    return arr[0]

#Задача №12
def function12(x):
    return x * (x+1) // 2

#Задача №13
def function13(arr):
    return arr.replace(' ','')

#Задача №14
def function14(arr):
    return sum(arr) 

#Задача №15
def function15(string):
    return int(string) 

#Задача №16
def function16(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

#Задача №17
def function17(name):
    return '.'.join(w[0] for w in name.split()).upper()

#Задача №18
#import math
def function18(time):
    water = time * 0.5
    return math.floor(water) 

#Задача №19 
def function19(flow1,flow2):
    return (flow1 % 2) != (flow2 % 2)

#Задача №20 
#import math 
def function20(year):
    return math.ceil(year / 100)
#Задача №
#Задача №







