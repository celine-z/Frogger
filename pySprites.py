'''
Celine Zhang
May 29, 2015
Classes for the sprites of the Frogger game
'''
import pygame, random

class Player(pygame.sprite.Sprite):
    '''This class controls the player sprite including its movement'''
    def __init__(self, screen):
        '''This method initializes the image of the player and accepts the 
        screen as parameter'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes
        self.__frogup1 = pygame.image.load("SpriteImages\\frog-y1.png")
        self.__frogup2 = pygame.image.load("SpriteImages\\frog-y2.png")
        self.__frogdown1 = pygame.image.load("SpriteImages\\frog-y-1.png")
        self.__frogdown2 = pygame.image.load("SpriteImages\\frog-y-2.png")
        self.__frogright1 = pygame.image.load("SpriteImages\\frog-x1.png")
        self.__frogright2 = pygame.image.load("SpriteImages\\frog-x2.png")
        self.__frogleft1 = pygame.image.load("SpriteImages\\frog-x-1.png")
        self.__frogleft2 = pygame.image.load("SpriteImages\\frog-x-2.png")
        
        self.__list = [self.__frogup1, self.__frogup2, self.__frogdown1, \
                       self.__frogdown2, self.__frogright1,self.__frogright2,\
                       self.__frogleft1, self.__frogleft1]
        
        # Converts the images
        for images in self.__list:
            images = images.convert()
        
        self.image = self.__frogup1     
        self.rect = self.image.get_rect()
        
        self.__screen = screen

        self.reset()
        
        self.__pause = -1
        
    def change_direction(self, direction):
        '''This method accepts direction as a parameter, changes the direction
        of the dx and dy values including the picture, and sets on water to
        False. Also it updates the status of which direction the frog is going'''
        self.__dx = direction[0]*5
        self.__dy = direction[1]*5
        self.__onwater = False
        self.__times = 0
        
        if self.__dx > 0:
            self.__status = "right"
        elif self.__dx < 0:
            self.__status = "left"
        elif self.__dy < 0:
            self.__status = "up"
        elif self.__dy > 0:
            self.__status = "down"
        
    def right(self):
        '''This method changes the image of the frog when going right'''
        self.__times = self.__times + 1
        self.__status= "right"
        if self.__times == 1:
            self.image = self.__frogright1
        elif self.__times == 8:
            self.image = self.__frogright2
        elif self.__times == 15:
            self.__times = 0
        # Sets image after the frog stops to look like it is stationary
        elif self.__times == -1:
            self.image = self.__frogright1
            self.__status = None
                    
    def left(self):
        '''This method changes the image of the frog when going left'''
        self.__times = self.__times + 1
        self.__status= "left"
        if self.__times == 1:
            self.image = self.__frogleft1
        elif self.__times == 8:
            self.image = self.__frogleft2
        elif self.__times == 15:
            self.__times = 0
        # Sets image after the frog stops to look like it is stationary
        elif self.__times == -1:
            self.image = self.__frogleft1
            self.__status = None        
        
    def up(self):
        '''This method changes the image of the frog when going up'''
        self.__times = self.__times + 1
        self.__status= "up"
        if self.__times == 1:
            self.image = self.__frogup1
        elif self.__times == 8:
            self.image = self.__frogup2
        elif self.__times == 15:
            self.__times = 0
        # Sets image after the frog stops to look like it is stationary
        elif self.__times == -1:
            self.image = self.__frogup1
            self.__status = None            
        
    def down(self):
        '''This method changes the image of the frog when going down'''
        self.__times = self.__times + 1
        self.__status= "down"
        if self.__times == 1:
            self.image = self.__frogdown1
        elif self.__times == 8:
            self.image = self.__frogdown2
        elif self.__times == 15:
            self.__times = 0
        # Sets image after the frog stops to look like it is stationary
        elif self.__times == -1:
            self.image = self.__frogdown1
            self.__status = None            
        
    def set_speed(self, speed):
        '''This method accepts the speed of the object that the player is on and
        changes the on water to True'''
        self.__speed = speed
        self.__onwater = True
        
    def get_position(self):
        '''this method returns the position of the player'''
        return self.rect.centerx, self.rect.centery
    
    def pause_time (self):
        '''This method pauses the player'''
        self.__pause = 75 

    def reset(self):
        '''This method is the reset method that resets the player status, 
        location, direction, speed, and on water variable'''
        # Starting location
        self.__status = "up"
        self.__times = 0
        self.image = self.__frogup1
        self.rect.centerx = (self.__screen.get_width()/2)
        self.rect.centery = (self.__screen.get_height()-48)
        
        # Starting direction value
        self.__dx = 0
        self.__dy = 0
        
        self.__speed = 0
        self.__onwater = False
        
    def update(self):
        '''This method updates the player sprite's location and calls reset when
        it reaches the left and right boundary of the screen'''
        # Change speed to 0 if the player is not on moving water object
        if (not self.__onwater):
            self.__speed = 0
    
        self.rect.centerx += (self.__dx + self.__speed)
        
        # Make sure cannot pass top and bottom boundary
        if ((self.rect.top > 30) or (self.__dy > 0)) and \
           ((self.rect.bottom < self.__screen.get_height()-38) or\
            (self.__dy < 0)):
            self.rect.centery += (self.__dy)
        
        # Does not allow frog to move or be seen until death graphics are done        
        if self.__pause > 0:
            self.rect.centerx = (self.__screen.get_width()/2)
            self.rect.centery = 650
            self.__pause = self.__pause - 1
        elif self.__pause == 0:
            self.__pause = -1
            self.reset()
        
        if (self.__dx == 0) and (self.__dy == 0):
            self.__times = -2
        
        # Calls the correct image method
        if self.__status == "right":
            self.right()
        elif self.__status == "left":
            self.left()
        elif self.__status == "up":
            self.up()
        elif self.__status == "down":
            self.down()
            
            
class DieImage(pygame.sprite.Sprite):
    '''This class displays the die graphics'''
    def __init__(self):
        '''This method initializes the death images'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.__die1 = pygame.image.load("SpriteImages\\die-1.png")
        self.__die2 = pygame.image.load("SpriteImages\\die-2.png")
        self.__die3 = pygame.image.load("SpriteImages\\die-3.png")
        self.__die4 = pygame.image.load("SpriteImages\\die-4.png")
        
        self.__list = [self.__die1, self.__die2, self.__die3, self.__die4]
        
        for images in self.__list:
            images = images.convert()
        
        self.__amountdied = 0
        
        self.reset()
    
    def reset(self):
        '''This method resets the image and location and changes die to False'''
        self.__die = False
        self.image = self.__die1
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 640
        
    def set_position(self, position):
        '''Accepts the x_pos and y_pos of the sprite as a tuple and sets the 
        image to that location. It adds 1 to amountdied to keep track of amount
        died'''
        self.__amountdied = self.__amountdied + 1
        self.__times = 0
        self.__die = True
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
        
    def update(self):
        '''This method updates the die images'''
        if self.__amountdied == 3:
            self.__times = 29
        if self.__die:
            self.__times = self.__times + 1
            if self.__times <= 6:
                self.image = self.__die1
            elif self.__times == 12:
                self.image = self.__die2
            elif self.__times == 18:
                self.image = self.__die3
            elif self.__times == 30:
                self.image = self.__die4
            elif self.__times >= 75:
                self.reset()
        
        
