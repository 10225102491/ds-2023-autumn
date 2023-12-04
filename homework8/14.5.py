import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
audio, fs = np.load('music.wav')

# 对音频进行傅里叶变换
fft_result = fftpack.fft(audio)

# 获取频率轴的值
freq = fftpack.fftfreq(len(audio), 1 / fs)

# 创建可视化图
plt.figure(figsize=(12, 6))

# 绘制原始音频的振幅
plt.subplot(2, 1, 1)
plt.plot(audio)
plt.title('Original Audio')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# 绘制傅里叶变换后的振幅和频率
plt.subplot(2, 1, 2)
plt.plot(np.abs(fft_result))  # 取绝对值以显示振幅
plt.plot(freq, np.abs(fft_result))  # 频率对数轴
plt.title('Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.yscale('log')  # 对数尺度以更好地显示不同振幅的频率

plt.tight_layout()
plt.show()