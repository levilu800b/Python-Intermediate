from tkinter import *

# Create a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()
