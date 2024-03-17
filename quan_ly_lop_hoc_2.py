class SinhVien:
    def __init__(self, masv, ten, lop, diem):
        self.masv = masv
        self.ten = ten
        self.lop = lop
        self.diem = diem

    def __str__(self):
        return f"{self.masv} | {self.ten} | {self.lop} | {self.diem}"

class QuanLySinhVien:
    def __init__(self):
        self.ds_sinhvien = []

    def them_sinhvien(self, sv):
        self.ds_sinhvien.append(sv)

    def xoa_sinhvien(self, masv):
        self.ds_sinhvien = [sv for sv in self.ds_sinhvien if sv.masv != masv]

    def cap_nhat_sinhvien(self, masv, ten, lop, diem):
        sv = self.tim_sinhvien(masv)
        if sv:
            sv.ten = ten
            sv.lop = lop
            sv.diem = diem

    def tim_sinhvien(self, masv):
        for sv in self.ds_sinhvien:
            if sv.masv == masv:
                return sv
        return None

    def sap_xep_theo_ten(self):
        self.ds_sinhvien.sort(key=lambda sv: sv.ten)

    def sap_xep_theo_diem(self):
        self.ds_sinhvien.sort(key=lambda sv: sv.diem, reverse=True)

    def hien_thi_danh_sach(self):
        for sv in self.ds_sinhvien:
            print(sv)

# Khởi tạo hệ thống
ql_sinhvien = QuanLySinhVien()

# Thêm sinh viên
sv1 = SinhVien("12345", "Nguyễn Văn A", "K59", 8.5)
sv2 = SinhVien("54321", "Trần Thị B", "K60", 9.0)
ql_sinhvien.them_sinhvien(sv1)
ql_sinhvien.them_sinhvien(sv2)

# Hiển thị danh sách
print("Danh sách sinh viên:")
ql_sinhvien.hien_thi_danh_sach()

# Tìm kiếm sinh viên
masv = input("Nhập mã sinh viên cần tìm: ")
sv = ql_sinhvien.tim_sinhvien(masv)
if sv:
    print(f"Thông tin sinh viên {masv}:")
    print(sv)
else:
    print(f"Sinh viên có mã {masv} không tồn tại!")

# Cập nhật thông tin
masv = input("Nhập mã sinh viên cần cập nhật: ")
ten = input("Nhập tên mới: ")
lop = input("Nhập lớp mới: ")
diem = float(input("Nhập điểm mới: "))
ql_sinhvien.cap_nhat_sinhvien(masv, ten, lop, diem)

# Xóa sinh viên
masv = input("Nhập mã sinh viên cần xóa: ")
ql_sinhvien.xoa_sinhvien(masv)

# Sắp xếp và hiển thị
ql_sinhvien.sap_xep_theo_ten()
print("Danh sách sinh viên sau khi sắp xếp theo tên:")
ql_sinhvien.hien_thi_danh_sach()

ql_sinhvien.sap_xep_theo_diem()
print("Danh sách sinh viên sau khi sắp xếp theo điểm:")
ql_sinhvien.hien_thi_danh_sach()