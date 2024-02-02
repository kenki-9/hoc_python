
so_bat_dau = int(input("nhập vào khoảng bắt đầu: "))
so_ket_thuc = int(input("nhập vào khoảng kết thúc: "))


if so_ket_thuc <= so_bat_dau:
    print("Số kết thúc cần lớn hơn số bắt đầu.")
else:

    for num in range(so_bat_dau, so_ket_thuc + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
