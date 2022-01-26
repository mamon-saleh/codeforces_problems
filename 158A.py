#enter the len of the list and the num of the list that will go to the next round
a,b=map(int,input().split())
#enter the list 
c= list(map(int,input().split()))
#check if the b element is zero 
if c[b-1]==0 :
    #filter the list of the zeros 
    c=list(filter((0).__ne__,c))
    #print the remaine of the list
    print(len(c))
else :
    #find the b element of the list
    k=c[b-1]
    #delete all of the element from the first one to the b element
    del c[0:b-1]
    #count then print the remain 
    j=c.count(k)
    print(str(b-1+j))