@echo off
echo ========================================
echo Fine-Tune CogVideoX on Your Characters
echo ========================================
echo.
echo This will start training CogVideoX on your custom character dataset.
echo.
echo Before running this script:
echo 1. Add your training videos to: my_characters_dataset\videos\
echo 2. Update prompts.txt to match your videos
echo 3. (Optional) Add reference images to: my_characters_dataset\images\
echo.
echo Training will take 2-6 hours depending on your GPU.
echo.
pause

echo.
echo Starting training...
echo.

cd finetune

REM For Image-to-Video fine-tuning with LoRA
call train_ddp_i2v.sh

pause
