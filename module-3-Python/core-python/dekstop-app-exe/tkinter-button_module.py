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
# add button widget
button=tk.Button(text="submit", bg="black", fg="white", font=("Arial",18))
button.pack(pady=10)
# create output 
tk.mainloop()

# convert in .exe formate 
# cmd : python -m PyInstaller --onefile --windowed windows_app.py

# 