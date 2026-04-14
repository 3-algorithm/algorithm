L=int(input())
a=input()

sum=0

for i,char in enumerate(a):
    sum+=(ord(char)-96)*31**i
print((sum%1234567891))