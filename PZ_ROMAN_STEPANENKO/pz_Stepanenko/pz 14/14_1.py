#Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).

import tkinter as t
from tkinter import ttk as k

r = t.Tk()
r.title("Certificate Self Service Portal")
r.geometry("800x650")
r.configure(bg="#f0f0f0")

f = t.Frame(r, bg="white", padx=40, pady=40)
f.grid(row=0, column=0, pady=40, sticky="n")
r.grid_columnconfigure(0, weight=1)

t.Label(
    f,
    text="Certificate Self Service Portal",
    font=("Arial", 24),
    bg="white",
    fg="#333333",
).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))
t.Label(
    f,
    text="Fill out the form to get a certificate.",
    font=("Arial", 11),
    bg="white",
    fg="#666666",
).grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 25))

s = [
    ("Requester", "firstname lastname"),
    ("Short Name", "asdf"),
    ("Email", "mail@mail.com"),
    ("Organization", "Organization"),
    ("Country", "Armenia"),
    ("IPv4 Address", "127.0.0.1"),
    ("Hostname", "host"),
    ("FQDN", "host.domain.tld"),
]

o = k.Style()
o.theme_use("clam")
o.configure("TCombobox", fieldbackground="white", background="white")

i = 2
for l, p in s:
    t.Label(
        f,
        text=l,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#333333",
        width=15,
        anchor="e",
    ).grid(row=i, column=0, padx=(0, 15), pady=8, sticky="e")
    if l == "Country":
        c = k.Combobox(f, values=["Armenia", "Russia", "USA"], width=43)
        c.set(p)
        c.grid(row=i, column=1, pady=8, sticky="w")
    else:
        e = t.Entry(
            f,
            font=("Arial", 10),
            bg="white",
            fg="#333333",
            bd=1,
            relief="solid",
            width=45,
        )
        e.insert(0, p)
        e.grid(row=i, column=1, pady=8, ipady=4, sticky="w")
    i += 1

t.Label(
    f,
    text="Description",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#333333",
    width=15,
    anchor="e",
).grid(row=i, column=0, padx=(0, 15), pady=8, sticky="ne")
x = t.Text(
    f,
    font=("Arial", 10),
    bg="white",
    fg="#333333",
    bd=1,
    relief="solid",
    width=45,
    height=4,
)
x.insert("1.0", "desc")
x.grid(row=i, column=1, pady=8, sticky="w")
i += 1

t.Button(
    f,
    text="Submit Form",
    font=("Arial", 10),
    bg="#337ab7",
    fg="white",
    bd=0,
    padx=15,
    pady=8,
).grid(row=i, column=1, pady=(20, 0), sticky="w")

r.mainloop()

#Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 1 – 9.
