import time
import numpy as np
from PIL import Image

# Simulate a 1080p Video Frame (1920x1080)
# This creates a random image in memory
print("🎨 Generatng dummy 1080p frame...")
original_frame = np.random.randint(0, 255, (1080, 1920, 3), dtype=np.uint8)
img_pil = Image.fromarray(original_frame)

print(f"🔄 Starting Stress Test: 1080p -> 512x512 Resize + Norm")
print("   (Running 50 times to get average)")

start_time = time.time()

for i in range(50):
    # 1. Resize (The heavy part)
    img_resized = img_pil.resize((512, 512))
    
    # 2. Convert to Array
    arr = np.array(img_resized)
    
    # 3. Normalize (The math part)
    # This divides 262,144 pixels by 255.0
    arr = arr.astype(np.float32) / 255.0
    
    # 4. Expand Dims (Prep for ONNX)
    arr = np.expand_dims(arr, axis=0)

end_time = time.time()

avg_time = (end_time - start_time) / 50
print(f"\n✅ Average Preprocessing Time: {avg_time*1000:.2f} ms")

if avg_time < 0.05:
    print("🚀 Result: Super Fast. Preprocessing is negligible.")
elif avg_time < 0.15:
    print("⚠️ Result: Moderate. Preprocessing will rival Inference time.")
else:
    print("❌ Result: Bottleneck. Preprocessing is SLOWER than the AI.")