'''
This is a ROCK, PAPER, SCISSOR game that I've made using Python OOP.
It was fun to make one... [^_^]
'''


from tkinter import *
import tkinter.messagebox as tmsg
import random

class GameWindow:

	def __init__(self, master):

		# Setting up a little configurations
		self.master = master
		self.master.geometry("400x400")
		self.master.minsize(400,400)
		self.master.maxsize(400,400)
		self.master.title("Rock Paper Scissor Game")

		# Setting up variables
		self.labels = ["Rock!","Paper!","Scissor!","Shoot!"]
		self.options = ["ROCK","PAPER","SCISSOR"]
		self.user_decision = ''
		self.bot_decision = ''
		self.winner_text=""

		# Setting up frames
		self.f1 = Frame(borderwidth=10, bg="white")
		self.f2 = Frame(borderwidth=10, bg="white")
		self.f3 = Frame(borderwidth=10, bg="white")
		self.f4 = Frame(borderwidth=10, bg="white")

		# Setting up Widgets

		# Widget Frame 1
		self.l1 = Label(self.f1,text="Rock Paper Scissor Game",justify=CENTER, bg="white", fg="black", font="comicsansms 14 bold")
		self.l1.pack()

		# Widget Frame 2
		self.l1 = Label(self.f2,text="Status: ",justify=CENTER, bg="white", fg="black", font="comicsansms 12 italic")
		self.l1.pack()

		# Widgets Frame 3
		self.rock = Button(self.f3, text="ROCK", justify=LEFT, bg="lightgray", fg="black", font="system 14", state=DISABLED, padx=33, pady=30,command=lambda: self.choose_user_decision('ROCK'))
		self.paper = Button(self.f3, text="PAPER", justify=LEFT, bg="lightgray", fg="black", font="system 14", state=DISABLED, padx=33, pady=30,command=lambda: self.choose_user_decision('PAPER'))
		self.rock.pack(side=LEFT,padx=10)
		self.paper.pack(side=LEFT,padx=10)

		# Widgets Frame 4
		self.scissor = Button(self.f4, text="SCISSOR", justify=LEFT, bg="lightgray", fg="black", font="system 14", state=DISABLED, padx=100, pady=30,command=lambda: self.choose_user_decision('SCISSOR'))
		self.scissor.pack(side=LEFT,padx=13)


		# Packing all frames
		self.f1.pack(anchor=N)
		self.f2.pack(anchor=N)
		self.f3.pack(anchor=N)
		self.f4.pack(anchor=N)

		# Packing a separate button outside the frames
		self.b1 = Button(text="Start", justify=CENTER, bg="lightgray", fg="black", font="system 14", padx=13,command=self.start_game)
		self.b1.pack(pady=10)

		# Setting Game Buttons
		self.widget_options = [self.rock,self.paper,self.scissor]


		# Setting up the root config
		self.master.config(bg="white")

	def generate_random_decisions(self):
		# This function is callable and used for the bots' decision
		decision = random.sample(range(len(self.options)),1)
		return decision[0]

	def buttons_state_toggler(self,special_case):
		if self.rock['state']==DISABLED:
			for options in self.widget_options:
				options.config(state=NORMAL)
		elif self.rock['state']==NORMAL:
			for options in self.widget_options:
				options.config(state=DISABLED)
		elif special_case==True:
			for options in self.widget_options:
				options.config(state=DISABLED)

	def choose_user_decision(self, decision):
		self.user_decision=decision
		self.buttons_state_toggler(True)

	def winner_announcement(self):
		if self.user_decision=="ROCK" and self.bot_decision=="SCISSOR":
			self.winner_text="ROCK beats SCISSOR. YOU WON!!"
		elif self.user_decision=="SCISSOR" and self.bot_decision=="ROCK":
			self.winner_text="ROCK beats SCISSOR. YOU LOST!!"
		elif self.user_decision=="ROCK" and self.bot_decision=="PAPER":
			self.winner_text="PAPER beats ROCK. YOU WON!!"
		elif self.user_decision=="PAPER" and self.bot_decision=="ROCK":
			self.winner_text="PAPER beats SCISSOR. YOU LOST!!"
		elif self.user_decision=="SCISSOR" and self.bot_decision=="PAPER":
			self.winner_text="SCISSOR beats PAPER. YOU WON!!"
		elif self.user_decision=="PAPER" and self.bot_decision=="SCISSOR":
			self.winner_text="SCISSOR beats PAPER. YOU LOST!!"
		elif self.user_decision == self.bot_decision:
			self.winner_text=f"Both Chose {self.user_decision}. It's a DRAW!"
		else:
			self.winner_text="You Chose Nothing! You lost!"


	def start_game(self):

		self.bot_decision = self.options[self.generate_random_decisions()]
		self.buttons_state_toggler(False) # Enable all buttons
		self.b1.config(state=DISABLED)
		for items in self.labels:
			self.l1.config(text=items)
			self.master.after(1000)
			self.master.update()

		self.winner_announcement()
		self.l1.config(text=self.winner_text)
		self.b1.config(text="Play Again!",state=NORMAL)



root = Tk()
g1 = GameWindow(root)
root.mainloop()
