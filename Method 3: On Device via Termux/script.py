import onnxruntime as rt
import numpy as np
from PIL import Image # using PIL instead of cv2
import time
import sys

model_path = "dog_vs_cat_mobile.onnx" # Use your QUANTIZED model

print("📱 Loading model on Android...")
sess = rt.InferenceSession(model_path)
input_name = sess.get_inputs()[0].name

# Generate dummy data instead of loading a real file 
# (Easier than moving image files to specific phone folders)
input_shape = (1, 256, 256, 3) 
dummy_input = np.random.rand(*input_shape).astype(np.float32)

print("🏃 Running Inference...")
start = time.time()

# Run 10 loops to heat up the processor
for i in range(10):
    sess.run(None, {input_name: dummy_input})

end = time.time()
avg_time = (end - start) / 10

print(f"✅ Average Inference Time: {avg_time*1000:.2f} ms")