import tkinter as tk

def Start():
    print("Clicked")
##################Welcom screen#################
window = tk.Tk()
window.geometry("1080x720")
Main_Text = tk.Label(window,text="IELTS SPEAKING TEST")
Main_Text.pack()

Start_Button = tk.Button(window,text="Start",command=Start)
Start_Button.pack()

window.mainloop()