class LilyPad(pygame.sprite.Sprite):
    '''This class creates the lily pad sprite and sets its location of it'''
    def __init__(self, x_pos, y_pos):
        '''This method accepts x position and y position as parameter and
        initializes the position of the lily pad'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes
        self.__hitpic = pygame.image.load("SpriteImages\\reached-1.png")
        self.__lasthitpic = pygame.image.load("SpriteImages\\reached-2.png")
        self.image = pygame.image.load("SpriteImages\lily_pad.png")
        
        self.__list = [self.__hitpic, self.__lasthitpic, self.image]
        
        for images in self.__list:
            images = images.convert()
            
        self.__times = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        
        self.__hit = False
        
    def hit(self):
        '''Sets the hit variable to True'''
        self.__hit = True
        
    def already_hit(self):
        '''Returns if the lily pad was hit already'''
        if self.__hit:
            return True
        else:
            return False
    
    def update(self):
        '''This method updates the hit picture of the lily pad'''
        # If lily pad hit, image changes
        if self.__hit:
            self.__times = self.__times + 1
            if self.__times <= 8:
                self.image = self.__hitpic
            else:
                self.image = self.__lasthitpic


class LivesImage(pygame.sprite.Sprite):
    '''This class creates the lily pad sprite and sets its location of it'''
    def __init__(self, x_pos, y_pos):
        '''This method accepts x position and y position as parameter and
        initializes the position of the lily pad and its image'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes
        self.image = pygame.image.load("SpriteImages\\lives.png")
        self.image = self.image.convert()
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
        
        
class Platform(pygame.sprite.Sprite):
    '''This class creates a rectangle'''
    def __init__(self, x_pos, y_pos, width, height):
        '''This method accepts the x and y position as parameter and draws a 
        rectangle on the screen  from the width and height parameter'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Define the image attributes
        self.image = pygame.Surface((width,height))
        self.image.fill((5,5,5))
        self.image.set_colorkey((5,5,5))
        self.rect = self.image.get_rect()
        
        self.rect.left = x_pos
        self.rect.top = y_pos
        
        
class MovingObjects(pygame.sprite.Sprite):
    '''This class creates the moving car sprites and its movement'''
    def __init__(self, x_pos, y_pos, dx):
        '''This class initializes the image of the sprite, sets the x and y
        location of the sprite, and also sets a dx value'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.__right1 = pygame.image.load("SpriteImages\\car-r1.png")
        self.__right2 = pygame.image.load("SpriteImages\\car-r2.png")
        self.__right3 = pygame.image.load("SpriteImages\\car-r3.png")
        self.__left1 = pygame.image.load("SpriteImages\\car-l1.png")
        self.__left2 = pygame.image.load("SpriteImages\\car-l2.png")
        
        self.__list = [self.__right1, self.__right2, self.__right3, \
                       self.__left1, self.__left2]
        
        for images in self.__list:
            images = images.convert()
            
        # Check for if car is moving right and randomly choses rigt image
        if dx > 0:
            num = random.randrange(3)
            if num == 0:
                self.image = self.__right1
            if num == 1:
                self.image = self.__right2
            if num == 2:
                self.image = self.__right3
        # Check for if car is moving left and randomly choses left image
        elif dx < 0:
            if y_pos < 250:
                self.image = self.__left1
            if y_pos > 250:
                self.image = self.__left2
            
        self.rect = self.image.get_rect()
        self.__dx = dx
        self.rect.centerx = x_pos
        self.rect.centery = y_pos
    
    def update(self):
        '''This method updates the location of the object sprites'''
        if (self.rect.right < 0) and (self.__dx < 0):
            self.rect.left = 640
        if (self.rect.left > 640) and (self.__dx > 0):
            self.rect.right = 0
            
        self.rect.centerx += self.__dx
        

