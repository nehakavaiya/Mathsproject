print("welcome to determinant sum solve ")
d=int(input("if you use 2x2 determinant then enter'2'and if you use 3x3 determinant then enter'3'="))
if d==2:
    def determinant(a1,b1,a2,b2):
        print("2x2 Determinant is ",a1*b2-b1*a2)
    a1=int(input("enter a1="))
    b1=int(input("enter b1="))
    a2=int(input("enter a2="))
    b2=int(input("enter b2="))
    determinant(a1,b1,a2,b2,)

elif d==3:
    def determinant(a1,b1,c1,a2,b2,c2,a3,b3,c3):
        a=b2*c3-c2*b3
        b=a2*c3-c2*a3
        c=a2*b3-b2*a3

        print("3x3 Diterminant is ",a1*a-(b1*b)+c1*c)
    a1=int(input("enter a1="))
    b1=int(input("enter b1="))
    c1=int(input("enter c1="))
    a2=int(input("enter a2="))
    b2=int(input("enter b2="))
    c2=int(input("enter c2="))
    a3=int(input("enter a3="))
    b3=int(input("enter b3="))
    c3=int(input("enter c3="))
    determinant(a1,b1,c1,a2,b2,c2,a3,b3,c3)