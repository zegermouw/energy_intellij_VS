# energy_intellij_VS
This repo contains the code for checking the differences in power consumption between Intellij and Visual Studio Code

To run the power log, the following software is needed.
Intel Power Gadget
Intellij
Visual Studio Code (Including the extension Code Runner)

After all the software is installed, the power log can be started with the following command.

"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe" -file filename.csv -cmd python main.py arg1 arg2

arg1 should be ["intellij", "vs"] depending on the software that you want to test. 

arg2 should be ["java", "javascript", "python"] depending on the language that you want to test.

filename should be the name of the file where you want to store the data.
