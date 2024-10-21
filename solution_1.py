import os
import cv2
import numpy as np
import time

def count_ranges(histogram):
    num_ranges = 0
    is_increasing = True

    count = 0
    start = -1
    end = -1
        
    for i, value in enumerate(histogram):
        if int(value) >= 0 and start == -1:
            start = i
        elif int(value) <= 5 and start != -1:
            end = i
            if end - start < 70:
                count += 1
            start = -1
            end = -1
        
        try:
            if histogram[i] < histogram[i + 4]:
                is_increasing = True
            elif histogram[i] > histogram[i + 4]:
                if is_increasing:
                    num_ranges += 1
                is_increasing = False
        except:
            continue

    if is_increasing:
        num_ranges += 1

    return num_ranges, count


def run(image_folder):
    maxx = 0
    num_frames = 0
    start_time = time.time()

    for filename in os.listdir(image_folder):
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
        num_ranges, count = count_ranges(histogram)
        num_frames += 1
    
        if num_ranges <= 8:
            maxx += 1
        elif num_ranges >= 12 and count >= 41:
            maxx += 1
        else:
            continue
            
    end_time = time.time()

    fps = num_frames / (end_time - start_time)
    print(fps)
    print(maxx, len(os.listdir(image_folder)))

image_folder_neg = '/home1/data/vinhnguyen/CheckAvatar/none_data/negative'
image_folder_pos = '/home1/data/vinhnguyen/CheckAvatar/none_data/positive'

# run(image_folder_neg)
run(image_folder_pos)