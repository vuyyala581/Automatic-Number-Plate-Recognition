# License Plate Recognition using OpenCV and EasyOCR

## Overview
This project uses OpenCV and EasyOCR to detect and recognize vehicle license plate numbers from images. The extracted text is then formatted according to the Indian vehicle registration format.

## Features
- Detects license plates in an image.
- Extracts text using Optical Character Recognition (OCR).
- Formats and displays the extracted text in the standard Indian license plate format.
- Highlights the detected license plate in the image.

## Prerequisites
Ensure that you have the following dependencies installed:

```bash
pip install opencv-python numpy imutils easyocr matplotlib
```

## File Structure
```
|-- project/
    |-- main.py  # The script containing the implementation
    |-- img-1.jpg  # Sample image containing a license plate
    |-- README.md  # Documentation for the project
```

## Usage
Run the script using the following command:

```bash
python main.py
```

## Code Explanation
1. **Load the Image:** Reads the input image containing a vehicle license plate.
2. **Preprocessing:** Converts the image to grayscale, applies noise reduction, and detects edges.
3. **Contour Detection:** Finds the potential license plate by detecting contours in the image.
4. **Extracting the Plate:** Uses contour approximation to locate the number plate region.
5. **OCR Processing:** EasyOCR extracts text from the detected plate region.
6. **Formatting Output:** The extracted text is formatted according to the Indian license plate structure.
7. **Displaying Results:** The license plate is highlighted in the image and the extracted text is printed.

## Output Format
Once the script runs successfully, it will print the detected license plate number and its formatted breakdown:

```
LICENSE PLATE NUMBER: MH20DV2366

License Plate Breakdown:
State Code: MH
RTO Code: 20
Unique Code: DV2366

In India, car number plates follow a format of two letters for the state/UT, two digits for the RTO/district, and then a unique alphanumeric code (letters and numbers).
Example: TN 01 AB 1234 (TN = Tamil Nadu, 01 = RTO code, AB = series, 1234 = unique number)
```

## Example Image Output
The detected license plate is highlighted and displayed using matplotlib.

## Troubleshooting
- Ensure that the image file path is correct.
- If the plate is not detected, try adjusting the contour approximation parameters.
- If the OCR result is incorrect, ensure that the image quality is good and the plate is clearly visible.

## Future Improvements
- Improve accuracy by training a custom OCR model.
- Extend support for multiple images or video stream processing.
- Implement a web-based interface for real-time license plate recognition.

## License
This project is open-source and can be modified or distributed freely.

