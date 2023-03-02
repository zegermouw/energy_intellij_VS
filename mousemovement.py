import time
import subprocess
import pyautogui
import time
import sys

pyautogui.PAUSE = 2

if(sys.argv[1] == "vs"):
    program_path = r'"C:\Users\zeger\AppData\Local\Programs\Microsoft VS Code\Code.exe"'

if(sys.argv[1] == "intellij"):
    program_path = r'"C:\Program Files\JetBrains\IntelliJ IDEA 2022.2.3\bin\idea64.exe"'

if(sys.argv[2] == "python"):
    script_path = "testcode.py"
if(sys.argv[2] == "javascript"):
    script_path = "server.js"
if(sys.argv[2] == "java"):
    script_path = "Main.java"



command1 = f"{program_path} {script_path} --wait"
# command2 =
print(command1)

try:
    result = subprocess.Popen(command1, stdout=subprocess.PIPE, universal_newlines=True)
    if(sys.argv[1] == "vs"):
        for stdout_line in iter(result.stdout.readline, ""):
            print(stdout_line)
            if "successfully created" in stdout_line:
                if(sys.argv[2] == "python"):
                    pyautogui.hotkey('ctrl', 'shit', 'p')
                    pyautogui.write('>python: run python file in terminal')
                    pyautogui.press('enter')
                if(sys.argv[2] == "javascript"):
                    pyautogui.hotkey('ctrl', 'alt', 'n')
                if(sys.argv[2] == "java"):
                    pyautogui.hotkey('ctrl', 'alt', 'n')
                # pyautogui.click(1800,60)
        result.stdout.close()
        return_code = result.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
    if(sys.argv[1] == "intellij"):
        for stdout_line in iter(result.stdout.readline, ""):
            if "RdCoroutineScope" in stdout_line:
                time.sleep(10)
                if(sys.argv[2] == "python"):
                    pyautogui.hotkey('alt', 'f12')
                    pyautogui.write("python testcode.py intellij")
                    pyautogui.press('enter')
                if(sys.argv[2] == "javascript"):
                    pyautogui.hotkey('alt', 'f12')
                    pyautogui.write("node server.js intellij")
                    pyautogui.press('enter')
                if(sys.argv[2] == "java"):
                    pyautogui.hotkey('alt', 'f12')
                    pyautogui.write("javac Main.java ; java Main intellij")
                    pyautogui.press('enter')

except subprocess.CalledProcessError as err:
    print(err.stderr)
