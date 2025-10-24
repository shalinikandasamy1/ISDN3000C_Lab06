# ISDN3000C Lab 06 - Camera Exercise: GPIO, Button, LED, and OpenCV on RDK X-5

## Group Members
- Shalini Kandasamy
- Saanvi Ravi Katyayan

## Overview
This lab exercise demonstrates interfacing the RDK X-5 development board's GPIO pins with physical components (a push button and an LED) and integrating USB camera functions using Python and OpenCV. The program captures an image on button press, applies the Canny edge detection algorithm, and saves both the original and processed images. The LED lights up briefly to indicate a successful capture.

## Circuit Setup
- **LED:**
  - Connect LED anode (+, longer leg) through a 220Ω resistor to **Pin 31 (GPIO6)**
  - Connect LED cathode (-, shorter leg) to **Ground (e.g., Pin 6)**
- **Push Button:**
  - One side to **3.3V pin (Pin 1)**
  - Other side to **Pin 13 (GPIO27)**
  
See the circuit picture (![Alt text](media/circuit_photos.JPG)) in  'media' folder for reference.

## Software Setup
1. Install virtualenv and create a virtual environment with system packages to access `Hobot.GPIO`.
2. Inside the virtual environment, install OpenCV and numpy:
   ```
   pip install opencv-python numpy
   ```
3. Use the script `camera.py` (included in this repo) that:
   - Initializes GPIO pins and camera
   - Detects button press to capture an image
   - Applies Canny edge detection on the captured frame
   - Saves the original and edges images to uniquely named files
   - Lights the LED for 0.5 seconds as confirmation
   - Cleans up GPIO and releases camera resource on exit

## Running the Program
```
python3 camera.py
```

Press the button to take a photo. The LED will flash to confirm the action, and images will be saved in the working directory.

## Files
- `camera.py` — Main Python script for the exercise
- `circuit_photo.jpg` — Photo of the assembled circuit on breadboard

## Safety and Notes
- Discharge static before handling the board and components.
- Use a current-limiting resistor (220Ω) with the LED.
- Confirm all wiring before powering the board.
- Button uses internal pull-down resistor for simple wiring.

## Submission
- Circuit picture is included above
- Python scripts uploaded to the GitHub repository: `ISDN3000C_Lab06`
- Requirements listed in `requirements.txt`