class WaterObjects(pygame.sprite.Sprite):
    '''This class creates the moving water objects sprites and its movement'''
    def __init__(self, x_pos, y_pos, dx):
        '''This class initializes the image of the sprite, sets the x and y
        location of the sprite from the parameter of x_pos and y_pos. It also 
        sets a dx value using the dx parameter'''
        # Call the parent of __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.__turtle2_2 = pygame.image.load("SpriteImages\\turtle(2)-2.png")
        self.__turtle2_3 = pygame.image.load("SpriteImages\\turtle(2)-3.png")
        self.__turtle3_2 = pygame.image.load("SpriteImages\\turtle(3)-2.png")
        self.__turtle3_3 = pygame.image.load("SpriteImages\\turtle(3)-3.png")
        self.__invisible2_1 = pygame.image.load("SpriteImages\\invisible2-1.png")
        self.__invisible2_2 = pygame.image.load("SpriteImages\\invisible2-2.png")
        self.__invisible3_1 = pygame.image.load("SpriteImages\\invisible3-1.png")
        self.__invisible3_2 = pygame.image.load("SpriteImages\\invisible3-2.png")
        self.__log = pygame.image.load("SpriteImages\\waterobj-1.png")
        
        self.__list = [self.__turtle2_2, self.__turtle2_3, self.__turtle3_2,\
                       self.__turtle3_3, self.__invisible2_1,\
                       self.__invisible2_2, self.__invisible3_1,\
                       self.__invisible3_2, self.__log]
        
        for images in self.__list:
            images = images.convert()
        
        # Set image according to y loc ation
        if y_pos == 167:
            self.image = self.__log
            self.__inv = False
        elif y_pos == 132:
            self.image = self.__turtle3_2
            self.__index = 2
            self.__inv = True
        elif y_pos == 97:
            self.image = self.__log
            self.__inv = False
        elif y_pos == 62:
            self.image = self.__turtle2_2
            self.__index = 0
            self.__inv = True
            
        self.rect = self.image.get_rect()
        self.__dx = dx
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.rect.centerx = self.__x_pos
        self.rect.centery = self.__y_pos
        
        # Randomly choses an image stage
        self.__times = random.randrange( 0, 15, 14)
        # Randomly choses the stage of turtle's visibility
        self.__amountinvis = random.randrange(9)
        
    def get_speed(self):
        '''This method returns the speed of the moving object sprites'''
        return self.__dx
    
    def update(self):
        '''This method updates the location of the object sprites'''
        if (self.rect.right < 0) and (self.__dx < 0):
            self.rect.left = 640
        if (self.rect.left > 640) and (self.__dx > 0):
            self.rect.right = 0
            
        self.rect.centerx += self.__dx
        
        # Set the invisible image stages for the turtles
        if self.__inv:
            self.__times = self.__times + 1
            
            if self.__times == 1:
                self.image =  self.__list[self.__index]
                self.__dx = -1
            elif self.__times == 15:
                self.image =  self.__list[self.__index+1]
                self.__dx = -2
            elif self.__times == 35:
                self.__amountinvis = self.__amountinvis + 1
                if self.__amountinvis == 10:
                    self.__times = 36
                else:
                    self.__times = 0
            if self.__times == 36:
                self.image =  self.__list[self.__index+4]
                self.__dx = -1
            elif self.__times == 66:
                self.image =  self.__list[self.__index+5]
                self.__dx = -1
            elif self.__times == 96:
                self.rect.centery = -25
            elif self.__times == 126:
                self.rect.centery = self.__y_pos
            elif self.__times == 156:
                self.image =  self.__list[self.__index+4]
            elif self.__times == 186:
                self.__times = 0
                self.__amountinvis = 1
                
                
