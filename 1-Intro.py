import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread('img/test.png')
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# pixel_value = img[100, 50]   # nilai satu piksel
# img_cropped = img[0:4, 0:4]  # potongan 4x4

print('tipe:', img.dtype)
print('shape:', img.shape)
print('max:', img.max())
print('min:', img.min())
print('mean:', img.mean())
# plt.imshow(img_cropped)
# plt.show()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img_bw)
x_gelap, y_gelap = min_loc
x_terang, y_terang = max_loc
potongan_gelap = img_bw[y_gelap : y_gelap+8, x_gelap : x_gelap+8]
potongan_terang = img_bw[y_terang : y_terang+8, x_terang : x_terang+8]
print(potongan_gelap)
print(potongan_terang)

plt.figure(1)
plt.imshow(potongan_gelap, cmap='gray', vmin=0, vmax=255)

plt.figure(2)
plt.imshow(potongan_terang, cmap='gray', vmin=0, vmax=255)
plt.show()

cv2.imshow('test image', img)
cv2.imshow('test image bw', img_bw)
cv2.waitKey(0)

cap = cv2.VideoCapture(0)

while True:
    ret, cam = cap.read()
    if not ret:
        break
    # img = cv2.imread('img/test.png')
    [h, w, c] = cam.shape

    # for i in range(h):
    #     for j in range(w):
    #         cam[i,j,0] = 0
    #         cam[i,j,1] = 0
    #         # cam[i,j,2] = 0

    cam[:, :, 2] = 0
    cam[:, :, 1] = 0

    cv2.imshow('test image', cam)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()