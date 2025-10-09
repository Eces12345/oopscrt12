a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("{}is large".format(a))
elif b>a and b>c:
    print("{}is large".format(b))
else:
    print("{}is large".format(c))

