# CogVideoX1.5-5B-I2V

<p style="text-align: center;">
  <div align="center">
  <img src=https://github.com/THUDM/CogVideo/raw/main/resources/logo.svg width="50%"/>
  </div>
  <p align="center">
  <a href="https://huggingface.co/THUDM/CogVideoX1.5-5B-I2V/blob/main/README.md">📄 Read in English</a> | 
  <a href="https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space">🤗 Huggingface Space</a> |
  <a href="https://github.com/THUDM/CogVideo">🌐 Github </a> | 
  <a href="https://arxiv.org/pdf/2408.06072">📜 arxiv </a>
</p>
<p align="center">
📍 前往<a href="https://chatglm.cn/video?fr=osm_cogvideox"> 清影</a> 和 <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9"> API平台</a> 体验商业版视频生成模型
</p>

## 模型介绍

CogVideoX是 [清影](https://chatglm.cn/video?fr=osm_cogvideo) 同源的开源版本视频生成模型。下表展示我们在本代提供的视频生成模型列表相关信息:

<table  style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">模型名</th>
    <th style="text-align: center;">CogVideoX1.5-5B</th>
    <th style="text-align: center;">CogVideoX1.5-5B-I2V (当前仓库)</th>
  </tr>
  <tr>
    <td style="text-align: center;">视频分辨率</td>
    <td colspan="1" style="text-align: center;">1360 * 768</td>
    <td colspan="1" style="text-align: center;"> Min(W, H) = 768 <br> 768 ≤ Max(W, H) ≤ 1360 <br> Max(W, H) % 16 = 0 </td>
    </tr>
  <tr>
    <td style="text-align: center;">推理精度</td>
    <td colspan="2" style="text-align: center;"><b>BF16(推荐)</b>, FP16, FP32，FP8*，INT8，不支持INT4</td>
  </tr>
  <tr>
    <td style="text-align: center;">单GPU显存消耗</td>
    <td colspan="2"  style="text-align: center;"><b>BF16: 9GB minimum*</b></td>
  </tr>
  <tr>
    <td style="text-align: center;">多GPU显存消耗</td>
    <td colspan="2" style="text-align: center;"><b>BF16: 24GB* using diffusers</b><br></td>
  </tr>
  <tr>
    <td style="text-align: center;">推理速度<br>(Step = 50, FP/BF16)</td>
    <td colspan="2" style="text-align: center;">单卡A100: ~1000秒(5秒视频)<br>单卡H100: ~550秒(5秒视频)</td>
  </tr>
  <tr>
    <td style="text-align: center;">提示词语言</td>
    <td colspan="5" style="text-align: center;">English*</td>
  </tr>
  <tr>
    <td style="text-align: center;">提示词长度上限</td>
    <td colspan="2" style="text-align: center;">224 Tokens</td>
  </tr>
  <tr>
    <td style="text-align: center;">视频长度</td>
    <td colspan="2" style="text-align: center;">5 秒 或 10 秒</td>
  </tr>
  <tr>
    <td style="text-align: center;">帧率</td>
    <td colspan="2" style="text-align: center;">16 帧 / 秒 </td>
  </tr>
</table>

**数据解释**

+ 使用 diffusers 库进行测试时，启用了全部`diffusers`库自带的优化，该方案未测试在非**NVIDIA A100 / H100**
  外的设备上的实际显存 / 内存占用。通常，该方案可以适配于所有 **NVIDIA 安培架构**
  以上的设备。若关闭优化，显存占用会成倍增加，峰值显存约为表格的3倍。但速度提升3-4倍左右。你可以选择性的关闭部分优化，这些优化包括:

```
pipe.enable_sequential_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()
```

+ 多GPU推理时，需要关闭 `enable_sequential_cpu_offload()` 优化。
+ 使用 INT8 模型会导致推理速度降低，此举是为了满足显存较低的显卡能正常推理并保持较少的视频质量损失，推理速度大幅降低。
+ [PytorchAO](https://github.com/pytorch/ao) 和 [Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
  可以用于量化文本编码器、Transformer 和 VAE 模块，以降低 CogVideoX 的内存需求。这使得在较小显存的 GPU
  上运行模型成为可能！同样值得注意的是，TorchAO 量化完全兼容 `torch.compile`，这可以显著提高推理速度。在 `NVIDIA H100`
  及以上设备上必须使用 `FP8` 精度，这需要源码安装 `torch`、`torchao`、`diffusers` 和 `accelerate` Python
  包。建议使用 `CUDA 12.4`。
+ 推理速度测试同样采用了上述显存优化方案，不采用显存优化的情况下，推理速度提升约10%。 只有`diffusers`版本模型支持量化。
+ 模型仅支持英语输入，其他语言可以通过大模型润色时翻译为英语。

**提醒**

+ 使用 [SAT](https://github.com/THUDM/SwissArmyTransformer) 推理和微调SAT版本模型。欢迎前往我们的github查看。

## 快速上手 🤗

本模型已经支持使用 huggingface 的 diffusers 库进行部署，你可以按照以下步骤进行部署。

**我们推荐您进入我们的 [github](https://github.com/THUDM/CogVideo) 并查看相关的提示词优化和转换，以获得更好的体验。**

1. 安装对应的依赖

```shell
# diffusers>=0.32.0dev (or from source)
# transformers>=4.46.2
# accelerate>=1.1.1
# imageio-ffmpeg>=0.5.1
pip install --upgrade transformers accelerate diffusers imageio-ffmpeg 
```

2. 运行代码

```python 
import torch
from diffusers import CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    torch_dtype=torch.bfloat16
)

pipe.enable_sequential_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

## Quantized Inference

[PytorchAO](https://github.com/pytorch/ao) 和 [Optimum-quanto](https://github.com/huggingface/optimum-quanto/)
可以用于对文本编码器、Transformer 和 VAE 模块进行量化，从而降低 CogVideoX 的内存需求。这使得在免费的 T4 Colab 或较小 VRAM 的
GPU 上运行该模型成为可能！值得注意的是，TorchAO 量化与 `torch.compile` 完全兼容，这可以显著加快推理速度。

```python
# To get started, PytorchAO needs to be installed from the GitHub source and PyTorch Nightly.
# Source and nightly installation is only required until the next release.

import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXTransformer3DModel, CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image
from transformers import T5EncoderModel
from torchao.quantization import quantize_, int8_weight_only

quantization = int8_weight_only

text_encoder = T5EncoderModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="text_encoder", torch_dtype=torch.bfloat16)
quantize_(text_encoder, quantization())

transformer = CogVideoXTransformer3DModel.from_pretrained("THUDM/CogVideoX1.5-5B-I2V",subfolder="transformer", torch_dtype=torch.bfloat16)
quantize_(transformer, quantization())

vae = AutoencoderKLCogVideoX.from_pretrained("THUDM/CogVideoX1.5-5B-I2V", subfolder="vae", torch_dtype=torch.bfloat16)
quantize_(vae, quantization())

# Create pipeline and run inference
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    text_encoder=text_encoder,
    transformer=transformer,
    vae=vae,
    torch_dtype=torch.bfloat16,
)

pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()

prompt = "A little girl is riding a bicycle at high speed. Focused, detailed, realistic."
image = load_image(image="input.jpg")
video = pipe(
    prompt=prompt,
    image=image,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=81,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

此外，这些模型可以通过使用PytorchAO以量化数据类型序列化并存储，从而节省磁盘空间。你可以在以下链接中找到示例和基准测试。

- [torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
- [quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)

## 深入研究

欢迎进入我们的 [github](https://github.com/THUDM/CogVideo)，你将获得：

1. 更加详细的技术细节介绍和代码解释。
2. 提示词的优化和转换。
3. 模型推理和微调的详细代码。
4. 项目更新日志动态，更多互动机会。
5. CogVideoX 工具链，帮助您更好的使用模型。
6. INT8 模型推理代码。

## 模型协议

该模型根据 [CogVideoX LICENSE](LICENSE) 许可证发布。

## 引用

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```