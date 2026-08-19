
print("========== HOAT DONG 3 ==========")

# Bai 3.1 - Soi loi dat ten
print("\n--- Bai 3.1 ---")

print("1diem: Sai - bat dau bang chu so")
print("gia-tri: Sai - co dau '-'")
print("_tam_thoi: Hop le")
print("Diem_TB: Hop le, nhung chua dung PEP8 cho bien")
print("class: Sai - la tu khoa Python")
print("so luong: Sai - co khoang trang")
print("MAX_SPEED: Hop le, phu hop cach dat ten hang so")
print("diemTB: Hop le, nhung PEP8 nen viet diem_tb")
print("2024_data: Sai - bat dau bang chu so")
print("tong$: Sai - co ky tu $")
print("sinhVien1: Hop le, nhung PEP8 nen viet sinh_vien1")


# Bai 3.2 - Ap dung PEP8
print("\n--- Bai 3.2 ---")

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2

MUC_LUONG_TOI_THIEU = 5000000

print("Ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)



print("\n========== HOAT DONG 5 ==========")

# Bai 5.1 - Toan tu so hoc
print("\n--- Bai 5.1 ---")

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# Bai 5.2 - So sanh va logic
print("\n--- Bai 5.2 ---")

diem = 6.5
tuoi = 20

la_kha = diem >= 6.5 and diem < 8.0
tuoi_khong_phu_hop = tuoi < 18 or tuoi > 60
phu_dinh = not (tuoi < 18 or tuoi > 60)

print("Diem dat loai Kha?", la_kha)
print("Tuoi chua du 18 hoac tren 60?", tuoi_khong_phu_hop)
print("Phu dinh dieu kien tren:", phu_dinh)


# Bai 5.3 - Toan tu gan va toan tu dac biet
print("\n--- Bai 5.3 ---")

x = 10
print("x ban dau =", x)

x += 5
print("Sau x += 5:", x)

# De bai khong quy dinh so cu the cho cac phep gan tiep theo,
# cac gia tri duoi day duoc chon de minh hoa.
x -= 3
print("Sau x -= 3:", x)

x *= 2
print("Sau x *= 2:", x)

x /= 4
print("Sau x /= 4:", x)

x //= 2
print("Sau x //= 2:", x)

x **= 2
print("Sau x **= 2:", x)

danh_sach = [1, 2, 3, "python"]

print("3 co trong danh_sach?", 3 in danh_sach)

danh_sach_2 = danh_sach

print(
    "Hai bien co cung tham chieu mot list?",
    danh_sach_2 is danh_sach
)


# Bai 5.4 - Do uu tien toan tu
print("\n--- Bai 5.4 ---")

print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("(2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)
print(
    "10 > 5 and 3 < 1 or not False =",
    10 > 5 and 3 < 1 or not False
)




print("\n========== HOAT DONG 6 ==========")

# Bai 6.1
print("\n--- Bai 6.1 ---")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))


# Bai 6.2
print("\n--- Bai 6.2 ---")

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))