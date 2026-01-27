import os

dataset_path = '/kaggle/input/fer2013'
train_path = '/kaggle/input/fer2013/train'
emotions = os.listdir(train_path)

print(f"--- STATISTIC RELATORY (FER-2013) ---")
print(f"{'EMOTION':<15} | {'QUANTITY'}")
print("-" * 30)
grand_total = 0 

for emotion in emotions:
    folder_path = os.path.join(train_path, emotion)
    quantity = len(os.listdir(folder_path))
    grand_total += quantity
    print(f"{emotion:<15} | {quantity}")

print("-" * 30)
