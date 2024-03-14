def them(expenses, item):
    expenses.append(item)


def tim(expenses, item_name):
    result = -1
    length = len(expenses)
    for i in range(length):
        if expenses[i]['name'] == item_name:
            result = i
    return result


def xoa(expenses, item_name):
    index = tim(expenses, item_name)
    if index > -1:
        del expenses[index]
    else:
        print(item_name + " không có trong danh sách chi tiêu")


expenses = []

while True:
    print("chi tiêu của bạn l :", expenses)
    print("bạn muốn làm gì ? -\n"\
          "1. thêm\n" \
          "2. xóa")
    option = int(input(" 1 hoặc 2: "))

    name_input = input("tên vật phẩm: ")

    if option == 1:
        cost_input = int(input("giá vật phẩm: "))
        date_input = input("ngày: ")
        item = {'tên': name_input, 'giá': cost_input, 'ngày': date_input}
        them(expenses, item)
        print("chi tiêu cu bạn là: ", expenses)
    elif option == 2:
        xoa(expenses, name_input)
        print("chi tiêu cu bạn là: ", expenses)
    else:
        print("Invalid input")
    if option == 0:
        break

print("Goodbye!")