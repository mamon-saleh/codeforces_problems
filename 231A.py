#input the num of the problems
a=int(input())
k=0
for i in range(a):
    #input each girl solution 
    b=map(int,input().split())
    #check of the sum is greater than one
    if sum(b)>1:
        k+=1
print(k)