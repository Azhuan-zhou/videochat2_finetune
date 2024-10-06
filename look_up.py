import torch

# 加载 .pth 文件
model_weights = torch.load('/root/autodl-tmp/video_chat2/ckpt/stage4/videochat2_hd_mistral_7b_stage4.pth')

# 查看文件内容，通常会看到一个字典
print(model_weights.keys())