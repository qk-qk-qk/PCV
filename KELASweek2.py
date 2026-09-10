import cv2, numpy as np, matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break
    # img = cv2.imread('test.png')
    [h, w, c] = img.shape

    for i in range(h):
        for j in range(w):
            img[i,j,0] = 0
            img[i,j,1] = 0
            # img[i,j,2] = 0

    cv2.imshow('test image', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()