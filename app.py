from flask import Flask, jsonify, request, send_file, make_response
from werkzeug.utils import secure_filename
import io
import base64
from PIL import Image # manipulate
from processes.cryptography import encrypt, decrypt
import numpy as np # store array
from flask_cors import CORS
from google.cloud import storage

def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client(project='skripsi-416101')
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

from PIL import Image
import io

def upload_pil_image_to_storage(bucket_name, pil_image, destination_blob_name):
    """Uploads a PIL image to Google Cloud Storage."""
    with io.BytesIO() as output:
        pil_image.save(output, format="PNG")
        image_bytes = output.getvalue()
    upload_blob_from_memory(bucket_name, image_bytes, destination_blob_name)

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads content to a blob in Google Cloud Storage."""
    storage_client = storage.Client(project='skripsi-416101')
    # storage_client.from_service_account_json('./key.json')
    # storage_client = storage.Client(project='skripsi-416101', credentials='key.json')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(contents, content_type='image/png')
    print(f"Uploaded {destination_blob_name} to {bucket_name}.")


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
    list_buckets()
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200

@app.route("/encrypt", methods=["POST"])
def encryption():    
    # list_buckets()
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
        # img['image'].show()
        filename = "cipher_image/" + img['hash'][:20] + ".png"
        # filename = "cipher_image/percobaan.png"
        upload_pil_image_to_storage('website_skripsi', img['image'], filename)
        img_url = "https://storage.googleapis.com/website_skripsi/"+filename
        # print(type(img['image']))
        # upload_blob_from_stream('website_skripsi', img['image'], 'gambar pertama')
        """ img_array = np.array(img)
        print(img_array) """

        # img_bytes = io.BytesIO()
        # img['image'].save(img_bytes, format='PNG')
        # img_bytes = img_bytes.getvalue()
        # Convert BytesIO object to bytes and then to a string
        # Assuming img_bytes contains the raw binary data of the image
        # img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        # upload_blob_from_memory(img_base64, 'string.png')
        """ print("=============================")
        img_bytes_io = io.BytesIO(img_bytes)
        img = Image.open(img_bytes_io)
        img_array = np.array(img)
        print(img_array) """
        # Return the same image in the response
        
        response_data = {
            'file': img_url,
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

