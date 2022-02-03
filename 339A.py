#enter the input as a list 
a=list(input())
c=[]
#for each odd number index in the list append it to another list
for i in range(len(a)):
    if i%2==1:
        continue
    else:
        c.append(a[i])
#sort this list
c.sort()
k=[]
#for each element in the length-1 of the previous list append the value with "+"
for j in range(len(c)-1):
    if len(c)==1:
        print(c[0])
        break
    k.append(str(c[j]))
    k.append("+")
#append the last element without "+"
k.append(c[-1])
#print the join of each element in the list
print("".join(k))

