a=input("write dr or rd     rd=radian and dr=dgree")
if a=='dr':
    b=float(input("enter dgree"))
    p=3.14
    c=b*p/180
    print(f"in radian = {c}")
if a=='rd':
    b=float(input("enter radian"))
    p=3.14
    c=b*180/p
    print(f"in dgree is {c}")


