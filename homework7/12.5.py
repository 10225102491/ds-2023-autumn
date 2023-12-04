import torch
import torchvision.transforms as transforms
from PIL import Image

# 打开图片
picture = Image.open('picture.jpeg')

# 创建一个变换对象，该对象将图片转换为灰度，然后缩放到指定的尺寸
transform = transforms.Compose([
    transforms.Grayscale(),  # 转换为灰度图像
    transforms.Resize((256, 256))  # 缩放到指定的尺寸
])

# 应用变换
image = transform(picture)

# 显示图片
image.show()