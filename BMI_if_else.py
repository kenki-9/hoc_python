
can_nang_kg = float(input("Nhập cân nặng (kg): "))
chieu_cao_m = float(input("Nhập chiều cao(m): "))

BMI = can_nang_kg / (chieu_cao_m ** 2)

print("Chỉ số BMI của bạn là:", BMI)

if BMI < 16:
    print("Gầy cấp độ III")
elif 16 <= BMI < 17:
    print("Gầy cấp độ II")
elif 17 <= BMI < 18.5:
    print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
    print("Bình thường")
elif 25 <= BMI < 30:
    print("Thừa cân")
elif 30 <= BMI < 35:
    print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")
