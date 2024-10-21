import cv2
import numpy as np
from scipy.spatial import distance

def calculate_hog_feature(image):
    resized_image = cv2.resize(image, (224, 224))
    hog = cv2.HOGDescriptor()
    hog_feature = hog.compute(resized_image)
    hog_feature = hog_feature.flatten()
    
    return hog_feature

def hog_cosine_distance(feature1, feature2):
    feature1_normalized = feature1 / np.linalg.norm(feature1)
    feature2_normalized = feature2 / np.linalg.norm(feature2)
    
    cosine_dist = distance.cosine(feature1_normalized, feature2_normalized)
    
    return cosine_dist

image1 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/11.360_f_349497933_ly4im8bdmhlalzgykg2f2yzovjjbtlw5.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/11.360_f_349497933_ly4im8bdmhlalzgykg2f2yzovjjbtlw5.jpg', cv2.IMREAD_GRAYSCALE)

# image2 = cv2.imread('/home1/data/vinhnguyen/CheckAvatar/none_data/positive/12.default-avatar-icon-of-social-media-user-vector.jpg', cv2.IMREAD_GRAYSCALE)

hog_feature1 = calculate_hog_feature(image1)
hog_feature2 = calculate_hog_feature(image2)

cosine_distance = hog_cosine_distance(hog_feature1, hog_feature2)
print(cosine_distance)