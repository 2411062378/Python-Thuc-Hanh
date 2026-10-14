import tkinter as tk

danh_sach_mau = ["white", "lightblue", "lightgreen", "lightyellow", "lightpink"]
vi_tri = 0

def doi_mau():
    global vi_tri
    vi_tri = (vi_tri + 1) % len(danh_sach_mau)
    cua_so.config(bg=danh_sach_mau[vi_tri])

cua_so = tk.Tk()
cua_so.title("Doi mau nen")
cua_so.geometry("350x200")

btn = tk.Button(cua_so, text="Doi mau nen", command=doi_mau)
btn.pack(pady=80)

cua_so.mainloop()