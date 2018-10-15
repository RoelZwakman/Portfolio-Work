import tkinter as tk
import Main


#based on the tkinter GUI framework.
class Application(tk.Frame):
	
	def __init__(self, master=None):

		tk.Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):

		self.msgButton = tk.Button(self, text='Send message over COM3 connection', command=Main.sendMessage)
		self.msgButton.grid()

		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()
		

app = Application()
app.master.title('Interface')
app.mainloop()
	