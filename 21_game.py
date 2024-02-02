import random
import time


while True:

    so_hien_tai = 1

    if random.randint(0, 1) == 0:
        nguoi_choi_hien_tai = "Người"
    else:
        nguoi_choi_hien_tai = "máy"

    while so_hien_tai <= 21:

        print("Số Hiện tại là:  " + str(so_hien_tai) + ".")
        print()

        if nguoi_choi_hien_tai == "Người":

            print("chọn số 1, 2, hoặc  3.")

            lua_chon_cua_nguoi_choi = ""
            while lua_chon_cua_nguoi_choi not in ["1", "2", "3"]:
                lua_chon_cua_nguoi_choi = input("bạn muốn chọn số nào ? ")

            lua_chon_cua_nguoi_choi = int(lua_chon_cua_nguoi_choi)
            so_hien_tai = so_hien_tai + lua_chon_cua_nguoi_choi
            print()

            if so_hien_tai >= 21:
                print("Số Hiện tại là: " + str(so_hien_tai) + ".")
                print()
                print("Bạn đã thua.")
                break
            nguoi_choi_hien_tai = "Máy"

        else:

            lua_chon_cua_may = random.randint(1, 3)
            so_hien_tai = so_hien_tai + lua_chon_cua_may
            print("Lượt chơi của máy. sự lựa chọn của máy là: " +
                  str(lua_chon_cua_may) + ".")
            print()
            time.sleep(1)

            if so_hien_tai >= 21:
                print("Số Hiện tại là: " + str(so_hien_tai) + ".")
                print()
                print("Bạn đã thắng!")
                break
            nguoi_choi_hien_tai = "Người"

    print()
    play_again = input("Bạn có muốn chơi lại không? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Tạm biệt")
        break