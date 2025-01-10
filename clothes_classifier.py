from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import uuid
import io
import numpy as np
from PIL import Image
from rembg import remove
from transformers import pipeline, ViTForImageClassification, AutoProcessor


# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Load Hugging Face pipeline for Vision Transformer (image classification)
model_name = "google/vit-base-patch16-224"
processor = AutoProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Hugging Face pipeline for text generation (chatbot)
chatbot_pipeline = pipeline("text-generation", model="gpt2")

def classify_image(image_array):
    """
    Classify the clothing item using a pre-trained Hugging Face Vision Transformer model.
    """
    try:
        # Convert the image to PIL format
        pil_image = Image.fromarray(image_array)
        pil_image = pil_image.resize((28, 28))

        # Normalize pixel values
        image_array = np.array(pil_image) / 255.0

        # Preprocess the image and make predictions
        inputs = processor(images=pil_image, return_tensors="pt")
        outputs = model(**inputs)
        predictions = outputs.logits.softmax(dim=-1)
        top_prediction = predictions.argmax(dim=-1).item()

        # Get the label for the top prediction
        label = model.config.id2label[top_prediction]
        return label
    except Exception as e:
        print(f"Error during classification: {e}")
        return "Unknown"

def generate_ai_response(labels):
    """
    Generate a dynamic response about the outfit based on classified labels.
    """
    try:
        upper_label = labels[0]
        lower_label = labels[1]
        
        # Feed clothing labels directly as input to the model
        input_text = f"Upper Item: {upper_label}, Lower Item: {lower_label}. Comment on this outfit."

        # Generate response using the Hugging Face GPT-2 pipeline
        response = chatbot_pipeline(input_text, max_length=50, num_return_sequences=1, truncation=True)
        return response[0]["generated_text"].strip()
    except Exception as e:
        print(f"Error generating AI response: {e}")
        return "I'm having trouble analyzing your outfit. Please try again later."

# model_name = "google/flan-t5-base"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# def generate_ai_response(labels):
#     """
#     Generate a response about the outfit using the Flan-T5 model.
#     """
#     try:
#         upper_label = labels[0]
#         lower_label = labels[1]
#         input_text = f"Upper Item: {upper_label}, Lower Item: {lower_label}. Comment on this outfit."

#         # Tokenize and generate response
#         inputs = tokenizer(input_text, return_tensors="pt")
#         outputs = model.generate(inputs["input_ids"], max_length=150, temperature=0.7)
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#         return response.strip()
#     except Exception as e:
#         print(f"Error generating AI response with Flan-T5: {e}")
#         return "I'm having trouble analyzing your outfit. Please try again later."



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save uploaded file
    file_id = str(uuid.uuid4())
    filename = f"{file_id}.png"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    # Process image
    processed_items = process_image(file_path)
    return jsonify(processed_items), 200

def process_image(image_path):
    try:
        # Background removal
        with open(image_path, "rb") as f:
            raw_image = f.read()
        bg_removed = remove(raw_image)

        # Load the image with background removed
        bg_removed_image = Image.open(io.BytesIO(bg_removed)).convert("RGBA")
        white_bg = Image.new("RGBA", bg_removed_image.size, (255, 255, 255, 255))
        composite = Image.alpha_composite(white_bg, bg_removed_image).convert("RGB")

        # Split into upper and lower halves
        np_image = np.array(composite)
        height = np_image.shape[0]
        mid_height = height // 2
        upper_region = np_image[:mid_height, :, :]
        lower_region = np_image[mid_height:, :, :]

        # Classify both regions
        upper_label = classify_image(upper_region)
        lower_label = classify_image(lower_region)

        # Save processed images
        session_id = str(uuid.uuid4())
        session_folder = os.path.join(app.config["PROCESSED_FOLDER"], session_id)
        os.makedirs(session_folder, exist_ok=True)

        upper_path = os.path.join(session_folder, f"upper_{uuid.uuid4()}.png")
        lower_path = os.path.join(session_folder, f"lower_{uuid.uuid4()}.png")

        Image.fromarray(upper_region).save(upper_path)
        Image.fromarray(lower_region).save(lower_path)

        return {
            "upper": {
                "image": f"/processed/{session_id}/{os.path.basename(upper_path)}",
                "label": upper_label
            },
            "lower": {
                "image": f"/processed/{session_id}/{os.path.basename(lower_path)}",
                "label": lower_label
            }
        }
    except Exception as e:
        print(f"Error processing image: {e}")
        return {"upper": {}, "lower": {}}

@app.route("/processed/<session_id>/<filename>")
def serve_processed_image(session_id, filename):
    session_folder = os.path.join(app.config["PROCESSED_FOLDER"], session_id)
    return send_from_directory(session_folder, filename)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    upper_label = data.get("upper_label", "Unknown")
    lower_label = data.get("lower_label", "Unknown")

    # Prepare labels and generate AI response
    labels = [upper_label, lower_label]
    ai_response = generate_ai_response(labels)
    return jsonify({"response": ai_response})


if __name__ == "__main__":
    app.run(debug=True)
