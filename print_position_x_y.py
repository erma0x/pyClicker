import pyautogui, time

while True: 
    posXY = pyautogui.position() 
    print(posXY[0],',',posXY[1])
    time.sleep(0.3)
    if posXY[0] == 0:
        break
