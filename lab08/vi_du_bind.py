import tkinter as tk

def on_key(event):
    lbl_msg.config(text=f"Ban vua nhan phim: {event.char}")

def on_click(event):
    lbl_msg.config(text=f"Ban vua click tai toa do: ({event.x}, {event.y})")

cua_so = tk.Tk()
cua_so.title("Vi du bind()")
cua_so.geometry("400x250")

lbl_msg = tk.Label(cua_so, text="Hay go phim hoac click chuot", font=("Arial", 12))
lbl_msg.pack(pady=30)

cua_so.bind("<Key>", on_key)
cua_so.bind("<Button-1>", on_click)

cua_so.mainloop()