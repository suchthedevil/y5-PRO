import tkinter as tk

c = tk.Canvas(height=500, width=900)
c.pack()

c.create_rectangle(0, 0, 100, 100, fill="blue")

c.mainloop()