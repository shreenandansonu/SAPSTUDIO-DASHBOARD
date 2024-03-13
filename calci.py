import tkinter as tk

root = tk.Tk()

# Create and configure widgets
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
button = tk.Button(root, text="Submit")

# Place widgets in the grid
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
entry1.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
button.grid(row=2, column=0, columnspan=2, pady=5)

# Configure the grid to maintain size
for i in range(3):  # Adjust based on the number of rows
    root.grid_rowconfigure(i, weight=1, uniform='row')

for i in range(2):  # Adjust based on the number of columns
    root.grid_columnconfigure(i, weight=1, uniform='column')

root.mainloop()
