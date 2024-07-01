import pyautogui

def take_screenshot(save_path):
    # Take screenshot
    screenshot = pyautogui.screenshot()
    
    # Save screenshot with specified file extension
    screenshot.save(save_path)
    print(f"Screenshot saved at {save_path}")

# Specify the path where you want to save the screenshot
save_path = "D:\Bot Generated FitLine Documents\PO\img.png"

# Call the function to take a screenshot and save it
take_screenshot(save_path)
