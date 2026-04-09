"""
Download CogVideoX models for local use
This script downloads the model to a local directory for offline use.
"""

from huggingface_hub import snapshot_download
import os

# Create local_models directory
os.makedirs("local_models", exist_ok=True)

print("=" * 60)
print("CogVideoX Model Downloader")
print("=" * 60)
print()
print("Available models:")
print()
print("1. CogVideoX-5B-I2V (Recommended)")
print("   - Size: ~25 GB")
print("   - Resolution: 480x720")
print("   - VRAM: 16GB+")
print()
print("2. CogVideoX1.5-5B-I2V (Higher Quality)")
print("   - Size: ~30 GB")
print("   - Resolution: 768x1360")
print("   - VRAM: 24GB+")
print()

choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    model_id = "THUDM/CogVideoX-5b-I2V"
    local_dir = "./local_models/CogVideoX-5B-I2V"
elif choice == "2":
    model_id = "THUDM/CogVideoX1.5-5b-I2V"
    local_dir = "./local_models/CogVideoX1.5-5B-I2V"
else:
    print("Invalid choice. Please run again and enter 1 or 2.")
    exit(1)

print()
print(f"Downloading: {model_id}")
print(f"Save location: {local_dir}")
print("This will take 30 minutes to 2 hours depending on your internet speed.")
print()

try:
    snapshot_download(
        repo_id=model_id,
        local_dir=local_dir,
        local_dir_use_symlinks=False,
        resume_download=True
    )
    
    print()
    print("=" * 60)
    print("✅ Download Complete!")
    print("=" * 60)
    print()
    print(f"Model saved to: {local_dir}")
    print()
    print("To use this local model, run:")
    print(f"  python inference/cli_demo.py \\")
    print(f"    --prompt \"Your prompt here\" \\")
    print(f"    --image_or_video_path \"your_image.png\" \\")
    print(f"    --generate_type \"i2v\" \\")
    print(f"    --model_path \"{local_dir}\"")
    print()
    
except Exception as e:
    print()
    print("=" * 60)
    print("❌ Download Failed!")
    print("=" * 60)
    print()
    print(f"Error: {e}")
    print()
    print("Possible solutions:")
    print("1. Check your internet connection")
    print("2. Make sure you have enough disk space")
    print("3. Try again - the download can resume where it left off")
    print()
