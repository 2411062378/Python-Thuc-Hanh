import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)
print("Loại dữ liệu:", type(diem_list), type(diem_array))

diem_cong_them = diem_array + 0.5
print("Cộng bằng NumPy (vectorized):", diem_cong_them)

diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Cộng bằng List comprehension:", diem_cong_them_list)

print("Trung bình:", np.mean(diem_array))
print("Lớn nhất:", np.max(diem_array))
print("Nhỏ nhất:", np.min(diem_array))
print("Độ lệch chuẩn:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma trận:\n", ma_tran)
print("Kích thước (shape):", ma_tran.shape)
print("Ma trận nhân 2:\n", ma_tran * 2)