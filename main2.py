from tkinter import *

print('hello')

class Rulet:

	def __init__(self):
		self.a = 1
	
	def start(self):
		root = Tk()
		root.title('Рулетка')
		root.geometry('250x80')
		rul = Button(root, text='правила', command=lambda: rules())
		rul.pack(side='bottom')

		singin = Button(root,text='Войти',command=lambda:Rulet.login(self))
		singin.pack(side='bottom')

		play = Button(root,text='Играть',command=lambda: Rulet.play(self))
		play.pack(side='top')


		def rules(): #окно с сылкой на правила игры
			root1 = Tk()
			root1.geometry('300x50')
			root1.title('правила')
			text = Text(root1)
			text0 = Label(root1, text='Ну тогда перейдите по этой ссылке')
			text.insert(1.0, 'https://goo.gl/zFwaJt')
			text0.pack()
			text.pack()
		root.mainloop()
	
	def login(self):
		singin = Tk()
		singin.title('Вход')
		 
		l0 = Label(singin,text='Неверный логин или пароль')
		l1 = Label(singin,text='Логин')
		e1 = Entry(singin)
		l2 = Label(singin,text='Пароль')
		e2 = Entry(singin,show=' ')
		b1 = Button(singin,text='Войти',command=lambda:singingin(e1.get(),e2.get()))

		r1 = Button(singin,text='Зарегестрироваться',command=lambda: register())
		r1.pack()
		
		l1.pack()
		e1.pack()
		l2.pack()
		e2.pack()
		b1.pack()

		def singingin(log,pas):
			
			login=log
			password=pas

			l5 = Label(singin,text='неверный логин или пароль')

			f = open('ak', 'r')
			logins = []

			for line in f.readlines():
				logins.append(line.split())

			wrong = True

			for line in logins:
				print(line[0],login,line[1],password)
				if line[0] == login:
					if line[1] == password:
						self.play()
						print('you win')
						wrong = False

			if wrong:
				l5.pack()

		def register():
			register = Tk()
			ll0 = Label(register,text='Этот логин уже занят')
			great = Label(register,text='Вы зарегистрированы')
			ll1 = Label(register,text='Логин')
			ee1 = Entry(register)
			ll2 = Label(register,text='Пароль')
			ee2 = Entry(register)
			bb1 = Button(register,text='Зарегестрироваться',command=lambda:registr(ee1.get(),ee2.get()))
			
			

		def registr(a,b):

			f = open('ak','r')
			logins = []

			for line in f.readlines():
				login = line.split()
				logins.append(login[0])

			f.close()

			if a in logins():
				ll0.pack()
			else:
				f = open('ak','a')
				f.write(a,' ',b)
				great.pack()
			

			ll1.pack()
			ee1.pack()
			ll2.pack()
			ee2.pack()
			bb1.pack()

	def play(self):
		play = Tk()
