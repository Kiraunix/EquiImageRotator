import tkinter as tk
from tkinter import filedialog

import numpy as np
from equilib import equi2equi
from PIL import Image, ImageTk


class ImageRotatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Rotator")

        # Load image
        self.load_button = tk.Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Save image
        self.save_button = tk.Button(master, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack()

        # Rotation sliders
        self.roll_scale = tk.Scale(master, from_=-180, to=180, orient=tk.HORIZONTAL, label="Roll", length=600)
        self.roll_scale.pack()
        self.pitch_scale = tk.Scale(master, from_=-180, to=180, orient=tk.HORIZONTAL, label="Pitch", length=600)
        self.pitch_scale.pack()
        self.yaw_scale = tk.Scale(master, from_=-180, to=180, orient=tk.HORIZONTAL, label="Yaw", length=600)
        self.yaw_scale.pack()

        # Bind the release of the mouse button to the update_image function
        self.roll_scale.bind("<ButtonRelease-1>", lambda event: self.update_preview())
        self.pitch_scale.bind("<ButtonRelease-1>", lambda event: self.update_preview())
        self.yaw_scale.bind("<ButtonRelease-1>", lambda event: self.update_preview())

        # Image display
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image_path = None
        self.image = None
        self.display_image = None
        self.preview_image = None

        # Bind resize event
        self.master.bind('<Configure>', lambda event: self.update_preview())

    def load_image(self):
        # Reset sliders before loading a new image
        self.roll_scale.set(0)
        self.pitch_scale.set(0)
        self.yaw_scale.set(0)

        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.preview_image = self.image.resize((self.image.width // 10, self.image.height // 10), Image.LANCZOS)
            self.update_preview()
            self.save_button.config(state=tk.NORMAL)

    def save_image(self):
        if self.image:
            self.apply_rotation(self.image).save(self.image_path)  # Save directly to the original path

    def apply_rotation(self, image):
        rots = {
            'roll': np.radians(self.roll_scale.get()),
            'pitch': np.radians(self.pitch_scale.get()),
            'yaw': np.radians(self.yaw_scale.get()),
        }
        img_array = np.array(image)
        img_array = np.transpose(img_array, (2, 0, 1))
        rotated_img_array = equi2equi(src=img_array, rots=rots, mode="bilinear")
        rotated_img_array = np.transpose(rotated_img_array, (1, 2, 0))
        return Image.fromarray(rotated_img_array)

    def update_preview(self, event=None):
        if self.preview_image:
            canvas_width = self.canvas.winfo_width() - 20  # 10px margin on each side
            canvas_height = int(canvas_width / 2)  # Maintain aspect ratio for the preview
            rotated_preview = self.apply_rotation(self.preview_image)
            self.display_image = ImageTk.PhotoImage(rotated_preview.resize((canvas_width, canvas_height), Image.LANCZOS))
            self.canvas.create_image(10, 10, anchor=tk.NW, image=self.display_image)
            self.canvas.image = self.display_image  # Keep a reference to prevent garbage-collection

root = tk.Tk()
app = ImageRotatorApp(root)
root.mainloop()

