import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = cv2.imread('img/test.png', 0)

    mean_blur = cv2.blur(img, (5, 5))
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
    median_blur = cv2.medianBlur(img, 5)

    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)
    sobel_combined = np.clip(sobel_combined, 0, 255).astype(np.uint8)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = np.clip(np.abs(laplacian), 0, 255).astype(np.uint8)

    titles = [
        'Citra Original', 
        'Mean Blur (5x5)', 
        'Gaussian Blur (5x5)', 
        'Median Blur (5)', 
        'Sobel Edge', 
        'Laplacian'
    ]
    images = [img, mean_blur, gaussian_blur, median_blur, sobel_combined, laplacian]

    plt.figure(figsize=(12, 8))
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i], fontsize=10)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()