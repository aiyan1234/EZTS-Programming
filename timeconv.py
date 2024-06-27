def timeConversion(s):
    # Write your code here
    if s.endswith("PM"):
        m=s[:-2]
        if m.startswith("12"):
            print(m)
        else:
            x=m[:2]
            z=str(int(x)+12)
            m=m.replace(m[:2], z)
            print(m)
    elif s.endswith("AM"):
        m=s[:-2]
        if m.startswith("12"):
            x=m[:2]
            z="00"
            m=m.replace(m[:2],z)
            print(m)
        else:
            print(m)
                    
s = input("enter the time: ")

timeConversion(s)
'''def timeConversion(s):
    if s.endswith("PM"):
        m = s[:-2]
        if m.startswith("12"):
            return m
        else:
            x = m[:2]
            z = str(int(x) + 12)
            m = m.replace(m[:2], z, 1)
            return m
    elif s.endswith("AM"):
        m = s[:-2]
        if m.startswith("12"):
            x = m[:2]
            z = "00"
            m = m.replace(m[:2], z, 1)
            return m
        else:
            return m

s = input("Enter the time: ")
converted_time = timeConversion(s)
print("Converted time:", converted_time)
'''