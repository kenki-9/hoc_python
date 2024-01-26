import turtle
shape=input("vuông hoặc tròn, nhập vào hình muốn vẽ: ")

if shape == "square" or shape == "circle" :

    color=input("vàng , đỏ hoặc xanh hãy chọn màu của bạn: ")

    if color== "red" or color == "yellow" or color == "green":
            wn = turtle.Screen()
            wn.bgcolor("black")
            wn.title("hình của bạn")

            hinh=turtle.Turtle()
            hinh.shape(shape)
            hinh.color(color)

    else: print("xin lỗi chúng tôi không có màu này")
else:
    print("xin lỗi tôi không thể vẽ hình này")



turtle.done()