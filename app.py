from flask import Flask, render_template
import pyautogui
import time

app = Flask(__name__)

@app.route('/')
def open_powershell_as_admin():
    # Simulate opening PowerShell as admin

    # Press Windows key
    pyautogui.hotkey('win')
    
    # Type 'powershell'
    time.sleep(1)
    pyautogui.write('powershell')
    
    # Wait for the search results to show up
    time.sleep(1)
    
    # Press Ctrl + Shift + Enter to open PowerShell as administrator
    pyautogui.hotkey('ctrl', 'shift', 'enter')
    
    # Wait for UAC prompt to appear
    time.sleep(2)  # Adjust as necessary for your system
    
    # Simulate typing 'cd ..' and pressing Enter
    pyautogui.write('cd ..')
    pyautogui.press('enter')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
