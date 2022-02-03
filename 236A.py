#enter the string
a=input()
#knowing how many distinct characters in the string
b=len(set(list(a)))
#excute the condition
print("CHAT WITH HER!") if b%2==0 else print("IGNORE HIM!")