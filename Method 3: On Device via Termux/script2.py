import time

# 1. Start Total Timer (Includes library import time!)
total_start = time.time()

print("🚀 Initializing...")
import onnxruntime as rt
import numpy as np
from PIL import Image
import os

# --- CONFIGURATION ---
model_path = "dog_vs_cat_mobile.onnx"
image_path = "test.jpg"

# 2. Load the Model
print("⏳ Loading model into RAM...")
load_start = time.time()
try:
    sess = rt.InferenceSession(model_path)
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()
load_end = time.time()

input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# 3. Load and Preprocess Image
print(f"🖼️ Preprocessing {image_path}...")
prep_start = time.time()

if not os.path.exists(image_path):
    print(f"❌ Error: {image_path} not found.")
    exit()

try:
    img = Image.open(image_path).convert('RGB')
    img = img.resize((256, 256))
    img_data = np.array(img).astype(np.float32) / 255.0
    input_data = np.expand_dims(img_data, axis=0)
except Exception as e:
    print(f"❌ Error processing image: {e}")
    exit()
prep_end = time.time()

# 4. Run Inference
print("🏃 Running Prediction...")
inf_start = time.time()
outputs = sess.run([output_name], {input_name: input_data})
inf_end = time.time()

# 5. Stop Total Timer
total_end = time.time()

# --- REPORTING ---
# Predictions
prediction = outputs[0][0][0]
if isinstance(prediction, np.ndarray): prediction = prediction.item()
label = "DOG 🐶" if prediction > 0.5 else "CAT 🐱"
confidence = prediction if prediction > 0.5 else 1 - prediction

print(f"\n" + "="*30)
print(f"   RESULT: {label} ({confidence*100:.1f}%)")
print(f"="*30)

print(f"\n⏱️  TIMING BREAKDOWN:")
print(f"   • Model Loading:  {(load_end - load_start)*1000:.1f} ms")
print(f"   • Preprocessing:  {(prep_end - prep_start)*1000:.1f} ms")
print(f"   • AI Inference:   {(inf_end - inf_start)*1000:.1f} ms  <-- (Real speed)")
print(f"-"*30)
print(f"   ✅ TOTAL TIME:    {(total_end - total_start):.4f} seconds")