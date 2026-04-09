# Fine-Tune CogVideoX on Your Custom Characters Data

This guide shows you how to train CogVideoX on your own character images/videos to create a personalized video generation model.

## 📋 Overview

**What You'll Get:**
- A model trained specifically on YOUR 5 characters
- Better character consistency and accuracy
- 100% local - no external services needed after training
- Full ownership of the trained model

**Hardware Requirements:**
- **Minimum**: NVIDIA GPU with 16GB VRAM (RTX 4080)
- **Recommended**: NVIDIA GPU with 24GB VRAM (RTX 4090) or A100
- **Storage**: 50GB+ free disk space

---

## 🎯 Step-by-Step Guide

### Step 1: Prepare Your Training Data

Create a dataset folder with this structure:

```
my_characters_dataset/
├── prompts.txt          # Text descriptions for each video
├── videos/              # Your training videos
├── videos.txt           # List of video filenames
├── images/              # (Optional) Reference images
└── images.txt           # (Optional) List of image filenames
```

#### **What You Need:**

1. **Videos**: 20-100 short videos (5-10 seconds) of your characters
   - Resolution: 480x720 (height x width) for CogVideoX-5B
   - Frames: 49 frames per video (recommended)
   - Format: MP4

2. **Prompts**: Text descriptions for each video
   - One line per video in `prompts.txt`
   - Example: "A blue warrior character walking through a forest"

3. **Images** (Optional for I2V):
   - Reference images of your characters
   - Format: PNG
   - Resolution: 480x720

---

### Step 2: Install Training Dependencies

```bash
# Install fine-tuning dependencies
pip install accelerate deepbits
pip install -e .
```

---

### Step 3: Configure Training

The project supports two training methods:

#### **Method A: LoRA (Recommended for beginners)**
- ✅ Faster training
- ✅ Less VRAM required
- ✅ Smaller output files
- ✅ Good for most use cases

#### **Method B: Full Fine-Tuning (SFT)**
- ✅ Better quality
- ❌ More VRAM required
- ❌ Longer training time

---

### Step 4: Run Training

#### **For Image-to-Video (I2V) with LoRA:**

1. Edit the training script: `finetune/train_ddp_i2v.sh`

2. Key parameters to set:
```bash
--output_dir "./output/my_characters_model"
--data_root "./my_characters_dataset"
--caption_column "prompts.txt"
--image_column "images.txt"
--video_column "videos.txt"
--train_resolution "49x480x720"
--id_token "mychar"  # Special token for your characters
```

3. Run training:
```bash
cd finetune
bash train_ddp_i2v.sh
```

---

### Step 5: Use Your Trained Model

After training completes, use your custom model:

```bash
python inference/cli_demo.py \
  --prompt "mychar dancing in the rain" \
  --image_or_video_path "my_character_image.png" \
  --generate_type "i2v" \
  --model_path "THUDM/CogVideoX-5B-I2V" \
  --lora_path "./output/my_characters_model" \
  --output_path "my_custom_video.mp4"
```

---

## 💡 Tips for Best Results

### Data Quality:
- ✅ Use high-quality, well-lit videos
- ✅ Show characters from multiple angles
- ✅ Include various poses and actions
- ✅ Keep backgrounds simple initially
- ✅ 25+ videos recommended

### Training Settings:
- ✅ Use `--id_token` (e.g., "mychar") to help model learn your characters
- ✅ Set `lora_alpha` equal to `lora_rank` (e.g., both = 128)
- ✅ Use rank 64 or higher for better results
- ✅ Train for 500-1000 steps minimum

### Prompts:
- ✅ Be descriptive and specific
- ✅ Use your identifier token in prompts
- ✅ Keep under 200 words
- ✅ Example: "mychar, a blue warrior with silver armor, walking confidently through a magical forest"

---

## 🔧 Troubleshooting

### Out of Memory:
- Reduce batch size
- Use gradient accumulation
- Enable CPU offload
- Use lower resolution

### Poor Results:
- Add more training data
- Increase training steps
- Check data quality
- Adjust learning rate

---

## 📊 Expected Training Times

| GPU | Method | Dataset Size | Time |
|-----|--------|--------------|------|
| RTX 4090 | LoRA | 50 videos | ~2-4 hours |
| RTX 4080 | LoRA | 50 videos | ~3-6 hours |
| A100 | LoRA | 50 videos | ~1-2 hours |

---

## 🎓 Advanced Options

### Multi-GPU Training:
```bash
# Edit accelerate_config.yaml for multi-GPU setup
accelerate launch --config_file accelerate_config.yaml train.py
```

### Resume Training:
```bash
--resume_from_checkpoint "./output/my_characters_model/checkpoint-500"
```

---

## ✅ After Training

Your trained model will be in:
```
./output/my_characters_model/
├── checkpoint-*/
├── lora_weights.safetensors
└── training_config.json
```

You can now:
1. ✅ Generate videos locally with your custom model
2. ✅ Share the LoRA weights (small file, ~100MB)
3. ✅ Continue training with more data
4. ✅ No internet connection needed!

---

## 🚀 Next Steps

1. Start with 20-30 videos of your characters
2. Train with LoRA for 500-1000 steps
3. Test generation and evaluate quality
4. Add more data if needed and continue training
5. Fine-tune parameters for your specific use case

Good luck with your custom character video generator! 🎬
