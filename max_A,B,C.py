# Nhập giá trị của A, B, và C
A = float(input("Nhập giá trị của A: "))
B = float(input("Nhập giá trị của B: "))
C = float(input("Nhập giá trị của C: "))

# Xác định giá trị lớn nhất
lon_nhat = max(A, B, C)

# In kết quả
if lon_nhat == A:
    print("A là số lớn nhất.")
elif lon_nhat == B:
    print("B là số lớn nhất.")
else:
    print("C là số lớn nhất.")
