import cv2
import numpy as np
import matplotlib.pyplot as plt

def img_negatif(image):
    tinggi, lebar = image.shape
    hasil = np.zeros((tinggi, lebar), dtype=np.uint8)
    
    for i in range(tinggi):
        for j in range(lebar):
            intensitas_asli = image[i, j]
            hasil[i, j] = 255 - intensitas_asli
            
    return hasil

def img_ekualisasi(image):
    tinggi, lebar = image.shape
    total_piksel = tinggi * lebar
    
    hist = [0] * 256
    for i in range(tinggi):
        for j in range(lebar):
            intensitas = image[i, j]
            hist[intensitas] += 1
            
    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]
        
    cdf_min = 0
    for val in cdf:
        if val > 0:
            cdf_min = val
            break
            
    map_table = [0] * 256
    for i in range(256):
        map_table[i] = round(((cdf[i] - cdf_min) / (total_piksel - cdf_min)) * 255)
        
    hasil = np.zeros((tinggi, lebar), dtype=np.uint8)
    for i in range(tinggi):
        for j in range(lebar):
            intensitas_asli = image[i, j]
            hasil[i, j] = map_table[intensitas_asli]
            
    return hasil

img = cv2.imread('img/test.png', cv2.IMREAD_GRAYSCALE)
    
citra_negatif = img_negatif(img)
citra_ekualisasi = img_ekualisasi(img)
    
plt.figure(figsize=(15, 5))
    
plt.subplot(1, 3, 1)
plt.title("Citra Asli")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    
plt.subplot(1, 3, 2)
plt.title("Transformasi Intensitas (Negatif)")
plt.imshow(citra_negatif, cmap='gray', vmin=0, vmax=255)
    
plt.subplot(1, 3, 3)
plt.title("Ekualisasi Histogram")
plt.imshow(citra_ekualisasi, cmap='gray', vmin=0, vmax=255)
    
plt.show()