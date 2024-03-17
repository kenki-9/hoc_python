class Student:
    def __init__(self, ma_sv, ho_ten, ngay_sinh, que_quan, chuyen_nganh, lop):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan
        self.chuyen_nganh = chuyen_nganh
        self.lop = lop

    def __str__(self):
        return f"MSSV: {self.ma_sv}\nHọ tên: {self.ho_ten}\nNgày sinh: {self.ngay_sinh}\nQuê quán: {self.que_quan}\nChuyên ngành: {self.chuyen_nganh}\nLớp: {self.lop}"

class Student_List:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, ma_sv, new_info):
        for student in self.students:
            if student.ma_sv == ma_sv:
                for key, value in new_info.items():
                    setattr(student, key, value)
                return True
        return False

    def delete_student(self, ma_sv):
        for student in self.students:
            if student.ma_sv == ma_sv:
                self.students.remove(student)
                return True
        return False

    def search_student(self, keyword):
        result = []
        for student in self.students:
            if keyword in student.ma_sv or keyword in student.ho_ten:
                result.append(student)
        return result

    def sort_student(self, key):
        self.students.sort(key=lambda student: getattr(student, key))

    def print_all(self):
        for student in self.students:
            print(student)

student_list = Student_List()

# Thêm sinh viên mới
student1 = Student("123456", "Nguyễn Văn A", "01/01/2000", "Hà Nội", "Công nghệ thông tin", "K62")
student2 = Student("654321", "Trần Thị B", "02/02/2001", "TP. Hồ Chí Minh", "Kinh tế", "K63")
student_list.add_student(student1)
student_list.add_student(student2)

# Cập nhật thông tin sinh viên
student_list.update_student("123456", {"ho_ten": "Nguyễn Văn A1"})

# Xóa sinh viên
student_list.delete_student("654321")

# Tìm kiếm sinh viên
result = student_list.search_student("A")

# Sắp xếp sinh viên theo mã sinh viên
student_list.sort_student("ma_sv")

# In danh sách sinh viên
student_list.print_all()