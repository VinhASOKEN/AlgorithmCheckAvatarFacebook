# Algorithm Check Avatar Facebook

This project aims to classify Facebook avatar images into two categories: 
1. **None** - the default white silhouette image displayed when a user hasn't updated their Facebook profile picture.
2. **Normal** - any user-uploaded profile picture.

## Solutions

The project includes three different solutions for classification:

### Solution 1: Histogram-Based Algorithm
My custom algorithm leverages histogram analysis to differentiate between the "None" image and normal profile pictures. It has shown the best classification results among the three solutions. The algorithm runs efficiently, providing fast performance without the need for heavy AI models, while maintaining a solid accuracy rate.

### Solution 2: HOG Feature Extraction
This solution employs Histogram of Oriented Gradients (HOG) feature extraction for image classification. HOG is known for its effectiveness in capturing edge and gradient structures in images.

### Solution 3: SIFT Feature Extraction
In this approach, I utilize the SIFT (Scale-Invariant Feature Transform) algorithm. SIFT is robust for detecting and describing local features in images, making it suitable for our classification task.

## Performance
The algorithms are designed to run quickly, ensuring a seamless user experience. Users can run the provided script `solution_1.py` to test the accuracy and frames per second (FPS) performance of the histogram-based algorithm.

## Getting Started
To get started with the project, clone the repository and run the solution scripts.
