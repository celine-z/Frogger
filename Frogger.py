'''
Celine Zhang
May 29, 2015
Frogger game: A game where the player guides the frog using the arrow keys to
help them get to the lily pads on the other side. If frog collides with cars or
the water they will lose a life. This also includes a menu screen of the game
name, best time, and the instructions.
'''

# I - Import and Initialize
import pygame, pySprites, random
pygame.init()

def main():
    '''This function defines the mainline logic'''
    # D - Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("FROGGER")
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("SpriteImages\\instructionbg.png")
    background = background.convert()
    
    # Sprites
    game_name = pygame.font.Font("Fonts\\Bubbly Frog.ttf", 90)
    game_name_label = pySprites.Message(game_name, "F   R   O   G   G   E   R",\
                                        None, False, (320, 90), (150, 225, 0))
    
    best_time_font= pygame.font.Font("Fonts\\blockbusted.ttf", 30)
    best_time = 0
    best_time_label = pySprites.Timer(best_time_font, "Best Time : ", \
                                      best_time, (320, 170),  (28, 218, 211))
    
    font = pygame.font.Font("Fonts\\telespania.ttf", 20)
    instructions1 = pySprites.Message(font,\
        "Use the arrow keys to guide the frogs to the lily", None, False, \
        (320, 240), (225, 225, 0))
    
    instructions2 = pySprites.Message(font,\
        "pads on the other side of the river without getting", None, False, \
        (320, 270), (225, 225, 0))
    
    instructions3 = pySprites.Message(font,\
        "hit by the cars or falling into the water.You will", None, False, \
        (320, 300), (225, 225, 0))
    
    instructions4 = pySprites.Message(font,\
        "be timed on how fast you complete the game.", None, False, \
        (320, 330), (225, 225, 0))
    
    instructions5 = pySprites.Message(font,\
        "Good luck and have fun!", None, False, (320, 360), (225, 225, 0))
    
    start_font = pygame.font.Font("Fonts\\blockbusted.ttf", 40)
    start = pySprites.Message(start_font,\
        "press space to begin", None, False, (320, 399), (255, 0, 0))
    
    allSprites = pygame.sprite.OrderedUpdates(game_name_label, best_time_label,
                                              instructions1, instructions2,
                                              instructions3, instructions4,
                                              instructions5, start)
    
    # Menu music
    pygame.mixer.music.load("MusicFiles\\FroggerMenuScreen(1).ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # A - Action
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)    
    
    # L - Loop
    while keepGoing:
    
        # T - Timer to set frame rate
        clock.tick(30)
        time_b4 = (pygame.time.get_ticks() / 1000.0)
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Stops menu music when game starts
                    pygame.mixer.music.stop()
                    keepGoing, best_time = game(time_b4, best_time, screen)
                    if keepGoing:
                        best_time_label.set_time(best_time)
                        pygame.mixer.music.load(\
                            "MusicFiles\\FroggerMenuScreen(1).ogg")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
    
        # R - Refresh display
        screen.blit(background, (0, 0))
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
    
    # Show background before quit
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)    
    # Close the game window
    pygame.quit()
    
