from flask import Flask, jsonify
import boto3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/buckets')
def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    bucket_list_html = "<h2>S3 Buckets:</h2><ul style='list-style-type: none; font-family: Arial, sans-serif;'>"
    for bucket in buckets:
        bucket_list_html += f"<li style='margin: 10px 0; padding: 10px; background-color: #f0f0f0; border-radius: 5px;'>{bucket}</li>"
    bucket_list_html += "</ul>"

    return bucket_list_html

@app.route('/buckets/json')
def list_buckets_json():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    # Devuelve la lista de buckets en formato JSON
    return jsonify(buckets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

