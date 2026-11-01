import time
import pyautogui

# Global automation safety settings
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

TARGET_IMAGE = "menu_bar_insert.png"


def click_target_button(image_path, confidence_level=0.8):
    """
    Scans the live screen for a target image template.
    If found, moves the cursor to its center coordinates and executes a click.
    Returns True if clicked successfully, or False if the image is missing.
    """
    try:
        # 1. Capture and locate image with fuzzy matching parameters
        button_location = pyautogui.locateOnScreen(
            image_path, confidence=confidence_level, grayscale=True
        )

        # 2. Extract center target and execute action pipeline
        button_center = pyautogui.center(button_location)
        print(f"Button at {button_location}")

        # Refactored pipeline with an explicit tracking pause
        pyautogui.moveTo(button_center.x, button_center.y, duration=0.5)
        time.sleep(0.2)  # Give the OS a moment to recognize the cursor focus
        pyautogui.mouseDown()
        time.sleep(0.1)  # Simulate holding the mouse down briefly
        pyautogui.mouseUp()
        return True

    except (pyautogui.ImageNotFoundException, TypeError):
        # Gracefully handle missing target assets without breaking execution
        return False


# --- MAIN AUTOMATION EVENT LOOP ---
print("Bot starting in 3 seconds... Switch to your target window.")
time.sleep(3)

while True:
    try:
        # Call the target button function
        if click_target_button(TARGET_IMAGE, confidence_level=0.8):
            print(f"click_target_button True")

            # Perform sequential secondary actions immediately after a successful click
            pyautogui.write("Action completed!", interval=0.1)
            pyautogui.press("enter")

            # Cool-down period to prevent spamming actions
            time.sleep(2)
        else:
            print("Searching for target...")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nBot stopped manually.")
        break

