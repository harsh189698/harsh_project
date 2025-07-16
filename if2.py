a=int(input())
b=int(input())
c=int(input())      

if a==b and a==c:
    print("a b c are same")
elif a==b:
    print("a b both are same")
elif a==c:
    print("a c both are same")
elif a>b and a>c:
    print("a is a big")
elif b>c and b>a:
    print("b is a big")
elif c>a and c>b:
    print("c is a big")
else:
    print("invalid..!")

