#enter the number of lines
a=int(input())
X=0
for i in range(a):
    c=input()
    #for each element in the line check if there "+" or "-"
    for j in c:
        if j=="+":
            X+=1
            break
        if j=="-":
            X-=1
            break
print(X)