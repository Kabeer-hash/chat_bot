"""
Launch CogVideoX Image-to-Video Demo using LOCAL model only
No HuggingFace downloads - uses your locally saved model
"""

import os
import sys

# Add the inference/gradio_composite_demo path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "inference", "gradio_composite_demo"))

# IMPORTANT: Change this path to where you saved your model
LOCAL_MODEL_PATH = r"F:\PersonalData\GitHub_Repo\chat_bot\local_models\CogVideoX-5B-I2V"

print("=" * 60)
print("CogVideoX Image-to-Video Demo (LOCAL MODEL)")
print("=" * 60)
print(f"\nUsing local model from: {LOCAL_MODEL_PATH}")
print("\nStarting the Gradio web interface...")
print("\nOnce started, you can:")
print("1. Upload an image with your 5 characters")
print("2. Enter a prompt describing what they should do")
print("3. Click 'Generate Video'")
print("\n" + "=" * 60)

# Modify app.py to use local model
os.environ["LOCAL_MODEL_PATH"] = LOCAL_MODEL_PATH

# Import and run the demo
from app import demo

if __name__ == "__main__":
    demo.queue(max_size=15)
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
