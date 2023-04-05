import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class ImageRemover:
    def __init__(self):
        self.image_list = []
        self.current_index = -1
        self.directory = ""
        self.selected_image = None
        self.width_height = None
        
        self.root = tk.Tk()
        self.root.title("Image Remover")
        
        # 1st row
        load_button = tk.Button(self.root, text="Load Images", command=self.load_images)
        load_button.grid(row=0, column=0)
        
        # 2nd row
        remove_button = tk.Button(self.root, text="Remove", command=self.remove_image)
        remove_button.grid(row=1, column=0)
        
        # 3rd row
        self.index_width_height = tk.StringVar()
        width_height_label = tk.Label(self.root, textvariable=self.index_width_height)
        width_height_label.grid(row=2, column=0)
        
        # 4th row
        self.image_display = tk.Label(self.root)
        self.image_display.grid(row=3, column=0)
        self.image_display.bind("<Button-1>", self.display_next_image)
        
       
        self.root.mainloop()

    def load_images(self):
        self.directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Directory")
        if self.directory:
            self.image_list = [os.path.join(self.directory, f) for f in os.listdir(self.directory) if f.endswith('.jpg') or f.endswith('.png')]
            self.current_index = 0
            self.show_image()

    def show_image(self):
        image_path = self.image_list[self.current_index]
        #image = tk.PhotoImage(file=image_path)
        image = ImageTk.PhotoImage(Image.open(image_path))        
        self.index_width_height.set(f"{self.current_index} / {len(self.image_list)}, W x H : {image.width()} x {image.height()}")
        self.image_display.config(image=image)
        self.image_display.image = image

    def remove_image(self):
        print(f'self.current_index : {self.current_index}, self.selected_image : {self.selected_image}')
        if self.current_index >= 0 and self.selected_image is not None:
            image_path = self.image_list[self.current_index]
            image_name = os.path.basename(image_path)
            new_directory = os.path.join(os.path.dirname(self.directory), f"{os.path.basename(self.directory)}_removed")
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            shutil.move(image_path, os.path.join(new_directory, image_name))
            self.image_list.pop(self.current_index)
            if len(self.image_list) > 0:
                if self.current_index >= len(self.image_list):
                    self.current_index = len(self.image_list) - 1                
                self.show_image()
                #self.selected_image = event.widget
                #self.selected_image = None
            else:
                exit()
                #self.width_height.set("")
                #self.image_display.config(image="")
                #self.current_index = -1

    def display_next_image(self, event):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
        else:
            self.current_index = 0
        self.show_image()
        self.selected_image = event.widget
        if len(self.image_list) <= 0:
            exit()
 
app = ImageRemover()










