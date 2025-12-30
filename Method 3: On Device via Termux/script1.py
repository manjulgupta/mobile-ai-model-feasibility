import onnxruntime as rt
import numpy as np
from PIL import Image  # Using Pillow instead of OpenCV
import time
import os

# --- CONFIGURATION ---
model_path = "dog_vs_cat_mobile.onnx"  # Make sure this matches your file name
image_path = "test.jpg"                # Make sure this image is in the folder

# 1. Load the Model
print("⏳ Loading model...")
try:
    sess = rt.InferenceSession(model_path)
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()

input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# 2. Load and Preprocess the Image
print(f"🖼️ Processing {image_path}...")

if not os.path.exists(image_path):
    print("❌ Error: Image file not found! Did you copy 'test.jpg' to this folder?")
    exit()

try:
    # Open image and convert to RGB (ensures compatibility even with PNGs)
    img = Image.open(image_path).convert('RGB')

    # Resize to 256x256 (Same as your training)
    img = img.resize((256, 256))

    # Convert to Numpy Array
    img_data = np.array(img)

    # Normalize (0-255 -> 0.0-1.0)
    img_data = img_data.astype(np.float32) / 255.0

    # Add Batch Dimension: (256, 256, 3) -> (1, 256, 256, 3)
    input_data = np.expand_dims(img_data, axis=0)

except Exception as e:
    print(f"❌ Error processing image: {e}")
    exit()

# 3. Run Inference (The Real Test)
print("🏃 Running Prediction...")
start_time = time.time()

# Run the model
outputs = sess.run([output_name], {input_name: input_data})

end_time = time.time()

# 4. Results
inference_time = (end_time - start_time) * 1000
print(f"\n✅ Done! Inference time: {inference_time:.2f} ms")

# Interpret Prediction
# Assuming output is probability [0-1] where >0.5 is Dog (based on your earlier code)
prediction = outputs[0][0][0] 

# Handle different output shapes just in case
if isinstance(prediction, np.ndarray):
    prediction = prediction.item()

label = "DOG 🐶" if prediction > 0.5 else "CAT 🐱"
confidence = prediction if prediction > 0.5 else 1 - prediction

print(f"-----------------------------")
print(f"RESULT: {label}")
print(f"Confidence: {confidence*100:.2f}%")
print(f"Raw Output: {prediction:.4f}")
print(f"-----------------------------")