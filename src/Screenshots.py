import time
import logging
from PIL import ImageGrab
import os

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Path where to save the screenshots
screenshot_folder = "C:\\Users\\Goomie\\Documents\\Dev\\wow-bot-gpt\\screenshots\\"

# Capture frequency in seconds (increase this value to reduce resource consumption)
capture_frequency = 5

# Initialize variables for the last two captures
last_capture = None
current_capture = None

# Initialize capture type
capture_type = "last"  # Default type

# Loop to periodically capture the screen
while True:
    try:
        # Capture the screen for "current"
        if capture_type == "current":
            current_capture = ImageGrab.grab()
        else:
            last_capture = ImageGrab.grab()

        # Save the image with reduced resolution
        if capture_type == "current":
            current_capture.thumbnail((1280, 720))  # Reduce resolution to 720p
        else:
            last_capture.thumbnail((1280, 720))  # Reduce resolution to 720p

        # Create a file name based on capture type and timestamp
        file_name = f"{capture_type}_capture.png"

        # Save the capture with the generated file name
        if capture_type == "current":
            current_capture.save(os.path.join(
                screenshot_folder, file_name), "JPEG", quality=60)
        else:
            last_capture.save(os.path.join(screenshot_folder,
                              file_name), "JPEG", quality=60)

        # Log a message to indicate that the capture was done
        logging.info(
            f"{file_name} completed and saved in {screenshot_folder + file_name}")

        # Toggle the capture type
        if capture_type == "current":
            capture_type = "last"
        else:
            capture_type = "current"

        # Wait for the next capture
        time.sleep(capture_frequency)

    except Exception as e:
        # In case of error, log an error message
        logging.error(f"Error while capturing screen: {str(e)}")

    # You can add a condition to stop the loop if necessary
