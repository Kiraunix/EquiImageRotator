# EquiImageRotator

![Demo GIF](./demo.gif)

EquiImageRotator is a user-friendly application designed to rotate equirectangular images with ease. Whether you're working with 360-degree panoramas or other spherical images, this tool provides a simple interface to apply roll, pitch, and yaw rotations accurately.

## Features
Load and Save Images: Easily load equirectangular images from your file system and save the rotated images.
Intuitive Rotation Controls: Adjust roll, pitch, and yaw with interactive sliders, offering precise control over the image orientation.
Real-Time Preview: View the effects of your adjustments in real-time, ensuring you get the perfect rotation before saving.
High-Quality Processing: Utilizes bilinear interpolation to maintain image quality during rotation.
## Getting Started
Clone the Repository:

```sh
git clone https://github.com/yourusername/EquiImageRotator.git
cd EquiImageRotator
```

### Install Dependencies:
Ensure you have Python and pip installed, then run:

```sh
pip install -r requirements.txt
```

### Run the Application:
```sh
python EquiImageRotater.py
```

## Dependencies
Tkinter: For the graphical user interface.
Pillow: For image handling.
Numpy: For numerical operations.
Equilib: For equirectangular image rotation processing.

## Usage
Launch the application and click "Load Image" to select an equirectangular image from your file system.
Use the sliders to adjust the roll, pitch, and yaw of the image.
The preview area will update in real-time to reflect your changes.
Once satisfied with the rotation, click "Save Image" to overwrite the original file with the rotated image.

## Acknowledgments
- Tkinter: Used for creating the graphical user interface.
- Pillow: Utilized for image processing and manipulation.
- Numpy: Employed for numerical operations and data manipulation.
- Equilib: A crucial library for processing equirectangular images. Special thanks to [Haruya Ishikawa](https://haruishi.xyz/) for developing and maintaining this library.You can find more about Equilib [here](https://github.com/haruishi43/equilib).

