print("---------------------------------CALCULATOR--------------------------------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
d='y'
while d=='y' or d=='Y':
    ch=int(input("Enter choice to perform arithmetic calculation:"))
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    if ch==1:
        c=a+b
        print(a,"+",b,"=",c)
    elif ch==2:
        c=a-b
        print(a,"-",b,"=",c)
    elif ch==3:
        c=a*b
        print(a,"*",b,"=",c)
    elif ch==4:
        c=a/b
        print(a,"/",b,"=",c)
    else:
        print("Invalid Choice")
    d=input("Do you need to perform more arithmetic operation(y/n):")
