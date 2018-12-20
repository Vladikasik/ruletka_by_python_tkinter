from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('185x170')

l1 = ttk.Label(root,text='login')
e1 = ttk.Entry(root)
l2 = ttk.Label(root,text='password')
e2 = ttk.Entry(root,show='*')
b1 = ttk.Button(root,text='Login',command=lambda:logining_in())
b2 = ttk.Button(root,text='Register',command=lambda :register())
l3 = ttk.Label(root,text='   ')
l4 = ttk.Label(root,text='   ')

b2.pack()
l4.pack()
l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
b1.pack()


def logining_in():
    login = e1.get()
    password = e2.get()

    l5 = Label(root,text='неверный логин или пароль')

    f = open('ak', 'r')
    logins = []

    for line in f.readlines():
        logins.append(line.split())

    wrong = True

    for line in logins:
        print(line[0],login,line[1],password)
        if line[0] == login:
            if line[1] == password:
                play()
                print('you win')
                wrong = False

    if wrong:
        l5.pack()

def register():
    root1 = Tk()

    l1 = ttk.Label(root1, text='login')
    e1 = ttk.Entry(root1)
    l2 = ttk.Label(root1, text='password')
    e2 = ttk.Entry(root1)
    l5 = ttk.Label(root1, text='pavtorite password')
    e3 = ttk.Entry(root1)
    b1 = ttk.Button(root1, text='Register',command=lambda:new_password())
    l3 = ttk.Label(root1, text='   ')
    l4 = ttk.Label(root1, text='   ')
    l6 = Label(root1,text='вы успешно зарегестрировались')
    l7 = Label(root1,text='пароли не совпадают')


    l4.pack()
    l1.pack()
    e1.pack()
    l2.pack()
    e2.pack()
    l5.pack()
    e3.pack()
    l3.pack()
    b1.pack()

   

    def new_password():
        pas1 = e2.get()
        pas2 = e3.get()
        if pas1 == pas2:
            //l7[text] = '' 
            l6.pack()
        else:
            l7.pack()


def play():
    play = Tk()

root.mainloop()