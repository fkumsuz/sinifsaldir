"""from flask import Flask, render_template
import os
from PIL import Image

app = Flask(__name__)

# Folder containing the original images
original_image_folder = "static/images"
# Folder to store resized images
resized_image_folder = "static/resized_images"

# Get the list of image files in the original folder
image_files = [file for file in os.listdir(original_image_folder) if file.endswith((".jpg", ".jpeg", ".png"))]
# Ensure the resized images folder exists
os.makedirs(resized_image_folder, exist_ok=True)

# Resize all images to 500x500 and save them to the resized folder
resized_image_files = []
for filename in image_files:
    image_path = os.path.join(original_image_folder, filename)
    with Image.open(image_path) as img:
        img_resized = img.resize((500, 500))
        resized_image_path = os.path.join(resized_image_folder, filename)
        img_resized.save(resized_image_path)
        resized_image_files.append(os.path.join("resized_images", filename))

@app.route('/')
def index():
    return render_template('index.html', image_files=resized_image_files)

if __name__ == '__main__':
    app.run(debug=True)
"""


from flask import Flask, render_template
import os

app = Flask(__name__)

# Folder containing the images
image_folder = "./images"
# Get the list of image files and names in the folder
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith((".jpg", ".jpeg", ".png"))]
image_names = [os.path.splitext(os.path.basename(file))[0] for file in image_files]

@app.route('/')
def index():
    return render_template('index.html', image_files=image_files, image_names=image_names)

if __name__ == '__main__':
    app.run(debug=True)
