BACKGROUND_COLOR ="white"# "#5F6F52"
TEXT_COLOR = "black"  #"#FEFAE0"

from flask import Flask, render_template
import os

app = Flask(__name__)

# Folder containing the images
image_folder = "static/images"
# Get the list of image files and names in the folder
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith((".jpg", ".jpeg", ".png"))]
image_names = [os.path.splitext(os.path.basename(file))[0] for file in image_files]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', image_files=image_files, image_names=image_names, background_color=BACKGROUND_COLOR, text_color=TEXT_COLOR)

if __name__ == '__main__':
    app.run(debug=True)
