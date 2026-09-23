print("===== BAI 5.1 - PASS =====")
diem = 6.5
if diem >= 8.0:
    pass
elif diem >= 5.0:
    print("Dat yeu cau")
else:
    pass

print("\n===== BAI 5.2 - BREAK =====")
so = 29
la_so_nguyen_to = True
if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break
print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")


print("\n===== BAI 5.3 =====")
n = 20
so_hien_tai = n + 1
while True:
    la_so_nguyen_to = True
    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        break
    so_hien_tai += 1
print(f"So nguyen to dau tien lon hon {n} la: {so_hien_tai}")


print("\n===== BAI 5.4 - CONTINUE =====")
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue
    danh_sach_hop_le.append(so)
print("Cac so hop le (duong):", danh_sach_hop_le)


print("\n===== BAI 6.1 - TAM GIAC SAO =====")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


print("\n BAI 6.2 - HINH THOI SAO ")
n = 4
# Nua tren
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Nua duoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))