
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\Users\acer\Downloads\yasan.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(1,2,2)
plt.imshow(gray,cmap="gray")
plt.title("Gray Image")
plt.axis("off")
plt.show()
# Basic Global Thresholding using Iterative Threshold Selection

rows, cols = gray.shape

# Initial Threshold = Average intensity
T = np.mean(gray)

while True:

    G1 = gray[gray >= T]     # Foreground
    G2 = gray[gray < T]      # Background

    # Prevent division by zero
    if len(G1) == 0 or len(G2) == 0:
        break

    m1 = np.mean(G1)
    m2 = np.mean(G2)

    new_T = (m1 + m2) / 2

    # Stop when threshold converges
    if abs(new_T - T) < 1:
        break

    T = new_T

print("Optimal Threshold =", int(T))

# Create empty output image
binary = np.zeros(gray.shape, dtype=np.uint8)

rows, cols = gray.shape
# Basic Thresholding
for i in range(rows):
    for j in range(cols):
        if gray[i,j] >= T:
            binary[i,j] = 255
        else:
            binary[i,j] = 0

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Gray Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(binary,cmap='gray')
plt.title("Basic Global Thresholding")
plt.axis("off")

plt.show()
hist = np.zeros(256)

rows, cols = gray.shape

for i in range(rows):
    for j in range(cols):
        hist[gray[i,j]] += 1
total = rows * cols

sum_total = 0

for i in range(256):
    sum_total += i * hist[i]

sumB = 0
wB = 0
maximum = 0
threshold = 0

for t in range(256):

    wB += hist[t]

    if wB == 0:
        continue

    wF = total - wB

    if wF == 0:
        break

    sumB += t * hist[t]

    mB = sumB / wB
    mF = (sum_total - sumB) / wF

    between = wB * wF * ((mB - mF) ** 2)

    if between > maximum:
        maximum = between
        threshold = t

print("Otsu Threshold =", threshold)
otsu = np.zeros(gray.shape, dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if gray[i,j] >= threshold:
            otsu[i,j] = 255
        else:
            otsu[i,j] = 0

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Gray Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(otsu,cmap='gray')
plt.title("Otsu Thresholding")
plt.axis("off")

plt.show()
window = 11
C = 5

pad = window // 2

padded = np.pad(gray, pad, mode='reflect')

adaptive = np.zeros(gray.shape, dtype=np.uint8)

rows, cols = gray.shape

for i in range(rows):

    for j in range(cols):

        local = padded[i:i+window, j:j+window]

        mean = np.mean(local)

        if gray[i,j] > (mean - C):
            adaptive[i,j] = 255
        else:
            adaptive[i,j] = 0
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Gray Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(adaptive,cmap='gray')
plt.title("Adaptive Mean Thresholding")
plt.axis("off")

plt.show()
plt.figure(figsize=(15,8))

plt.subplot(2,2,1)
plt.imshow(gray,cmap='gray')
plt.title("Gray Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(binary,cmap='gray')
plt.title("Basic Thresholding")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(otsu,cmap='gray')
plt.title("Otsu Thresholding")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(adaptive,cmap='gray')
plt.title("Adaptive Mean Thresholding")
plt.axis("off")

plt.tight_layout()
plt.show()