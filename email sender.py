import smtplib
from tkinter import *
from tkinter import messagebox

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

root = Tk()
root.title('Python Gmail Sender')
root.resizable(width=False, height=False)
root.geometry('800x500')
root.configure(background='dodger blue')

usm = " "

def main():
    to = Label(root, text='To : ', font=("Arial Black", 12),fg='white', bg='dodger blue')
    cc = Label(root, text='CC : ', fg='white', font=("Arial Black", 12), bg='dodger blue')
    bcc = Label(root, text='BCC : ', fg='white', font=("Arial Black", 12), bg='dodger blue')
    subject = Label(root, text='Subject : ',  font=("Arial Black", 12), fg='white', bg='dodger blue')

    to.grid(row=0, column=0, sticky=W, padx=3)
    cc.grid(row=1, column=0, sticky=W,pady=3, padx=3)
    bcc.grid(row=2, column=0, sticky=W, padx=3)
    subject.grid(row=3, column=0, sticky=W, pady=3, padx=3)

    to_entry = Entry(root, width=110)
    cc_entry = Entry(root, width=110)
    bcc_entry = Entry(root, width=110)
    subject_entry = Entry(root, width=110)

    to_entry.grid(row=0, column=1)
    cc_entry.grid(row=1, column=1, pady=5)
    bcc_entry.grid(row=2, column=1)
    subject_entry.grid(row=3, column=1, pady=5)

    scroll = Scrollbar(root)
    scroll.grid(row=4, column=2, pady=5, sticky=NS)

    message = Text(root, width=95, height=19, yscrollcommand=scroll.set)
    message.grid(row=4, columnspan=2, pady=3.5)

    scroll.config(command=message.yview)

    def send():
        header = f"From: {usm}\n"
        header += f"To: {to_entry.get()}\n"
        header += f"Cc: {cc_entry.get()}\n"
        header += f"Bcc: {bcc_entry.get()}\n"
        header += f"Subject: {subject_entry.get()}\n\n"
        pesan = header + f"{message.get('1.0', END)}"

        penerima = [f"{to_entry.get()}"]
        if cc_entry.get():
            penerima.append(f"{cc_entry.get()}")
        else: pass
        if bcc_entry.get():
            penerima.append(f"{bcc_entry.get()}")
        else: pass

        kirimkan = server.sendmail(usm, penerima , pesan)

        to_entry.delete(0, END)
        cc_entry.delete(0, END)
        bcc_entry.delete(0, END)
        subject_entry.delete(0, END)
        message.delete(1.0, END)

        messagebox.showinfo("Success !", f"Email Kepada {', '.join(penerima)}\nSukses terkirim !")

        return kirimkan

    kirim = Button(root, text="Send Now", bg="royal blue", fg='white', activebackground="dodger blue",
                   activeforeground="light blue", font=("Arial Black", 12), command=send)
    kirim.grid(row=5, column=1, sticky=E, pady=4)

    exit = Button(root, text="    ", bg="dodger blue", relief=FLAT)
    exit.grid(row=5, column=1)

wel = Frame(root)
wel.pack()
text = Label(wel, width=800, height=6, text='\n\n\nWELCOME TO PyGMAIL\nAn App to Send Google Email using Python',
             font=('Bonk', 32), fg='papaya whip',bg='dodger blue')
text.pack()

log = Frame(root, width=800, height=250)
log.pack()

user = Entry(log, width=100, fg='gray')
user.pack()
pwd = Entry(root, width=100, fg='gray')
pwd.pack(pady=2)

user.insert(0, "Your Gmail Username here..")
pwd.insert(0, "Your Gmail Password here..")

vent_user = 0
vent_pwd = 0

def userfun(event):
    global vent_user
    if vent_user == 0:
        user.delete(0, END)
        user.config(fg='black')
        vent_user += 1
    else: pass
    return

def pwdfun(event):
    global  vent_pwd
    if vent_pwd == 0:
        pwd.delete(0, END)
        pwd.config(fg='black', show='*')
        vent_pwd+= 1
    else: pass
    return

def useradd(event):
    global vent_user
    if vent_user == 1 and not user.get().endswith("@gmail.com"):
        user.insert(END, "@gmail.com")
        vent_user+=1
        return
user.bind('<FocusIn>', userfun)
user.bind('<FocusOut>', useradd)
pwd.bind('<FocusIn>', pwdfun)

def ngelogin(event):
    try:
        usm = user.get()
        pas = pwd.get()
        server.login(usm, pas)
        log.destroy()
        wel.destroy()
        pwd.destroy()
        login_tombol.destroy()
    except:
        messagebox.showwarning('Warning !', 'E-mail atau Password Anda Salah')
    return main()

def ngeloginTomb():
    try:
        usm = user.get()
        pas = pwd.get()
        server.login(usm, pas)
        log.destroy()
        wel.destroy()
        pwd.destroy()
        login_tombol.destroy()
    except:
        messagebox.showwarning('Warning !', 'E-mail atau Password Anda Salah')
    return main()

login_tombol = Button(root, width=7, text="Sign In", font=("Arial Black", 10),fg='white', bg='royal blue',
                      activebackground='dodger blue', activeforeground='light blue', command=ngeloginTomb)
login_tombol.pack(pady=10)
pwd.bind('<Return>', ngelogin)

root.mainloop()