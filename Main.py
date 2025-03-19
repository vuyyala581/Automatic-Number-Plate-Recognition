import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('/content/y.png')
if img is None:
    raise ValueError("Image not found. Check the file path.")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Noise reduction and edge detection
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(bfilter, 30, 200)

# Find contours
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Identify the license plate region
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

if location is None:
    raise ValueError("License plate not found!")

# Create a mask and extract the license plate
mask = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask, [location], 0, 255, -1)
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Crop the license plate region
(x, y) = np.where(mask == 255)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)
cropped_image = gray[x1:x2+1, y1:y2+1]

# OCR to extract text
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
if not result:
    raise ValueError("No text detected on the license plate!")

text = result[0][-2]

# Draw the recognized text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0), 3)

# Display the final output
plt.figure(figsize=(10,5))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

print("LICENSE PLATE NUMBER:", text)

# Format output to match Indian license plate structure
if len(text) >= 4:
    state_code = text[:2]
    rto_code = text[2:4]
    unique_code = text[4:]
    print("\nLicense Plate Breakdown:")
    print(f"State Code: {state_code}")
    print(f"RTO Code: {rto_code}")
    print(f"Unique Code: {unique_code}")
    print("\nIn India, car number plates follow a format of two letters for the state/UT, two digits for the RTO/district, and then a unique alphanumeric code (letters and numbers).")
    print("Example: TN 01 AB 1234 (TN = Tamil Nadu, 01 = RTO code, AB = series, 1234 = unique number)")
