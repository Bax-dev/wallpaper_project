import os
import ctypes
import random
import schedule
import time
from PIL import Image

# Path to your wallpapers directory
wallpapers_dir = r"C:\Users\user\Documents\Wallpaper"

def set_wallpaper(image_path):
    
    bmp_image = Image.open(image_path)
    bmp_image_path = image_path.replace('.jpg', '.bmp')
    bmp_image.save(bmp_image_path, 'BMP')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, bmp_image_path, 3)

def change_wallpaper():
    wallpapers = [os.path.join(wallpapers_dir, f) for f in os.listdir(wallpapers_dir) if f.endswith(('.jpg', '.png'))]
    if wallpapers:
        wallpaper = random.choice(wallpapers)
        set_wallpaper(wallpaper)
        print(f"Wallpaper changed to: {wallpaper}")
    else:
        print("No wallpapers found in the directory.")

# Schedule the wallpaper change every 5 seconds
schedule.every(5).seconds.do(change_wallpaper)

if __name__ == "__main__":
    change_wallpaper()  # Set the initial wallpaper
    while True:
        schedule.run_pending()
        time.sleep(1)
