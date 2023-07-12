from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Miniso UT")


icon = PhotoImage(file='C:\\Users\\bieng\\Documents\\image.png')
window.iconphoto(True,icon)

namae = Label(window, image=icon)

print("hello")
namae.pack()
window.mainloop()