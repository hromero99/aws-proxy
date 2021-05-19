from flask import Flask
from flask import jsonify, abort
from flask import request
import boto3
import os
UPLOAD_DIRECTORY = "/tmp/"

app = Flask(__name__)

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_KEY")
)


@app.route("/s3/upload/<filename>", methods=["POST"])
def upload_to_s3(filename):
    if "/" in filename:
        abort(400, "Invalid caracter inserted")
    file = request.files['upload_file']
    if file:
        file.save(os.path.join(UPLOAD_DIRECTORY, filename))
        s3.upload_file(os.path.join(UPLOAD_DIRECTORY, filename), "microk8s-sensor-data", filename)
    return {"data": f"File {filename} upload to bucket"}, 201

