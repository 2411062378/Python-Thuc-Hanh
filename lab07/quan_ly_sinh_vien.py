danh_sach_sinh_vien = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Nguyen Van An",
        "lop": "DH14C5",
        "diem": 8.0
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "lop": "DH14C5",
        "diem": 7.5
    }
]


def hien_thi_danh_sach():
    print("\n" + "=" * 60)
    print(f"{'Ma SV':<10}{'Ho ten':<25}{'Lop':<12}{'Diem':<10}")
    print("-" * 60)

    if len(danh_sach_sinh_vien) == 0:
        print("Danh sach sinh vien dang rong.")
        return

    for sv in danh_sach_sinh_vien:
        print(
            f"{sv['ma_sv']:<10}"
            f"{sv['ho_ten']:<25}"
            f"{sv['lop']:<12}"
            f"{sv['diem']:<10}"
        )

    print("=" * 60)


def tim_sinh_vien_theo_ma(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None


def nhap_diem(loi_nhac):
    while True:
        try:
            diem = float(input(loi_nhac))

            if 0 <= diem <= 10:
                return diem

            print("-> Diem phai nam trong khoang tu 0 den 10.")

        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so.")


def them_sinh_vien():
    ma_sv = input("Nhap ma sinh vien: ").strip().upper()

    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print("-> Ma sinh vien da ton tai.")
        return

    ho_ten = input("Nhap ho ten sinh vien: ").strip().title()
    lop = input("Nhap lop: ").strip().upper()
    diem = nhap_diem("Nhap diem: ")

    sinh_vien_moi = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "lop": lop,
        "diem": diem
    }

    danh_sach_sinh_vien.append(sinh_vien_moi)

    print("-> Them sinh vien thanh cong.")


def tim_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()

    sv = tim_sinh_vien_theo_ma(ma_sv)

    if sv is None:
        print("-> Khong tim thay sinh vien.")
        return

    print("\nTHONG TIN SINH VIEN")
    print("Ma sinh vien:", sv["ma_sv"])
    print("Ho ten:", sv["ho_ten"])
    print("Lop:", sv["lop"])
    print("Diem:", sv["diem"])


def sua_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()

    sv = tim_sinh_vien_theo_ma(ma_sv)

    if sv is None:
        print("-> Khong tim thay sinh vien.")
        return

    ho_ten = input("Nhap ho ten moi: ").strip().title()
    lop = input("Nhap lop moi: ").strip().upper()
    diem = nhap_diem("Nhap diem moi: ")

    sv["ho_ten"] = ho_ten
    sv["lop"] = lop
    sv["diem"] = diem

    print("-> Sua thong tin sinh vien thanh cong.")


def xoa_sinh_vien():
    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

    sv = tim_sinh_vien_theo_ma(ma_sv)

    if sv is None:
        print("-> Khong tim thay sinh vien.")
        return

    danh_sach_sinh_vien.remove(sv)

    print("-> Xoa sinh vien thanh cong.")


def thong_ke():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co sinh vien nao.")
        return

    tong_diem = 0

    for sv in danh_sach_sinh_vien:
        tong_diem += sv["diem"]

    diem_trung_binh = tong_diem / len(danh_sach_sinh_vien)

    print("\n===== THONG KE =====")
    print("Tong so sinh vien:", len(danh_sach_sinh_vien))
    print("Diem trung binh:", round(diem_trung_binh, 2))


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien")
    print("3. Tim sinh vien")
    print("4. Sua thong tin sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            them_sinh_vien()

        elif lua_chon == "3":
            tim_sinh_vien()

        elif lua_chon == "4":
            sua_sinh_vien()

        elif lua_chon == "5":
            xoa_sinh_vien()

        elif lua_chon == "6":
            thong_ke()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh.")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()