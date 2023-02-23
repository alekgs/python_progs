import tkinter as tk


def add_label():
    label_1 = tk.Label(win, text='Hello, world !')
    label_1.pack()


win = tk.Tk()
photo = tk.PhotoImage(file='blue-company.png')
win.iconphoto(False, photo)
win.title('Моё первое окно на Python')
# win.config(bg='#d5e5f3')
win.geometry('800x600+600+200')
win.resizable(True, True)
win.minsize(640, 480)
win.maxsize(800, 600)

btn_1 = tk.Button(win, text='Hello', command=add_label)

btn_1.pack()
win.mainloop()
