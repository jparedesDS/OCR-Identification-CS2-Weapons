# OCR Weapon Detection in Counter-Strike 2

This project captures the screen and detects weapon names in Counter-Strike 2 using Optical Character Recognition (OCR). It preprocesses the captured image, applies OCR with Tesseract, and extracts weapon names from a predefined list.

## Features
- Captures the screen in real-time
- Applies image preprocessing to enhance text recognition
- Uses Tesseract OCR to extract text from the image
- Detects specific weapon names from a predefined list

## Installation
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- OpenCV
- NumPy
- Tesseract OCR
- MSS

### Install Dependencies
```sh
pip install opencv-python numpy pytesseract mss
```

### Tesseract Installation
You must have Tesseract installed on your system. Download it from:
[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

After installation, ensure `pytesseract` can locate the Tesseract executable by setting its path:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Modify as needed
```

## Usage
Run the script to start capturing the screen and detecting weapon names:
```sh
python script.py
```

Press `Z` to exit the application.

## Code Overview
- **process_frame(frame)**: Enhances the image for better text recognition.
- **detect_text(frame)**: Extracts text from the image and matches weapon names.
- **Screen capture loop**: Continuously captures a region of the screen, applies preprocessing, and detects text.

## Weapons Detected
- AK-47
- M4A1-S
- M4A1
- AWP
- FAMAS
- Galil
- Desert Eagle
- USP-S
- Glock-18

## License
This project is open-source and available under the MIT License.

