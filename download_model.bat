@echo off
echo ========================================
echo Download CogVideoX Models Manually
echo ========================================
echo.
echo Choose which model to download:
echo.
echo 1. CogVideoX-5B-I2V (Recommended) - 25GB
echo    - Image-to-Video generation
echo    - Resolution: 480x720
echo    - Best for character animation
echo.
echo 2. CogVideoX1.5-5B-I2V (Higher Quality) - 30GB
echo    - Image-to-Video generation
echo    - Resolution: 768x1360
echo    - Better quality, more VRAM needed
echo.
echo 3. Both models - 55GB
echo.
echo NOTE: You need HuggingFace CLI installed
echo Install it with: pip install huggingface_hub[cli]
echo.
pause

set /p choice="Enter your choice (1, 2, or 3): "

if "%choice%"=="1" (
    echo.
    echo Downloading CogVideoX-5B-I2V...
    huggingface-cli download THUDM/CogVideoX-5b-I2V --local-dir "./local_models/CogVideoX-5B-I2V"
) else if "%choice%"=="2" (
    echo.
    echo Downloading CogVideoX1.5-5B-I2V...
    huggingface-cli download THUDM/CogVideoX1.5-5b-I2V --local-dir "./local_models/CogVideoX1.5-5B-I2V"
) else if "%choice%"=="3" (
    echo.
    echo Downloading both models...
    echo This will take a long time and require 55GB+ disk space.
    huggingface-cli download THUDM/CogVideoX-5b-I2V --local-dir "./local_models/CogVideoX-5B-I2V"
    huggingface-cli download THUDM/CogVideoX1.5-5b-I2V --local-dir "./local_models/CogVideoX1.5-5B-I2V"
) else (
    echo.
    echo Invalid choice. Please run again and enter 1, 2, or 3.
)

echo.
echo Download complete!
echo Models saved to: .\local_models\
pause
