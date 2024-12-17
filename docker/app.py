from flask import Flask, request, jsonify
import json
import object_detection

app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def hello_user():
    return "<h1>welcome to object detection service</h>"

# Define a route for the object detection API
@app.route("/api/object_detect", methods=['POST'])

def object_detect():
    # Get the JSON data from the request
    data = request.get_json()
    # Extract the image ID and base64 encoded image data from the JSON
    id = data["id"]
    image = data["image"]
    
    # Call the process_img function from the object_detection module to process the image
    result = object_detection.process_img(image)
    
    print(f"Processing image with ID: {id}...")
    
    return jsonify({"id": id, "object": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, threaded=True)