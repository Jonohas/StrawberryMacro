import usb_hid
import board
from digitalio import Direction, Pull, DigitalInOut


columns = [board.GP6]
rows = [board.GP2,board.GP3,board.GP4,board.GP5]

pressed = []

for col in columns:
    pressed_rows = []
    p_col = DigitalInOut(col)
    p_col.direction = Direction.OUTPUT
    p_col.value = False
    
    for row in rows:
        p_row = DigitalInOut(row)
        p_row.direction = Direction.INPUT
        p_row.pull = Pull.UP
        pressed_rows.append(p_row.value)
    
    p_col.direction = Direction.INPUT
    pressed.append(pressed_rows)
    

print(pressed)

