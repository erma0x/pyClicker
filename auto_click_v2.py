

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

# TUTORIAL
#https://nitratine.net/blog/post/simulate-mouse-events-in-python/

mouse = Controller()
print ("Current position: " + str(mouse.position)) # Find mouse position

mouse.position = (10, 20) # SET MOUSE POSITION
mouse.move(20, -13) # move mouse relative to it's position

# Click the left button
mouse.click(Button.left, 1)
# Click the right button
mouse.click(Button.right, 1)
# Click the middle button
mouse.click(Button.middle, 1)
# Double click the left button
mouse.click(Button.left, 2)
# Click the left button ten times
mouse.click(Button.left, 10)

mouse.press(Button.left)
mouse.release(Button.left)



# Scroll up two steps
mouse.scroll(0, 2)
# Scroll right five steps
mouse.scroll(5, 0)
