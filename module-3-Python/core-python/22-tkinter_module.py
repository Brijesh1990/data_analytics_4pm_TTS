import tkinter as tk 
# windows app
root=tk.Tk()
# title 
root.title("windows app data")
# create geometry 
root.geometry("550x450")
# write a label on window
label=tk.Label(text="My name is Dhruv", fg="white", bg="blue",font=("Arial",25))
label.pack(pady=20)
# create output 
tk.mainloop()