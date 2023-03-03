@echo off
set loop=0
:loop
"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe" -file intellij_javascript%loop%.csv -cmd python main.py intellij javascript
timeout 10
set /a loop=%loop%+1 
if "%loop%"=="10" goto next
goto loop

:next
