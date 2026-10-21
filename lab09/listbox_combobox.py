import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Vi du Listbox & Combobox")
cua_so.geometry("350x450")

# --- LISTBOX ---
tk.Label(cua_so, text="Danh sách môn học (Listbox):", font=("Arial", 10, "bold")).pack(pady=(10, 5))
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5)
for mon in ["Toán", "Lý", "Hóa", "Văn", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=5)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua_listbox.config(text=f"Môn đã chọn: {listbox_mon_hoc.get(lua_chon[0])}")

tk.Button(cua_so, text="Xem môn đã chọn", command=xem_mon_da_chon).pack(pady=5)
nhan_ket_qua_listbox = tk.Label(cua_so, text="", fg="green")
nhan_ket_qua_listbox.pack()

tk.Label(cua_so, text="----------------------------------------").pack(pady=5)

# --- COMBOBOX ---
tk.Label(cua_so, text="Chọn thành phố (Combobox):", font=("Arial", 10, "bold")).pack(pady=5)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Hà Nội", "Đà Nẵng", "TP.HCM", "Huế"], state="readonly")
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua_combo.config(text=f"Bạn chọn: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xác nhận thành phố", command=xem_thanh_pho).pack(pady=5)
nhan_ket_qua_combo = tk.Label(cua_so, text="", fg="purple")
nhan_ket_qua_combo.pack()

cua_so.mainloop()