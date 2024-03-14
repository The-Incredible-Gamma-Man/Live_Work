from flask import Flask, render_template, request
from face_recognition.compare import compare_faces

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    match = None
    if request.method == 'POST':
        # Process uploaded images
        image1 = request.files['image1']
        image2 = request.files['image2']
        match = compare_faces(image1, image2)
    return render_template('index.html', match=match)

if __name__ == '__main__':
    app.run(debug=True)
