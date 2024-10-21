import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_and_save_histogram(image_path, save_folder):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    print(image_path)

    
    plt.figure()
    plt.plot(histogram)
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    image_name = os.path.basename(image_path)
    histogram_path = os.path.join(save_folder, f'{os.path.splitext(image_name)[0]}_histogram.png')
    plt.savefig(histogram_path)
    plt.close()

def generate_histograms_for_images(image_folder, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            plot_and_save_histogram(image_path, save_folder)

image_folder = '/home1/data/vinhnguyen/CheckAvatar/data/positive'
save_folder = '/home1/data/vinhnguyen/CheckAvatar/positive_histogram'

generate_histograms_for_images(image_folder, save_folder)
