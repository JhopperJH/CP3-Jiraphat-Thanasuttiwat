num = int(input())
result = "*"
for x in range(num):
    num -= 1
    print((" " * num) + result)
    result += "**"

'''
def Mstair(step, char='*'):
    for i in range(1, step+1):
        print(" "*(step-i) + char*(2*i-1))
Mstair(num)
'''