class Message(pygame.sprite.Sprite):
    '''This class defines a label sprite'''
    def __init__(self, font, word, number, need_num, position, colour):
        '''This initializer accepts the font, word, number, position and colour
        as parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Sets the font, number, words, position, and colour
        self.__font = font
        self.__num = number
        self.__word = word
        self.__neednum = need_num
        self.__position = position
        self.__colour = colour
    
    def set_num(self, num):
        '''This method accepts num as parameter and changes the number value by
        adding the parameter to it'''
        self.__num =  self.__num + num
        
    def get_num(self):
        '''This method returns the number value'''
        return self.__num
        
    def update(self):
        '''This method will be called automatically to display 
        the message desired'''
        # if number needed for the score keeper
        if self.__neednum:
            self.__message = self.__word+"%d" %self.__num
        # if number not needed for the score keeper
        else:
            self.__message = self.__word
        self.image = self.__font.render(self.__message, 1, self.__colour)
        self.rect = self.image.get_rect()
        self.rect.center = self.__position
        
        
class Timer(pygame.sprite.Sprite):
    '''This class defines a timer label sprite'''
    def __init__(self, font, word, time, position, colour):
        '''This initializer accepts the font, word, number, position and colour
        as parameters'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Sets the font, time, word, position, and colour
        self.__font = font
        self.__time = time
        self.__word = word
        self.__position = position
        self.__colour = colour
    
    def set_time(self, time):
        '''This method accepts num as parameter and changes the time'''
        self.__time =  time
        
    def get_time(self):
        '''This method returns the time'''
        return self.__time
        
    def update(self):
        '''This method will be called automatically to display 
        the current time in seconds'''
        self.__message = self.__word+"%d sec" %self.__time
        self.image = self.__font.render(self.__message, 1, self.__colour)
        self.rect = self.image.get_rect()
        self.rect.center = self.__position