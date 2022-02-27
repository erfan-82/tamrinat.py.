a=int(input("hi dear please tell me anumber?"))
b=int(input("hi dear please tell me anumber?"))
c=int(input("hi dear please tell me anumber?"))
if (a<b)and(a<c):
    print(f"the least number is {a}")
if (b<a)and(b<c):
    print(f"the least number is {b}")
if (c<a)and(c<b):
    print(f"the least number is {b}")
else:
    print("this is not the least number.....")