def game(time_b4, best_time, screen):
    '''This function defines the game function'''   
    # D - Display 
     
    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("SpriteImages\\bg.png")
    background = background.convert()
    screen.blit(background, (0, 0))
    
    # Sprites
    player = pySprites.Player(screen)
    water = pySprites.Platform( 0, 0, 640, 171)
    boundary_l = pySprites.Platform( 0, 0, 1, 480)
    boundary_r = pySprites.Platform( 639, 0, 1, 480)
    font = pygame.font.Font("Fonts\\blockbusted.ttf", 15)
    lives = 3
    die_image = pySprites.DieImage()
    lives_label = pySprites.Message(font, "Lives: ", 3, False, (30, 465), \
                                    (225, 225, 0))
    lilypad_label = pySprites.Message(font, "Lily Pads Left: ", 5, True, \
                                      (167,465), (225, 225, 0))
    best_time_label = pySprites.Timer(font, "Best Time: ", best_time,(465,465),\
                                      (225, 225, 0))
    time_label = pySprites.Timer(font, "Time: ", 0, (580,465), (225, 225, 0))
    frogger = pygame.font.Font("Fonts\\Bubbly Frog.ttf", 25)
    frogger = frogger.render("F   R   O   G   G   E   R", 1,(150, 225, 0))
    screen.blit(frogger, (260, 450))
    end_label = pygame.font.Font("Fonts\\Bubbly Frog.ttf", 40)
    end_label = end_label.render("G  a  m  e   O  v  e  r  !", 1, (225,225,0))
    win_label = pygame.font.Font("Fonts\\Bubbly Frog.ttf", 40)
    win_label = win_label.render("Y  o  u   W  i  n  !", 1, (225,225,0))
    
    # Lilypad sprite
    lilypads = []
    x_pos = -93
    y_pos = 27
    for times in range (5):
        x_pos = x_pos + 138
        lilypad = pySprites.LilyPad(x_pos, y_pos)
        lilypads.append(lilypad)
    lilypadGroup = pygame.sprite.OrderedUpdates(lilypads)
    
    # Cars sprite
    cars = []
    y_value = 203
    for rows in range(4):
        if rows == 0:
            y_value = y_value + 40
            x_value = 0
            for col in range(3):
                x_value = x_value + random.randint(170, 300)
                car = pySprites.MovingObjects( x_value, y_value, -3)
                cars.append(car)
        if rows == 1:
            y_value = y_value + 35
            car = pySprites.MovingObjects( 0, y_value, -15)
            cars.append(car)
        if rows > 1 :
            y_value = y_value + 54
            x_value = 640
            for col in range(4):
                x_value = x_value - random.randint(100, 160)
                car = pySprites.MovingObjects( x_value, y_value, 5-rows)
                cars.append(car)          
    carGroup = pygame.sprite.OrderedUpdates(cars)
    
    # Water object sprite
    waterobjs = []
    y_cord = 202
    for toprows in range(4):
        y_cord = y_cord - 35
        # Logs
        if toprows % 2 == 0:
            x_cord = 0
            for topcol in range(3):
                x_cord = x_cord + random.randint(150, 250)
                waterobj = pySprites.WaterObjects(x_cord, y_cord, 2)
                waterobjs.append(waterobj)
        # Turtles
        else:
            x_cord = 640
            for topcol in range(3):
                x_cord = x_cord - random.randint(200, 250)
                waterobj = pySprites.WaterObjects(x_cord, y_cord, -1)
                waterobjs.append(waterobj)          
    waterobjGroup = pygame.sprite.OrderedUpdates(waterobjs)
    
    # Lives image sprite
    livesprites = []
    y_location = 466
    x_location = 45
    for numlives in range(lives):
        x_location += 12
        livesimg = pySprites.LivesImage(x_location, y_location)
        livesprites.append(livesimg)
    livesGroup = pygame.sprite.OrderedUpdates(livesprites)
    
    allSprites = pygame.sprite.OrderedUpdates(water, boundary_l, boundary_r,
                                              lilypadGroup, carGroup, 
                                              waterobjGroup, livesGroup, 
                                              lives_label, lilypad_label, 
                                              best_time_label, time_label,
                                              die_image, player)
    
    # Game music
    pygame.mixer.music.load("MusicFiles\\FroggerMenuScreen(2).ogg")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    lost_life = pygame.mixer.Sound("MusicFiles\\lose.ogg")
    lost_life.set_volume(0.3)
    reached = pygame.mixer.Sound("MusicFiles\\reached.ogg")
    reached.set_volume(0.9)
    game_over = pygame.mixer.Sound("MusicFiles\\gameOver.ogg")
    game_over.set_volume(0.3)
    winner = pygame.mixer.Sound("MusicFiles\\win.ogg")
    winner.set_volume(1)
        
    # A - Action
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
 
    # L - Loop
    while keepGoing:
    
        # T - Timer to set frame rate
        clock.tick(30)
        
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return (False, best_time_label.get_time())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    player.change_direction((0, 1))                
                elif event.key == pygame.K_RIGHT:
                    player.change_direction((1, 0))
                elif event.key == pygame.K_LEFT:
                    player.change_direction((-1, 0))
            elif event.type == pygame.KEYUP:
                player.change_direction((0, 0))
        
        # Keep track of time and subtracts time used during menu screen
        if (lilypad_label.get_num() > 0) and (lives_label.get_num() > 0):
            time_label.set_time((pygame.time.get_ticks() / 1000.0)-time_b4)
        
        # Check if player collided with water object
        if player.rect.colliderect(water):
            die = True
            onwaterobj = False
            player.set_speed(0)
            # Check if player collided with moving water objects
            for objects in waterobjGroup:
                if objects.rect.collidepoint(player.rect.center)or\
                   objects.rect.collidepoint(player.rect.midbottom):
                    onwaterobj = True
                    player.set_speed(objects.get_speed())
                    die = False
            # Check if it collided with lily pad
            if not onwaterobj:
                for lilypadhit in lilypadGroup:
                    if player.rect.colliderect(lilypadhit):
                        if lilypadhit.already_hit():
                            die = True
                        else:
                            die = False
                            reached.play()
                            player.reset()
                            lilypad_label.set_num(-1)
                            lilypadhit.hit()
            # If player not on either water object or lily pad, kills the player
            if die:
                lives_label.set_num(-1)
                livesprites[lives_label.get_num()].kill()
                lost_life.play()
                die_image.set_position(player.get_position())
                player.pause_time()
        
        # Collision detection with player and car
        if pygame.sprite.spritecollide(player, carGroup, False):
            lives_label.set_num(-1)
            livesprites[lives_label.get_num()].kill()
            lost_life.play()
            die_image.set_position(player.get_position())
            player.pause_time() # pause player when dead
        
        # Collision detection with player and left boundary
        if player.rect.colliderect(boundary_l):
            lives_label.set_num(-1)
            livesprites[lives_label.get_num()].kill()
            lost_life.play()
            die_image.set_position(player.get_position())
            player.pause_time() # pause player when dead
            
        # Collision detection with player and right boundary
        if player.rect.colliderect(boundary_r):
            lives_label.set_num(-1)
            livesprites[lives_label.get_num()].kill()
            lost_life.play()
            die_image.set_position(player.get_position())
            player.pause_time() # pause player when dead
            
        # Check if all lily pad collected
        if lilypad_label.get_num() <= 0:
            if (best_time_label.get_time()== 0) or \
               (best_time_label.get_time() > time_label.get_time()):
                best_time_label.set_time(time_label.get_time())
            pygame.mixer.music.stop()    
            winner.play()
            screen.blit(win_label, (252, 185))
            pygame.display.flip()
            keepGoing = False
        
        # Check if no lives left
        if lives_label.get_num() <= 0:
            pygame.mixer.music.stop()
            game_over.play()
            screen.blit(end_label, (227, 183))
            pygame.display.flip()
            keepGoing = False
            
        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()  
        
    # Return keepGoing as True
    pygame.time.delay(3000)
    return (True, best_time_label.get_time())
    
# Call the main function
main()