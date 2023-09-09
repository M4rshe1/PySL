from tkinter import filedialog, Tk
import tkinter as tk

from PIL import Image
import os

# Check if the folder images exists
if not os.path.exists('images'):
    # If not create the folder
    os.mkdir('images')

# Set selectable Image types
filetypes = (
    ('JPEG', '*.jpg'),
    ('PNG', '*.png'),
    ('TIFF', '*.tiff'),
    ('All files', '*.*')
)

# select image with explorer and save it in the images folder
# Open explorer to select the image
while True:
    # Hide the Tkinter GUI
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=filetypes)
    # Break if an images is selected
    # kill the program if no image is selected
    if image_path == "":
        print("No image selected")
        exit()
    else:
        break


# enter Filetype to save the image as
file_type = input("Enter Filetype to save the image as: \n>> ")

# save the image in the images folder
# set size for ico format to 256x256
if file_type == "ico":
    Image.open(image_path).resize((256, 256)).save(f"images/{image_path.split('/')[-1].split('.')[0]}.{file_type}")
else:
    Image.open(image_path).save(f"images/{image_path.split('/')[-1].split('.')[0]}.{file_type}")
