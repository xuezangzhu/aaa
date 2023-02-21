
import pyautogui

def run():
    pyautogui.screenshot("filename.jpg")
    with open("filename.jpg","rb") as f:
        return f.read()
