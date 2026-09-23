print("===== HOAT DONG 3 =====")

# for voi range()
for i in range(1, 6):
    print(i)
print("\nDuyet List:")
diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
    print("Diem:", diem)
print("\nDuyet Tuple:")
toa_do = (3, 5)
for gia_tri in toa_do:
    print(gia_tri)
print("\nDuyet Dictionary:")
diem_mon = {"Toan": 8.0, "Ly": 7.5}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)
print("\nDuyet String:")
ten = "Python"
for ky_tu in ten:
    print(ky_tu)

print("\n===== BANG CUU CHUONG =====")

n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("\n BAI 4.1 - GIAI THUA ")
n = 5
giai_thua = 1
i = 1
while i <= n:
    giai_thua = giai_thua * i
    i += 1
print(f"{n}! = {giai_thua}")

print("\n BAI 4.2 - TONG CHU SO ")

so = 4527
so_tam = so
tong_chu_so = 0
while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10
print(f"Tong cac chu so cua {so} la: {tong_chu_so}")