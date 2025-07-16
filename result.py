a=float(input("enter the marks for subject a:"))
b=float(input("enter the marks for subject b:"))
c=float(input("enter the marks for subject c:"))
d=float(input("enter the marks for subject d:"))
e=float(input("enter the marks for subject e:"))



total=a+b+c+d+e
per=(total/500)*100

if  per>90:
    print("A")

elif per>80:
    print("B")
    
elif per>70:
    print("C")
    
elif per>60:
    print("D")
    
elif per>50:
    print("E")
    
else:
    print("Fail")