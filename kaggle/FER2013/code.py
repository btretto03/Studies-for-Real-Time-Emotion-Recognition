import os
import matplotlib.pyplot as plt
from PIL import Image

dataset_path = '/kaggle/input/fer2013'
train_path = '/kaggle/input/fer2013/train'
emotions = os.listdir(train_path)

plt.figure(figsize=(12, 8))

for i, emotion in enumerate(emotions):
    emotion_direc = os.path.join(train_path, emotion) #current emotion
    file_name = os.listdir(emotion_direc)[0] 
    complete_path = os.path.join(emotion_direc, file_name)
    img = Image.open(complete_path)

    plt.subplot(3, 3, i + 1) #take the figure we had and divide it in 3x3 squares
    plt.imshow(img, cmap='gray')
    plt.title(emotion, fontsize=14, fontweight='bold')
    plt.axis('off')

plt.tight_layout()
plt.show()