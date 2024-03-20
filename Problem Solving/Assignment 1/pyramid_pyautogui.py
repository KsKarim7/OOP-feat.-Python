import pyautogui
from time import sleep

rows = int(input("Enter number of rows: "))
sleep(3)

pyautogui.write(str(rows))
pyautogui.press("enter")
for i in range(1,rows+1):
    pyautogui.write("#"*i)
    pyautogui.press("enter")








