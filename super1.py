#sending zeros at last without using extra space in O(n) tc
n=[4,5,0,1,2,0,0,6]
j=0
for i in range(len(n)):
    if n[i]!=0:
        n[j]=n[i]
        j=j+1
print(n)
while j<len(n):
    n[j]=0
    j=j+1
print(n)


#max repe vowel in string
v={'a','A','e','E','i','I','O','o','U','u'}
l=[]
s="Helloworldeoooeee"
for i in s:
    if i in v:
        l.append(i)
print(l)
count=0
uniq=[]
for i in range(len(l)):
    if i not in uniq:
        x=l.count(i)
        count=max(count,x)
        ch=l[i]
print(ch)

#maximum count including if max count is repeated
l=[1,2,3,2,3,1,2,1,1,1,2,2,3,3,3,4,4,3,2,1,1]
d={}
m=[]
for i in l:
    if i not in m:
        m.append(i)
        d[i]=l.count(i)
maxi=[]
print(d)
maxvalue=max(d.values())
#print(ele)
for i in d:
    if d[i]==maxvalue:
        maxi.append(i)

if len(maxi)>1:
    print(-1)
    print(maxi)
else:
    print(maxi.pop())

#maximum count
l=[1,2,2,3,5,6,4,3,3,4,4]
candiate=None
for i in l:
    count=0
    if count==0:
        candiate=i
    else:
        [count+1 if i==candiate else -1]
print(candiate)


#file usage
with open("ronaldo.txt",'w') as f:
    f.write("Aiyan")
    f.write(" speed")

with open("ronaldo.txt",'a') as f:
    f.write(" Hello")
    f.write(" boy")

with open("ronaldo.txt",'r') as f:
    z=f.read()  
    print(z)
z=z.replace("Hello","Bye")
with open("ronaldo.txt",'a') as f:
    f.write(z)  

with open("ronaldo.txt",'r') as f:
    print(f.tell())
with open("ronaldo.txt",'r+b') as f:
    f.seek(-35,2)
    f.write(b'i am coder   ')
    print(f.read().decode('utf-8'))
    f.close()

#power of two number
def power(number,exp):
    if exp==0:
        return 1
    else:
        return number*power(number,exp-1)
print(power(5,3))

#strip usage
s="  Hello world     ree   "
print(s.lstrip())
print(s.rstrip())
print(s.strip())

#simple oops usage
class Student:
    def __init__(self,usn):
        self.usn=usn
    def details(self):
        print(f"enter the details of {self.usn}")
        self.name=input("enter the name: ")
        self.m1=int(input("enter the marks1: "))
        self.m2=int(input("enter the marks2: "))
        self.m3=int(input("enter the marks3: "))
        self.m4=int(input("enter the marks4: "))
    def print(self):
        self.details()
        print("------------------------------------------------------------------")
        print(f" Name : {self.name}\n Usn : {self.usn}\n Marks1 : {self.m1}\n Marks2 : {self.m2}\n Marks3 : {self.m3}\n Marks1 : {self.m4}")
        per=((self.m1+self.m2+self.m3+self.m4)/400)*100
        if per>100:
            print(f"Percentage : {per} % \n Report : Human by this Intelligence Does not exist \n {self.name} is not human She is a an Alien",chr(0x1F632),chr(0x1F633),chr(0x1F975),chr(0x1F525))
        elif per>=90:
            print(per,'%',"Best")
        elif per<90 and per>75:
            print(per,'%',"Average")
        else:
            print(per,'%',"poor")
        print("-----------------------------------------------------------------")
n=int(input("enter the number of students:"))
for i in range(n):
    s=input(f"enter the usn of student {i+1}:")
    c=Student(s)
    c.print()




