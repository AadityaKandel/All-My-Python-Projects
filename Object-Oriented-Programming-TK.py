'''
This is not my first tkinter application but the first one which uses Object Oriented Programming.
I have created several applications using the functional method that we normally learn in the beginning.
With this, I am finding several things easier than the functional method. Like variable scope. The best example is variable scope.
'''



from tkinter import *
import tkinter.messagebox as tmsg

class AppWindow:

	def __init__(self,master):
		# Setting required variables
		self.master=master
		self.window_width = 500
		self.window_height = 500
		self.title="OOP Application"

		# Setting window height and width
		self.master.minsize(self.window_width, self.window_height)

		# Setting the title of root window
		self.master.title(self.title)

		# Setting extra variables
		self.count = 0


		# Creating Widgets
		self.l1 = Label(text=f"Count: {self.count}", fg="black", bg="white", border=4, pady=10)
		self.l1.pack()

		self.b1 = Button(text="Add Count",bg="gray",fg="black",border=4, command=self.increase_count)
		self.b1.pack()

		self.b2 = Button(text="Sub Count",bg="gray",fg="black",border=4, command=self.decrease_count)
		self.b2.pack()

		# Setting the config for root
		self.master.config(bg="white")

	def increase_count(self):
		self.count+=1
		self.l1.config(text=f"Count: {self.count}")
		

	def decrease_count(self):
		self.count-=1
		self.l1.config(text=f"Count: {self.count}")


root = Tk()
app1 = AppWindow(root)
root.mainloop()
