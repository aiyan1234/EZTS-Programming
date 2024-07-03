'''Space counter 
You have been gives the task of making the counter on a social media platform more userfriendly.your task is to find and return an integer value representing the count of the number of 
spaces in a gives string S. 
Input: 
A string: 
Output: 
Return an integer value representing the count of the number of space in a given string S.'''
s=input("enter the string")

#method 1
#print(s.count(' '))

#method 2
c=0
for i in s:
    if i==' ':
        c+=1
print(c)