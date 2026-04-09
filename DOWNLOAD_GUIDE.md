# 📥 How to Download CogVideoX Base Model

## 🎯 Quick Answer: It's Already Downloading!

The model download started when you ran `python app.py` in the terminal. You can see the progress there.

**Current location:** `C:\Users\Kabeer\.cache\huggingface\hub\`

---

## 📋 Different Ways to Download the Model

### **Method 1: Let It Finish (Easiest) ✅**

Just wait for the current download to complete. The Gradio demo will automatically start when it's done.

**Progress:** Check the terminal window where you ran `python app.py`

---

### **Method 2: Download to Specific Location (Recommended)**

This gives you better control over where the model is saved.

#### **Option A: Using Python Script**

```bash
python download_model.py
```

This interactive script will:
- Ask which model you want
- Download to `./local_models/` folder
- Show progress and completion message
- Can resume if interrupted

#### **Option B: Using Batch File**

```bash
download_model.bat
```

Same as above but Windows batch file.

---

### **Method 3: Manual Download with HuggingFace CLI**

#### **Step 1: Install CLI**
```bash
pip install huggingface_hub[cli]
```

#### **Step 2: Download Model**

For **CogVideoX-5B-I2V** (Recommended):
```bash
huggingface-cli download THUDM/CogVideoX-5b-I2V --local-dir "./local_models/CogVideoX-5B-I2V"
```

For **CogVideoX1.5-5B-I2V** (Higher Quality):
```bash
huggingface-cli download THUDM/CogVideoX1.5-5b-I2V --local-dir "./local_models/CogVideoX1.5-5B-I2V"
```

---

## 🤔 Which Model Should You Download?

### **CogVideoX-5B-I2V** ⭐ RECOMMENDED
- **Size:** ~25 GB
- **Resolution:** 480x720 (height x width)
- **VRAM Required:** 16GB+
- **Frames:** 49 frames (6 seconds at 8 fps)
- **Best For:** Most users, good quality, faster generation

### **CogVideoX1.5-5B-I2V**
- **Size:** ~30 GB  
- **Resolution:** 768x1360 (height x width)
- **VRAM Required:** 24GB+
- **Frames:** 81 frames (5 seconds at 16 fps)
- **Best For:** Higher quality, if you have a powerful GPU

**Recommendation:** Start with **CogVideoX-5B-I2V** - it's easier to run and still produces great results!

---

## ⏱️ Download Time Estimates

| Internet Speed | 25 GB Model | 30 GB Model |
|----------------|-------------|-------------|
| 10 Mbps | ~6 hours | ~7 hours |
| 50 Mbps | ~1.2 hours | ~1.4 hours |
| 100 Mbps | ~35 minutes | ~42 minutes |
| 500 Mbps | ~7 minutes | ~8 minutes |

---

## 💾 Where is the Model Saved?

### **Automatic Download (Current Method):**
```
C:\Users\Kabeer\.cache\huggingface\hub\models--THUDM--CogVideoX-5b\
```

### **Manual Download (Using Scripts):**
```
f:\PersonalData\GitHub_Repo\chat_bot\local_models\CogVideoX-5B-I2V\
```

**Advantage of Manual Download:**
- ✅ Easier to find and manage
- ✅ Can copy to backup
- ✅ Can share with others
- ✅ No cache cleanup needed

---

## ✅ How to Verify Download is Complete

The model folder should contain these files:

```
CogVideoX-5B-I2V/
├── model_index.json
├── scheduler/
│   └── scheduler_config.json
├── text_encoder/
│   ├── config.json
│   └── model.safetensors
├── tokenizer/
│   ├── spiece.model
│   └── tokenizer.json
├── transformer/
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors  (~10 GB)
├── vae/
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors  (~5 GB
└── vae_temporal_decoder/
    ├── config.json
    └── diffusion_pytorch_model.safetensors
```

**Total size:** ~25 GB

---

## 🚀 How to Use Downloaded Model

### **Option 1: Command Line**

```bash
python inference/cli_demo.py ^
  --prompt "A warrior character walking through a forest" ^
  --image_or_video_path "my_character.png" ^
  --generate_type "i2v" ^
  --model_path "./local_models/CogVideoX-5B-I2V" ^
  --output_path "output.mp4"
```

### **Option 2: Modify Gradio Demo**

Edit `inference/gradio_composite_demo/app.py` and change line 40:

```python
# Change this:
MODEL = "THUDM/CogVideoX-5b"

# To this:
MODEL = "./local_models/CogVideoX-5B-I2V"
```

Then run:
```bash
cd inference\gradio_composite_demo
python app.py
```

---

## ❌ Troubleshooting

### **Download is Very Slow**

**Solution 1:** Use HuggingFace mirror (if in China)
```bash
export HF_ENDPOINT=https://hf-mirror.com
python download_model.py
```

**Solution 2:** Resume interrupted download
Both methods support resume - just run the command again!

### **Not Enough Disk Space**

**Solutions:**
- Free up space on your drive
- Use an external drive
- Download to a different drive:
  ```bash
  huggingface-cli download THUDM/CogVideoX-5b-I2V --local-dir "D:/models/CogVideoX-5B-I2V"
  ```

### **Download Fails**

**Try these:**
1. Check internet connection
2. Disable VPN if using one
3. Try again - downloads can resume
4. Use alternative method (CLI vs Python script)

### **Out of Memory During Download**

This shouldn't happen - the download itself uses minimal RAM. The error is likely during model loading. Make sure you have:
- 16GB+ GPU VRAM for CogVideoX-5B
- 24GB+ GPU VRAM for CogVideoX1.5-5B

---

## 🎓 Pro Tips

### **Tip 1: Download Both Models**
If you have space, download both:
```bash
python download_model.py  # Choose option 3 in batch file
```

### **Tip 2: Backup Your Model**
Once downloaded, create a backup:
```bash
xcopy /E /I local_models\CogVideoX-5B-I2V D:\backup\CogVideoX-5B-I2V
```

### **Tip 3: Use Symlinks to Save Space**
If you want to share models between projects:
```bash
mklink /D C:\Users\Kabeer\.cache\huggingface\hub\local-model F:\models\CogVideoX
```

---

## 📊 What's Downloading Right Now?

Check your terminal window. You should see output like:

```
Fetching 16 files:  19%|████████████████▉ | 3/16 [00:00<00:03, 3.98it/s]
Downloading: 45%|██████████████████████████▌ | 9.8G/21.5G [05:20<12:30, 15.6MB/s]
```

This shows:
- How many files downloaded
- Current speed
- Estimated time remaining

---

## ✅ After Download Complete

Once the model is downloaded:

1. ✅ Test it with the Gradio interface
2. ✅ Try generating a video with a sample image
3. ✅ Prepare your character images
4. ✅ (Optional) Start collecting training data for fine-tuning

**Next step:** See `YOUR_LOCAL_VIDEO_SOLUTION.md` for complete workflow!

---

## 📞 Need Help?

If you're stuck:
1. Check the terminal for error messages
2. Verify you have enough disk space (50GB+ free)
3. Make sure internet connection is stable
4. Try the alternative download method

**Current Status:** Model is downloading in your terminal. Just wait for it to complete! 🎬
