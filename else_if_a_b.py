a = float(input("a= "))
b = float(input("b= "))
c = -b/a

if a == 0:
    if b == 0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem: ",c)