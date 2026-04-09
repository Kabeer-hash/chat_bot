# Character Training Dataset

This folder contains the training data for your custom characters.

## 📁 Folder Structure

```
my_characters_dataset/
├── prompts.txt          ✅ Created - Text prompts for each video
├── videos.txt           ✅ Created - List of video files
├── videos/              ⏳ Create this folder - Add your training videos here
├── images/              ⏳ (Optional) Create this folder - Add reference images
└── images.txt           ⏳ (Optional) Create if using images
```

## 🎬 What to Add

### Required: Training Videos

1. **Create a `videos/` folder** in this directory
2. **Add 20-100 videos** of your characters:
   - Format: MP4
   - Resolution: 480x720 (height x width) 
   - Duration: 5-10 seconds each
   - Frames: 49 frames (6 seconds at 8 fps)

### Video Requirements:

- ✅ Clear, well-lit footage
- ✅ Show characters from different angles
- ✅ Various poses and actions
- ✅ Simple backgrounds work best
- ✅ Characters should be clearly visible

### Example Videos:
```
videos/
├── video_001.mp4  (blue warrior standing)
├── video_002.mp4  (blue warrior walking)
├── video_003.mp4  (red mage casting spell)
├── video_004.mp4  (red mage reading)
├── ...
└── video_020.mp4  (all five characters together)
```

### Optional: Reference Images (for I2V)

If you want to do Image-to-Video generation:

1. **Create an `images/` folder**
2. **Add character images**:
   - Format: PNG
   - Resolution: 480x720
   - Clear, high-quality images

3. **Create `images.txt`** with filenames:
```
image_001.png
image_002.png
image_003.png
...
```

## 📝 Prompts

The `prompts.txt` file is already created with 20 example prompts.
**Customize these to match your actual characters!**

Each line should describe what's happening in the corresponding video.

## 🚀 Next Steps

1. ✅ Customize the prompts to match your characters
2. ⏳ Create `videos/` folder and add training videos
3. ⏳ (Optional) Add reference images for I2V
4. ⏳ Run the training script (see FINETUNE_GUIDE.md)

## 💡 Tips

- More videos = better results (25+ recommended)
- Keep videos diverse (different actions, angles)
- Use consistent character descriptions in prompts
- Consider using an identifier token like "mychar" or "char5"

For detailed training instructions, see: `FINETUNE_GUIDE.md`
