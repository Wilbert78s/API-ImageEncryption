from flask import Flask, jsonify, request, send_file, make_response
from werkzeug.utils import secure_filename
import io
import base64
from PIL import Image # manipulate
from processes.cryptography import encrypt, decrypt
import numpy as np # store array
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config["ALLOWED_EXTENSIONS"] = set(['png', 'jpg', 'jepg'])
def allowed_file(filename):
    return "." in filename and \
        filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

def add_numbers(x, y):
    sum_result = x + y
    return sum_result

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200

@app.route("/encrypt", methods=["POST"])
def encryption():    
    image = request.files["image"]
    if image and allowed_file(image.filename):
        p1 = float(request.form.get('p1'))
        p2 = float(request.form.get('p2'))
        k1 = int(request.form.get('k1'))
        k2 = int(request.form.get('k2'))
        x0 = float(request.form.get('x0'))
        a0 = float(request.form.get('a0'))
        x1 = float(request.form.get('x1'))
        a1 = float(request.form.get('a1'))
        a = int(request.form.get('a'))        
        b = int(request.form.get('b'))
        # Read the content of the image

        """ image_data = image.read() """
        img = Image.open(image)
        img = encrypt(img, a, b, x0, a0, x1, a1, [p1,p2], k1, k2)
        """ img_array = np.array(img)
        print(img_array) """

        img_bytes = io.BytesIO()
        img['image'].save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        # Convert BytesIO object to bytes and then to a string
        # Assuming img_bytes contains the raw binary data of the image
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        """ print("=============================")
        img_bytes_io = io.BytesIO(img_bytes)
        img = Image.open(img_bytes_io)
        img_array = np.array(img)
        print(img_array) """
        # Return the same image in the response
        response_data = {
            'file': img_base64,
            'hash': img['hash'],
            'width': img['width'],
            'height': img['height']
        }
        return jsonify(response_data)
    
    return 0

@app.route("/decrypt", methods=["POST"])
def decryption():    
    image = request.files["image"]
    if image and allowed_file(image.filename):
        p1 = float(request.form.get('p1'))
        p2 = float(request.form.get('p2'))
        k1 = int(request.form.get('k1'))
        k2 = int(request.form.get('k2'))
        x0 = float(request.form.get('x0'))
        a0 = float(request.form.get('a0'))
        x1 = float(request.form.get('x1'))
        a1 = float(request.form.get('a1'))
        a = int(request.form.get('a'))        
        b = int(request.form.get('b'))
        width = int(request.form.get('width'))        
        height = int(request.form.get('height'))
        hashing = request.form.get('hashing')
        # Read the content of the image
        """ image_data = image.read() """
        img = Image.open(image)
        img = decrypt(img, a, b, x0, a0, x1, a1, [p1,p2], k1, k2, hashing, width, height)

        img_bytes = io.BytesIO()
        img['image'].save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')

        response_data = {
            'file': img_base64,
            'hash': img['hash'],
            'width': img['width'],
            'height': img['height']
        }
        return jsonify(response_data)
    return 0
        
if __name__ == "__main__":
    app.run()

