
#for the given list of numbers finding the maximum frequency of digit and if maximum frequency tie than print the maximum digit 
n=[1237,262,666,148,777]
s=''
d={}
s=map(str,n)
s=''.join(s)
print(s)
maxdigit=[]
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxvalue=max(d.values())
for i in d:
    if d[i]==maxvalue:
        maxdigit.append(i)
print(maxdigit)
if len(maxdigit)>1:
    print(max(maxdigit))
else:
    print(maxdigit.pop())
print(d)


# performing the operation
s=["+",'-','%','*','//']
n="21*21"
op=[i for i in n if i in s]
print(op)
x=op.pop()
s=n.split(x)
print(s)
if x=="+":
    print(float(s[0])+float(s[1]))
elif x=='-':
        print(float(s[0])-float(s[1]))
elif x=='*':
        print(float(s[0])*float(s[1]))
elif x=='//':
        print(float(s[0])//float(n[1]))
elif x=='%':
        print(float(s[0])%float(n[1]))
                        
        
