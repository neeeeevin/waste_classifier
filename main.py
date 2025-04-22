import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load the trained model from local path
MODEL_PATH = r"C:\Users\NEVIN\Desktop\gradio_environ\final_model_weights.hdf5"
model = load_model(MODEL_PATH)

def get_prediction(image: Image.Image):
    try:
        # Resize and preprocess image
        image = image.resize((180, 180))  # Match model input size
        img_array = img_to_array(image) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict
        prediction = model.predict(img_array)[0]
        predicted_class = int(np.argmax(prediction))
        confidence = float(prediction[predicted_class])

        # Class labels (update if needed)
        label = "♻️ Recyclable" if predicted_class == 1 else "🌱 Organic"

        return label, confidence

    except Exception as e:
        # Return error message with 0 confidence
        return f"Error: {str(e)}", 0.0
