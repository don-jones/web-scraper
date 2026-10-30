import time
import pyautogui

# Set a safety pause so you can move your mouse to the corner to abort the bot
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

print("Bot starting in 3 seconds... Switch to your target window.")
time.sleep(3)

# The element your bot is looking for (save a small cropped PNG of the target element)
TARGET_IMAGE = "target_button.png"

while True:
    try:
        # 1. LIVE SCREEN CAPTURE & MATCHING
        # confidence require 'opencv-python' to be installed for fuzzy/imperfect matching
        button_location = pyautogui.locateOnScreen(TARGET_IMAGE, confidence=0.8)
        
        if button_location is not None:
            #print(f"Target found at: {button_location}")
            
            # 2. DECISION & ACTION PIPELINE
            # Get the center coordinates of the found image
            button_center = pyautogui.center(button_location)
            
            # Move mouse and click
            pyautogui.moveTo(button_center.x, button_center.y, duration=0.2)
            pyautogui.click()
            
            # Perform a series of follow-up actions
            pyautogui.write("Action completed!", interval=0.1)
            pyautogui.press("enter")
            
            # Pause to prevent spamming the action
            time.sleep(2)
            
        else:
            print("Searching for target...")
            time.sleep(0.5) # Wait half a second before capturing the screen again
            
    except KeyboardInterrupt:
        print("\nBot stopped manually.")
        break

