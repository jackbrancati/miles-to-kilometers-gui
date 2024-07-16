from tkinter import *

window = Tk()
window.title('Miles to Kilometers GUI')

window.config(padx=20,pady=30)

def button_clicked():
    miles_input = float(input.get())
    km_output = miles_input*1.60934
    answer_label.config(text=km_output)

#Label
equals_label = Label(text='is equal to:')
equals_label.grid(column=0,row=1)

#Entry
input = Entry(width=10)
input.grid(column=1,row=0)

#Answer Label
answer_label = Label(text='0')
answer_label.grid(column=1,row=1)

#Km Label
km_label = Label(text='KM')
km_label.grid(column=2,row=1)

#Calculate Button
calc_button = Button(text='Calculate', command=button_clicked)
calc_button.grid(column=1,row=3)

window.mainloop()