import cv2
import matplotlib.pyplot as plt

img = cv2.imread("labka.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th = 0
max_val = 255

ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

output = [img, o1, o2, o3, o4, o5]

titles = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()