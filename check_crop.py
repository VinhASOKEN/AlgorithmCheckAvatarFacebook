import cv2
import numpy as np
import os

def check_image_colors(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    unique_colors = np.unique(gray)
    if len(unique_colors) <= 100:
        print(image_path)
        print("Error")

folder_test = "/home1/data/vinhnguyen/CheckAvatar/cropped_images"
for img in os.listdir(folder_test):
    img_path = os.path.join(folder_test, img)
    check_image_colors(img_path)
