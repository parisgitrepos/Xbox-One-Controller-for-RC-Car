from controller import Controller

joystick = Controller(0)

while True:
    velocity = joystick.velocity()
    lb, rb = joystick.get_lb_rb()
    lb, rb = str(lb), str(rb)
    print(f'Velocity: {velocity}\nLeft Button Pressed: {lb}\nRight Button Pressed: {rb}\n')
