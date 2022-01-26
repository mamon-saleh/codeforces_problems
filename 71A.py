#input the num of inputs
a=int(input())
for i in range(a):
    #check if the len of the word is longer than 10 letters 
    # then print the first letter then the lenghth mines two then the last letters
    b=str(input())
    print(b[1]+(len(b)-2) + b[-1]) if len(b)>10 else print(b)
    
