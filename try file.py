from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Miniso UT")


icon = PhotoImage(file='C:\\Users\\bieng\\Documents\\image.png')
window.iconphoto(True,icon)

namae = Label(window, image=icon)

print("hello!!!")

print("newline")

print("trying in new branch")
print("trying in new branch")
print("trying in new branch for it to merge after")
namae.pack()
window.mainloop()