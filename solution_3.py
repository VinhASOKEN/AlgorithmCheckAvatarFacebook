import cv2
import numpy as np

def extract_features(image):
    resized_image = cv2.resize(image, (224, 224))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors

def calculate_distance(des1, des2):
    if des1 is None or des2 is None:
        return float('inf')
    return np.linalg.norm(des1 - des2)

image1 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/11.360_f_349497933_ly4im8bdmhlalzgykg2f2yzovjjbtlw5.jpg')
# image2 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/11.360_f_349497933_ly4im8bdmhlalzgykg2f2yzovjjbtlw5.jpg')

image2 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/12.default-avatar-icon-of-social-media-user-vector.jpg')
kp1, des1 = extract_features(image1)
kp2, des2 = extract_features(image2)

d = calculate_distance(des1, des2)
print(d)
