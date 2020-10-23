import matplotlib.pyplot as plt
from skimage import io

file_name = '/home/caozheng/Documents/lianxi/5-cv2/339--131243.jpg'
img=io.imread(file_name)

# -255.0 - 255.0  alpha -1.0 - 1.0
Increment = 80.0        # 增量参数
alpha = Increment/255.0  # alpha=1,全白；-1，全黑；0，不变

def Illumi_adjust(alpha, img):
    if alpha > 0 :
        img_out = img * (1 - alpha) + alpha * 255.0
    else:
        img_out = img * (1 + alpha)

    return img_out/255.0

img_out = Illumi_adjust(alpha, img)

plt.figure(1)
plt.imshow(img)         # 绘制
plt.axis('off')         # 不显示坐标尺寸

plt.figure(2)
plt.imshow(img_out)
plt.axis('off')

plt.show()              # 显示窗口