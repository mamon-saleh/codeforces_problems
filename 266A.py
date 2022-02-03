#Enter the number of the letters and the letters
a = int(input())
b = (list(input()))
c=0
#for each element in the letters check if there are two identical letters in a row
for i in range(len(b) - 1):
    if b[i] == b[i + 1]:
        c+=1
print(0+c)