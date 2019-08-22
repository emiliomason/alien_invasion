import pygame.font  # allows python to render text to the screen


class Button:

    def __init__(self, ai_settings, screen, msg):  # contains the text for the button
        """Initialise button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # green
        self.text_color = (255, 255, 255)  # white
        self.font = pygame.font.SysFont(None, 48)  # default font and font size

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        # draw rectangle portion of the button
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # draw the text to the screen
