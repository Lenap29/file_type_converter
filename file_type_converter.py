# Import Required Library
import PIL.ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os

# Create Tkinter Object
root = Tk()

# set Geomtery
root.geometry("400x400")
canvas = Canvas(root)
image = PIL.ImageTk.PhotoImage(PIL.Image.open("bg.jpg"))
canvas.create_image(100, 100, image=image)
canvas.pack(fill='both', expand=True)
root.resizable(False,False)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", background='orange', foreground = "white")

# Set title
root.title("IMAGE CONVERTER")
# select image
def select_image():
    global file_name
    file_name = filedialog.askopenfilename(initialdir = "/",title = "Select Image")

# convert image
def convert_image():
  image_conversion = PIL.Image.open(file_name)
  if choose_image_format.get().lower() == "pdf'":
      image_conversion = image_conversion.convert('RGB')
  converted_file = f'{file_name.split(".")[0]}.{choose_image_format.get().lower()}'
  image_conversion.save(converted_file)
  messagebox.showinfo("Success","Image Converted Successfully!!")
  os.system('"' + converted_file + '"')

# Add Labels, Buttons
Label(canvas, text="Image Converter", font="italic 30 bold", bg="orange", fg="black").pack(pady=5)
Button(canvas, text="Select Image",command=select_image, font="italic 28",bg = "orange", fg="black").pack(pady=5)

# Image Format Values
image_format = [ "PNG", "JPG", "JPEG", "JFIF", "WEBP", "PDF"]

image_string = StringVar()

image_string.set(image_format[0])

choose_image_format = ttk.Combobox(canvas, textvariable = image_string, values=image_format, font="italic 15", state='readonly')
  
choose_image_format.pack(pady=20)

Button(canvas, text="convert",command=convert_image, font="italic 28",bg='orange', fg = "black").pack(pady=70)

# Execute Tkinter
root.mainloop()
