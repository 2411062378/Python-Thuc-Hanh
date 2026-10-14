import tkinter as tk

dem = 0

def dem_lan_bam():
    global dem
    dem += 1
    lbl_dem.config(text=f"So lan da bam: {dem}")

cua_so = tk.Tk()
cua_so.title("Dem so lan bam nut")
cua_so.geometry("350x200")

lbl_dem = tk.Label(cua_so, text="So lan da bam: 0", font=("Arial", 14))
lbl_dem.pack(pady=20)

btn_bam = tk.Button(cua_so, text="Bam vao day", command=dem_lan_bam)
btn_bam.pack(pady=10)

cua_so.mainloop()
