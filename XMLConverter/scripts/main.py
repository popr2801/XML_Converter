import conversion_algorithm as conversion_algorithm
import tkinter as tk 

def update_label():
    conversion_algorithm.convert_file(path.get(),dest.get())
    result_label.config(text="File converted succesfully!")
root = tk.Tk()

root.title("XML Converter")

root.geometry("300x400")
root.columnconfigure(0, weight=1)
input_label = tk.Label(root,text="File to convert")
convert_label = tk.Label(root,text = "Destination path")
path = tk.Entry(root)
dest = tk.Entry(root)
print(path.get())
result_label = tk.Label(root)
button1 = tk.Button(root,text = "Convert",command = update_label)
input_label.grid(row=0,sticky="nsew")
path.grid(row=1,sticky="nsew")
convert_label.grid(row=2,sticky="nsew")
dest.grid(row=3,sticky="nsew")
button1.grid(row=4,sticky="nsew")
result_label.grid(row=5,sticky="nsew")
root.mainloop()
