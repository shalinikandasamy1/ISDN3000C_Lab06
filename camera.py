import Hobot.GPIO as GPIO
import cv2
import time

LED_PIN = 31      # LED on physical Pin 31 as per lab instructions
BUTTON_PIN = 13   # Button on physical Pin 13

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN)

    cap = cv2.VideoCapture(0)  # Open default USB camera
    print("Ready")

    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.HIGH:  # Button pressed
                print("Button Pressed! Capturing...")
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED

                ret, frame = cap.read()
                if not ret:
                    print("Failed to capture frame!")
                    GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
                    time.sleep(0.5)
                    continue

                # Convert to grayscale and apply Canny edge detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 100, 200)

                timestamp = int(time.time())
                original_filename = f"original_{timestamp}.jpg"
                edges_filename = f"edges_{timestamp}.jpg"

                # Save images
                cv2.imwrite(original_filename, frame)
                cv2.imwrite(edges_filename, edges)

                print(f"Saved {original_filename} and {edges_filename}")

                time.sleep(0.5)  # Keep LED on half a second
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED

                # Wait until button released to avoid multiple captures
                while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                    time.sleep(0.1)

            time.sleep(0.1)  # Poll delay

    except KeyboardInterrupt:
        print("Cleaning up...")

    finally:
        cap.release()
        GPIO.cleanup()
        print("Done")

if __name__ == "__main__":
    main()
