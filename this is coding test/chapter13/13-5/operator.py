from itertools import permutations
def calculator(op,num1,num2):
    if op=="+":
        return num1+num2
    
    elif op=="-":
        return num1-num2
    
    elif op=="*":
        return num1*num2
    
    elif op=="%":
        if num1<0 and num2>0:
            return -((-num1)//num2)
        return num1//num2


n=int(input())
numbers=list(map(int,input().split()))

operators=list(map(int,input().split()))

kindofoperators=["+","-","*","%"]
operlist=[]

for i in range(4):
    for j in range(operators[i]):
        operlist.append(kindofoperators[i])

operlist2=list(permutations(operlist,n-1))

maxnum=-(1e9)
minnum=(1e9)

for opers in operlist2:
    result=numbers[0]
    for i in range(1,n):
         result=+calculator(opers[i-1],result,numbers[i])
    
    maxnum=max(maxnum,result)
    minnum=min(minnum,result)


print(maxnum)
print(minnum)

#python3 로 제출하니 시간초과가 나서 pypy3로 돌리니 성공을 했다. 
#찾아보니 python3가 함수호출이 느린편이라는 말이 있어서 함수부분을지우고 다시 해보기로 했다.