import tkinter as tk
# from tkinter.ttk import DISABLED, NORMAL


class startGUI():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400")
        self.window.resizable(False, False)
        self.window.title("Recruitment task")
        self.window.config(background = 'grey')
        self.create()
        self.show()
        self.display()

    def create(self):
        self.set_url_txt = tk.Label(self.window, text = "Enter the URL")
        self.set_url = tk.Entry(self.window, width = 40)
        self.download = tk.Button(self.window, text = "Download page")
        self.download.bind('<Button-1>', self.cos())
        self.score = tk.Text(self.window, height = 17, width = 44, state = 'disabled')
        return True
    def cos(self):
        return True
    def getUrl(self):
        # self.download.bind('<Button-1>', self)
        print("cos")
    def show(self):
        self.set_url_txt.place(x = 100, y = 20)
        self.set_url.place(x = 20, y = 48)
        self.download.place(x = 282, y = 45)
        self.score.place(x = 20, y = 90)

    def close(self):
        self.window.destroy()

    def display(self):
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()