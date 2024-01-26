# Nhập vào thứ  trong tuần
thu = int(input("Nhập vào thứ : "))

# Kiểm tra và in ra sự kiện tương ứng

    
if 2 <= thu <= 6:
    print("Hôm nay làm việc.")
elif thu == "7":
    print("Hôm nay đi chơi.")
elif 8 < thu  or thu < 2:
    print("xin hãy nhập vào thứ hợp lệ")
else:
    print("Hôm nay nghỉ ngơi.")
