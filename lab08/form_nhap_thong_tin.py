import tkinter as tk

def submit():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    lbl_result.config(text=f"Da nhan: {name} {age} tuoi {email}")

def xoa():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    lbl_result.config(text="")

cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("400x280")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(cua_so, width=25)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_age = tk.Entry(cua_so, width=25)
entry_age.grid(row=1, column=1, padx=10, pady=10)

tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

btn_submit = tk.Button(cua_so, text="Submit", command=submit)
btn_submit.grid(row=3, column=0, pady=15)

btn_xoa = tk.Button(cua_so, text="Xoa", command=xoa)
btn_xoa.grid(row=3, column=1, pady=15)

lbl_result = tk.Label(cua_so, text="", font=("Arial", 11), fg="blue")
lbl_result.grid(row=4, column=0, columnspan=2, pady=10)

cua_so.mainloop()