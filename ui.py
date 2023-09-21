import tkinter as tk
from PIL import Image, ImageTk
import win32api
import os
        
window = tk.Tk()
window.title('Image Viewer')
window.state('zoomed')
x = tk.IntVar()
aspect_ratio = (win32api.GetSystemMetrics(1) / win32api.GetSystemMetrics(0))
images = {}
imageFrame = tk.Frame(window)
imageFrame.pack(fill='both',expand=False)
img = tk.Label(imageFrame)
img.pack(side='left',padx=5)
def handle_click():
    load = Image.open("./imgs/"+images[x.get()])
    new_height = load.height*aspect_ratio
    new_width = load.width*aspect_ratio
    load = load.resize((int(new_width),int(new_height)))
    render = ImageTk.PhotoImage(load)
    img.config(image=render)
    img.image=render


folderFrame = tk.Frame(imageFrame,width=(win32api.GetSystemMetrics(0)//2),height=win32api.GetSystemMetrics(1))
folderFrame.pack(fill='y',expand=False,padx=10)
img_list=[]
path = "./imgs"
n_row = 0
n_col = 0
index = 0
for f in os.listdir(path):
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'):
        load = Image.open(os.path.join(path,f))
        load.thumbnail((150,150))
        img_list.append(ImageTk.PhotoImage(load))
        if n_col > 5:
            n_row +=1
            n_col = 0
        images[index] = f
        radio_button = tk.Radiobutton(folderFrame, image=img_list[index], indicatoron=0, bd=2, variable = x, value = index,command=handle_click)
        radio_button.grid(row=n_row,column=n_col)
        n_col += 1
        index += 1
if len(images)>0:
    load = Image.open("./imgs/"+images[0])
    new_height = load.height*aspect_ratio
    new_width = load.width*aspect_ratio
    load = load.resize((int(new_width),int(new_height)))
    render = ImageTk.PhotoImage(load)
    img.config(image=render)
    img.image=render

window.mainloop()

