Money = float(input("Nhập số tiền bạn đã chi tại cửa hàng là: "))

payment = 0

if Money < 75:

    payment = Money
elif Money < 100:
    payment = Money - 15
elif Money < 150:
    payment = Money - 25
else:
    payment = Money - 50
print("Tổng số tiền phải thanh toán là: ", payment)
