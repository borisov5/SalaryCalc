import tkinter as tk

from screen import before_calculations


if __name__ == '__main__':
    window = tk.Tk()
    window.configure(background='#d4f1f9')
    window.geometry('480x480')
    window.title('SalaryCalc')
    before_calculations(window)
    window.mainloop()
