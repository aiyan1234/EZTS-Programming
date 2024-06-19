'''2) Ant on Rail 
There is a ant on your balcony.It wants to leave the rail so sometimes it moves right and 
sometimes it moves left until it gets exhausted.Given an integer array A of size N which 
consists of integer 1 and -1 only representing ant's moves. 
Where 1 means ant moved unit distance towards the right side and -1 means it moved unit 
distance towards the left .Your task is to find and return the integer value representing how 
many times the ant reaches back to original starting position. 
Note: 
• Assume 1-based indexing 
• Assume that the railing extends infinitely on the either sides
Input Format:
input1 : An integer value N representing the number of moves made by the ant. input2 : 
An integer array A consisting of the ant's moves towards either side Sample Input
5 
1 -1 1 -1 1 
Sample Output
2


def originalpos(arr):
    count=0
    currpos=0
    for i in arr:
        currpos+=i
        if currpos==0:
            count+=1
    return count


n=int(input())
arr=list(map(int,input().strip().split()))
print(originalpos(arr))
'''
'''#prime or not in efficient
m=int(input("enter the message:"))
flag=0
if m<0:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,(m//2)+1):
        if m%i==0:
            flag=1
            break
if flag==0:
    print("Valid message")
else:
    print("not a valid message")'''
'''
#fibbonacci series
n=int(input("enter the no of terms"))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(a,end=' ')
    print(b,end=' ')
else:
    print(a,end=' ')
    print(b,end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a,b=b,c'''
'''
#find the first prime of a number and than finding the sum between that number the first prime number and than finding the 2nd next prime number and if the product of two primes numbers is prime return true or false
def is_prime(n):
    if n < 1:
        return False
    elif n==1 or n==2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
def nextprime(m):
    l=[]
    nextnumber=m+1
    while len(l)<2:
        if is_prime(nextnumber):
            l.append(nextnumber)
        nextnumber+=1
    return l
def suminbtw(result,m):
    sum=0
    for i in range(m+1,result[0]):
        sum+=i
    result[1]=sum
    return result
m=int(input("enter the number: "))
result=nextprime(m)
pro=result[0]*result[1]
result=suminbtw(result,m)
result.append(is_prime(pro))
print(tuple(result))
'''
        

