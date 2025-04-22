# Waste Classifier Web App

This is a simple image classification web application built using **Gradio** and a pre-trained **TensorFlow/Keras** model. The model predicts whether a given image of waste is **Organic** or **Recyclable**.

## Features

- Upload or take a photo of waste.
- The app predicts the category (Organic or Recyclable).
- It shows a confidence score between 0 and 1.
- Runs locally with a shareable web link.

## Requirements

- Python 3.7 or higher
- TensorFlow
- Gradio
- Pillow
- NumPy

Install the required packages using:

```bash
pip install -r requirements.txt
```
```bash
## File Structure
gradio_environ/
├── app.py                  # Gradio interface code
├── main.py                 # Contains image preprocessing and prediction logic
├── final_model_weights.hdf5 # Trained model file (update path if needed)
├── requirements.txt        # Python dependencies
├── LICENSE
├── README.md
```
## How to Run
1. Ensure Model File is Available
Place the trained model file (final_model_weights.hdf5) in the same directory as main.py.
If your model is in a different location, update the path in main.py like this:
MODEL_PATH = "your/custom/path/final_model_weights.hdf5"

2. (Optional) Activate a Virtual Environment

# For Windows
.\venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

## 3. Launch the Application
```bash
Use the following command to run the app:

python app.py
```
This will start a Gradio interface in your browser.

Prediction Logic
In main.py, the image is resized to 180x180 and normalized before being passed to the model.


image = image.resize((180, 180))
img_array = img_to_array(image) / 255.0
The model output is interpreted using:


label = "Recyclable" if predicted_class == 1 else "Organic"
Update this logic if your model uses different class labels.

## Customization
To use your own model:

Replace final_model_weights.hdf5 with your own .h5 file.

Adjust the image size in main.py to match your model input.

Modify class label mapping if your dataset uses more or different classes.


##  Model Weights

The trained model weights are stored in a `.hdf5` file and are too large to be hosted directly on GitHub.

👉 **Download the model weights from Google Drive**:  
[Click here to download final_model_weights.hdf5](https://drive.google.com/file/d/1xPw7w3biAlu_sxMGzCsgxPUWbzuFJUaI/view?usp=sharing)

---



