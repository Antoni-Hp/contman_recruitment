import tkinter as tk
from urllib.parse import urlparse
import tkinter.messagebox


class startGUI():

    def __init__(self, urlCallback):
        self.urlCallback = urlCallback
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
        self.download.bind('<Button-1>', self.cos)
        self.score = tk.Text(self.window, height = 17, width = 44, state = 'disabled')

    def cos(self, event):
        self.url = self.set_url.get()
        if self.is_url() is False:
            tk.messagebox.showinfo("Wrong url", "Please enter a valid URL")
        else:
            self.stats = self.urlCallback(self.url)
            self.showStats()

    def showStats(self):
        self.score.configure(state = 'normal')
        self.score.delete('1.0', tk.END)
        if self.stats != 'Page does not contain keywords':
            for k, v in self.stats.items():
                self.score.insert(tk.END, '%s : %s\n' %(k, v))
                self.score.see(tk.END)

        else:
            self.score.insert(tk.END, self.stats)
        self.score.configure(state = 'disable')

    def is_url(self):
        try:
            result = urlparse(self.url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

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