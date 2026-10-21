import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Checkbutton & Radiobutton")
cua_so.geometry("360x420")

# --- PHẦN 1: CHECKBUTTON ---
tk.Label(cua_so, text="Chọn sở thích của bạn:", font=("Arial", 11, "bold")).pack(pady=(10, 5))

bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

tk.Checkbutton(cua_so, text="Đọc sách", variable=bien_doc_sach).pack(anchor="w", padx=30)
tk.Checkbutton(cua_so, text="Thể thao", variable=bien_the_thao).pack(anchor="w", padx=30)
tk.Checkbutton(cua_so, text="Âm nhạc", variable=bien_am_nhac).pack(anchor="w", padx=30)

def xem_lua_chon():
    print("Đọc sách:", bien_doc_sach.get())
    print("Thể thao:", bien_the_thao.get())
    print("Âm nhạc:", bien_am_nhac.get())

tk.Button(cua_so, text="Xem lựa chọn (in ra console)", command=xem_lua_chon).pack(pady=10)

tk.Label(cua_so, text="----------------------------------------").pack()

# --- PHẦN 2: RADIOBUTTON ---
tk.Label(cua_so, text="Chọn loại tài khoản:", font=("Arial", 11, "bold")).pack(pady=(5, 5))

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Radiobutton(cua_so, text="Cá nhân", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so, text="Doanh nghiệp", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)

def xem_loai_tai_khoan():
    nhan_ket_qua.config(text=f"Bạn đã chọn: {bien_loai_tai_khoan.get()}")

tk.Button(cua_so, text="Xác nhận tài khoản", command=xem_loai_tai_khoan).pack(pady=5)
nhan_ket_qua = tk.Label(cua_so, text="", fg="blue")
nhan_ket_qua.pack()

cua_so.mainloop()