import pygame

screenSize = (640, 480)
surface = pygame.display.set_mode(screenSize)

class Background():
    def __init__(self):
        self.bgimage = pygame.image.load('bg1.png')
        self.rectBGimg = self.bgimage.get_rect()
        self.bgimage = pygame.transform.scale(self.bgimage, (int(screenSize[0] / self.rectBGimg.width * self.rectBGimg.width), int(screenSize[0] / self.rectBGimg.width * self.rectBGimg.height)))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.rectBGimg.height
        self.bgX2 = 0

        self.movingUpSpeed = 5

    def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height

    def render(self):
        surface.blit(self.bgimage, (self.bgX1, self.bgY1))
        surface.blit(self.bgimage, (self.bgX2, self.bgY2))
        
   
   pygame.init()     
   while True:
     
          