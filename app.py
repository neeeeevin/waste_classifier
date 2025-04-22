import gradio as gr
from main import get_prediction

def classify(image):
    label, confidence = get_prediction(image)
    return label, confidence  # Return as tuple instead of dict

interface = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil", label="📸 Upload or Take a Photo"),
    outputs=[
        gr.Label(num_top_classes=2, label="Prediction"),
        gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label="Confidence")
    ],
    title="♻️ Waste Classifier",
    description="Classify waste as Organic 🌱 or Recyclable ♻️ using your image."
)

if __name__ == "__main__":
    interface.launch(share=True)
