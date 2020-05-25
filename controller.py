import pygame
pygame.init() # Pygame requires a special function to init

class Controller:
    def __init__(self, joystick_id):
        self.joystick = pygame.joystick.Joystick(joystick_id)
        self.joystick.init()

    def get_lb_rb(self):
        pygame.event.get()
        lb = self.joystick.get_button(6) == 1
        rb = self.joystick.get_button(7) == 1
        return lb, rb # True if button is pressed, False if button is not pressed

    def velocity(self):
        pygame.event.get()
        velocity = round(self.joystick.get_axis(1)*-1, 1)
        return velocity # Velocity returned is between -1 and 1