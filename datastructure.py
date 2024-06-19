class Stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def stackpop(self):
        return self.items.pop()
    def display(self):
        print(self.items)
    def top(self):
        return self.items[-1]
    def displayrev(self):
        print(self.items[::-1])
    def length(self):
        return len(self.items)

s=Stack()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.display()
s.stackpop()
s.stackpop()
s.display()
s.displayrev()
print(s.top())
print(s.length())
'''
e=input()
s=Stack()
ob="[{("
cb=")}]"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.stackpop()
        if x=="(" and i==")":
            pass  
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            break
if flag==0 and s.length()==0:
    print("valid")
else:
    print("invalid")
'''
#balncing the brackets in O(n2)
'''def balnce(n):
    l=''
    b="[](){}"
    for i in n:
        if i in b:
             l+=i
    print(l)
    if l[0]==")" or l[0]==']' or l[0]=='}':
        return "invalid"
    else:
        while '()' in  l or  '[]' in l or '{}' in l:
                l=l.replace('()',"").replace('[]',"").replace('{}',"")
        print(len(l))
        if len(l)==0:
            return "valid"
        else:
            return "invalid"
n="[4-6{235(9+6)]"
n1="[3+7{52/11(3+5)}]"
print(balnce(n))'''

'''#next greater element
n = [3, 5, 2, 14, 5, 3, 7, 9, 4, 2, 5, 3]
s=[]
l=[0]*len(n)
i=len(n)-1
while i>=0:
    while len(s)>0 and s[-1]<n[i]:
        s.pop()
    if len(s)==0:
        l[i]=-1
    else:
        l[i]=s[-1]
    s.append(n[i])
    i=i-1
print(l)'''

'''
#Queue
class Queue:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        return self.items.pop(0)
    def display(self):
        print(self.items)
    def revdisplay(self):
        print(self.items[::-1])
    def top(self):
        return self.items[0]
    def length(self):
        return len(self.items)
q=Queue()
q.push(1)
q.push(3)
q.push(4)
q.push(5)
q.display()
print(q.pop())
print(q.pop())
q.display()
print(q.top())
q.revdisplay()
print(q.length())
'''


#linked list
class LinkedList:
    def __init__(self,data):
        self.data=data
        self.next=None
class list:
    head=None
    tail=None
    size=0
    def insertf(self):
        data=int(input("enter the data: "))
        temp=LinkedList(data)
        if self.head==None:
            self.head=self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
        self.size+=1

    def inserte(self):
        data=int(input("enter the data: "))
        temp=LinkedList(data)
        if self.head==None:
            self.head=self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
        self.size+=1
    def deletef(self):
        if self.head==None:
            print("list is empthy")
        else:
            print(self.head.data)
            self.head=self.head.next
    def deleend(self):
        if self.head==None:
            print("list is empthy")
        elif self.head.next==None:
            self.head=None
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            print(curr.next.data)
            curr.next=None


    def display(self):
        if self.head==None:
            print("list is empthy")
        else:
            curr=self.head
            while curr!=None:
                print(curr.data,end=" ")
                curr=curr.next

l=list()
l.insertf()
l.insertf()
l.inserte()
l.inserte()
l.display()
l.deleend()
l.deletef()
l.display()
        


