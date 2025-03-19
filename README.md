# License Plate Recognition using OpenCV and EasyOCR

## Overview
This project extracts and recognizes text from vehicle license plates using OpenCV for image processing and EasyOCR for Optical Character Recognition (OCR). The recognized license plate is formatted according to the Indian vehicle registration system.

## Features
- Detects and extracts the license plate from an image.
- Uses OCR to recognize text from the extracted license plate.
- Formats the extracted text to match Indian license plate conventions.
- Highlights and displays the recognized license plate on the original image.

## Requirements
Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
opencv-python
numpy
imutils
matplotlib
easyocr
```

## How to Run the Code
1. Clone the repository or download the script.
2. Ensure you have Python installed (Python 3.x recommended).
3. Place the image containing the license plate in the specified path.
4. Run the script using the command:
   
   ```bash
   python license_plate_recognition.py
   ```
   
5. The recognized license plate text and its formatted breakdown will be displayed in the console.
6. The script will display an image with the recognized license plate highlighted.

## Expected Output Format
After running the script, the extracted license plate text is printed in the following format:

```
LICENSE PLATE NUMBER: MH20DV2366

License Plate Breakdown:
State Code: MH
RTO Code: 20
Unique Code: DV2366

In India, car number plates follow a format of two letters for the state/UT, two digits for the RTO/district, and then a unique alphanumeric code (letters and numbers).
Example: TN 01 AB 1234 (TN = Tamil Nadu, 01 = RTO code, AB = series, 1234 = unique number)
```

## Notes
- Ensure that the image provided contains a clear and visible license plate for better accuracy.
- Modify the image path in the script if necessary.
- If no text is detected, try adjusting the image quality or OCR settings.

## Author
Vuyyala Kavya

