import pygame
import math
pygame.init()
(width,height)=(1200,800)
white=(255,255,255)
black=(0,0,0)
drag=0.999
elasticity=0.60
gravity=(math.pi, 0.002)
isJump=False
jumpCount=10
def addVectors(angle1, length1,angle2, length2):
    x=math.sin(angle1)*length1+math.sin(angle2)*length2
    y=math.cos(angle1)*length1+math.cos(angle2)*length2

    angle=0.5*math.pi-math.atan2(y,x)
    length=math.hypot(x,y)
    return (angle,length)
class balls:
    def __init__(self, position, size,speed, angle):
        self.x=position[0]
        self.y=position[1]
        self.size=size
        self.color=(0,0,0)
        self.thickness=3
        self.speed=speed
        self.angle=angle
    def circle(self):
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.size,self.thickness)
    def move(self):
        (self.angle, self.speed)=addVectors(self.angle,self.speed,math.pi, 0.002)
        self.x+=math.sin(self.angle)*self.speed
        self.y-=math.cos(self.angle)*self.speed
        self.speed*=drag
    def bounce(self):
        if self.x>width-self.size:
            self.x=2*(width-self.size)-self.x
            self.angle=-self.angle
            self.speed *= elasticity
        elif self.x<self.size:
            self.x=2*self.size-self.x
            self.angle=-self.angle
            self.speed *= elasticity
        if self.y>height-self.size:
            self.y=2*(height-self.size)-self.y
            self.angle=math.pi-self.angle
        elif self.y<self.size:
            self.y=2*self.size-self.y
            self.angle=math.pi-self.angle
            self.speed *= elasticity
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('physic')
myballs1 = balls((600, 200), 15,0,0)
open=True
while open:
    keys = pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_UP]:
            myballs1.speed=-1
            myballs1.angle=math.pi
            if keys[pygame.K_LEFT]:
                myballs1.speed=1
                myballs1.angle=-math.pi/3
            elif keys[pygame.K_RIGHT]:
                myballs1.speed=1
                myballs1.angle=math.pi/3
        isJump=True
    else:
        if jumpCount>=-10:
            go=10





    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                myballs1.speed=-1
                myballs1.angle=math.pi/2
            elif event.key == pygame.K_RIGHT:
                myballs1.speed=1
                myballs1.angle=math.pi/2
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                myballs1.speed*=0.75




    screen.fill(white)
    myballs1.move()
    myballs1.bounce()
    myballs1.circle()

    pygame.display.flip()