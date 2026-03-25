import tkinter as tk 

def check_password():
    pwd = entry.get()
    if len(pwd) < 6 :
        result_label.config(text="pass is too weak.. you need length bigger than 6")
    elif any(char.isdigit() for char in pwd) and any(char.isalpha() for char in pwd):
        result_label.config(text="not bad but there is better..")
    elif any(char in "!@#$%^&*" for char in pwd):
        result_label.config(text="here is a strong password..")
    else:
        result_label.config(text="very weak pass..")

root = tk.Tk()
# to make a title to your window 
root.title("password strength checker!")
root.geometry("400x250")
root.resizable(False,False)

tk.Label(root,text="enter Password :").pack(pady=10)
entry = tk.Entry(root,show="*")
entry.pack(pady=5)
tk.Button(root,text="check",command=check_password).pack(pady=5)
result_label = tk.Label(root,text="")
result_label.pack(pady=10)
root.mainloop()


