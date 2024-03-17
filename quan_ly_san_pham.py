def get_product_info(products_db, prod_id):

  if prod_id in products_db:
    return products_db[prod_id]
  else:
    return None

def update_product_list(products_db, prod_id, new_name):

  products_db[prod_id] = new_name

# Khởi tạo danh sách sản phẩm
products_db = {}

# In danh sách sản phẩm hiện tại
print("Danh sách sản phẩm hiện tại:")
print(products_db)

# Bắt đầu vòng lặp
while True:
  # In ra các lựa chọn
  print("\nChọn chức năng bạn muốn thực hiện:")
  print("1. Thêm sản phẩm mới")
  print("2. Cập nhật sản phẩm")
  print("3. Xóa sản phẩm")
  print("4. Thoát khỏi ứng dụng")

  # Lấy lựa chọn của người dùng
  option = int(input())

  # Xử lý lựa chọn
  if option == 1:
    # Thêm sản phẩm mới
    product_id = int(input("Nhập id sản phẩm: "))
    product_info = get_product_info(products_db, product_id)
    if product_info is not None:
      print("Sản phẩm đã tồn tại với id", product_id)
    else:
      product_name = input("Nhập tên sản phẩm: ")
      update_product_list(products_db, product_id, product_name)
      print("Thêm sản phẩm thành công")

  elif option == 2:
    # Cập nhật sản phẩm
    product_id = int(input("Nhập id sản phẩm: "))
    product_info = get_product_info(products_db, product_id)
    if product_info is not None:
      product_name = input("Nhập tên mới cho sản phẩm: ")
      update_product_list(products_db, product_id, product_name)
      print("Cập nhật sản phẩm thành công")
    else:
      print("Sản phẩm không tồn tại với id", product_id)

  elif option == 3:
    # Xóa sản phẩm
    product_id = int(input("Nhập id sản phẩm: "))
    product_info = get_product_info(products_db, product_id)
    if product_info is not None:
      del products_db[product_id]
      print("Xóa sản phẩm thành công")
    else:
      print("Sản phẩm không tồn tại với id", product_id)

  elif option == 4:
    # Thoát khỏi ứng dụng
    break

  else:
    # Lựa chọn không hợp lệ
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

# In danh sách sản phẩm sau khi quản lý
print("\nDanh sách sản phẩm sau khi quản lý:")
print(products_db)