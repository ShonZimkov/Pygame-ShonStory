import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
# #vars health
# horn_legs = 100
# horn_wings = 100
# horn_right = 100
# horn_left = 100
# horn_tail = 100
# horn_heada = 130
# horn_headb = 150
# horn_headc = 130
# horn_health = horn_legs + horn_wings + horn_right + horn_left + horn_tail + horn_heada + horn_headb + horn_headc
#vars idle
tail_idle = True
head_cidle = True
head_aidle = True
head_bidle = True
wings_idle = True
left_idle = True
right_idle = True
legs_idle = True
#vars attack
tail_attack = False
head_cattack = False
head_aattack = False
head_battack = False
wings_attack = False
left_attack = False
right_attack = False
legs_attack = False
#attacks
lightning = False
fire = False
tail_dmg = False
flame = False
#death
tail_d = False
legs_d = False
head_ad = False
head_bd = False
head_cd = False
right_d = False
left_d = False
wings_d = False

class Head_a(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 39):
            img = pygame.image.load(
                f'img/horntail/idle/head_a/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (245, 275))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0
    def update(self):
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop

        # update explosion amimation
        # self.frame_index += 1
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Head_ad(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 12):
            img = pygame.image.load(
                f'img/horntail/death/head_a/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (245, 275))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0
    def update(self):
        global head_ad
        if head_ad:
            if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop

            # update explosion amimation
            # self.frame_index += 1
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]

class Head_aa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 14):
            img = pygame.image.load(
                f'img/horntail/attack/Head_a/skill2_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (245, 275))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global head_aidle
        global head_aattack
        global fire
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            head_aidle = True
            head_aattack = False
            fire = True
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Head_b(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 49):
            img = pygame.image.load(
                f'img/horntail/idle/Head_b/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (180, 400))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0
        
    def update(self):
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Head_bd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 11):
            img = pygame.image.load(
                f'img/horntail/death/Head_b/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (180, 400))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0
        
    def update(self):   
        global head_bd
        if head_bd:    
            if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]


class Head_ba(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 12):
            img = pygame.image.load(
                f'img/horntail/attack/Head_b/skill3_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (210, 400))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0
        
    def update(self):
        global head_battack
        global head_bidle
        global flame
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            head_bidle = True
            flame = True
            head_battack = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Head_c(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 59):
            img = pygame.image.load(
                f'img/horntail/idle/Head_c/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (245, 275))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Head_cd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 12):
            img = pygame.image.load(
                f'img/horntail/death/Head_c/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (245, 275))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global head_cd
        if head_cd:
            if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]


class Head_ca(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 15):
            img = pygame.image.load(
                f'img/horntail/attack/Head_c/skill1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (275, 305))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global head_cidle
        global head_cattack
        global lightning
        if self.animation_tick == 5: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            head_cidle = True
            head_cattack = False
            lightning = True
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Left_Hand(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 4):
            img = pygame.image.load(
                f'img/horntail/idle/Left_Hand/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (225, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Left_d(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 14):
            img = pygame.image.load(
                f'img/horntail/death/Left/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (225, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global left_d
        if left_d:
            if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]



class Left_aHand(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(2, 14):
            img = pygame.image.load(
                f'img/horntail/attack/Left/skill2_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (310, 265))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global left_attack
        global left_idle
        if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            left_idle = True
            left_attack = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Right_Hand(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 4):
            img = pygame.image.load(
                f'img/horntail/idle/Right_Hand/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (240, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Right_d(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 14):
            img = pygame.image.load(
                f'img/horntail/death/Right/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (240, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global right_d
        if right_d:
            if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]


class Right_aHand(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(2, 14):
            img = pygame.image.load(
                f'img/horntail/attack/Right/skill2_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (330, 265))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global right_idle
        global right_attack
        if self.animation_tick == 12: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            right_attack = False
            right_idle = True
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Legs(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 2):
            img = pygame.image.load(
                f'img/horntail/idle/Legs/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (550, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Legs_d(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 10):
            img = pygame.image.load(
                f'img/horntail/death/Legs/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (550, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global legs_d
        if legs_d:
            if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]


class Legs_a(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 13):
            img = pygame.image.load(
                f'img/horntail/attack/Legs/attack1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (550, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global legs_idle
        global legs_attack
        if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            legs_attack = False
            legs_idle = True
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Tail(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 3):
            img = pygame.image.load(
                f'img/horntail/idle/Tail/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (350, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if tail_idle:
            if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = 0
            else:
                self.image = self.images[self.frame_index]


class Tail_d(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 8):
            img = pygame.image.load(
                f'img/horntail/death/Tail/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (350, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global tail_d
        if tail_d:
            if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]

class Tail_a(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 19):
            img = pygame.image.load(
                f'img/horntail/attack/Tail/attack1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (350, 200))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global tail_idle
        global tail_attack
        global tail_dmg
        if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index == 13:
            tail_dmg = True
        if self.frame_index >= len(self.images) :
            tail_dmg = False
            tail_idle = True
            tail_attack = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]


class Wings(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 31):
            img = pygame.image.load(
                f'img/horntail/idle/Wings/stand_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (670, 380))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Wings_d(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 12):
            img = pygame.image.load(
                f'img/horntail/death/Wings/die1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (670, 380))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global wings_d
        if wings_d:
            if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
                self.frame_index += 1
                self.animation_tick = 0 #reset tick back to 0 after changing frame
            self.animation_tick += 1 #add 1 each iteration of the while loop
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.frame_index = len(self.images)
            else:
                self.image = self.images[self.frame_index]

class Wings_a(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 22):
            img = pygame.image.load(
                f'img/horntail/attack/Wings/skill1_{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (670, 380))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global wings_idle
        global wings_attack
        if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            wings_idle = True
            wings_attack = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Lightning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 6):
            img = pygame.image.load(
                f'img/horntail/attacks/lightning/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (300, 380))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global lightning
        if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            lightning = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]
    
class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 4):
            img = pygame.image.load(
                f'img/horntail/attacks/fire/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (300, 380))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global fire
        if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            fire = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]

class Flame(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 10):
            img = pygame.image.load(
                f'img/horntail/attacks/flame/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (500, 200))
            img = pygame.transform.rotate(img,90)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        global flame
        if self.animation_tick == 10: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            flame = False
            self.frame_index = 0
        else:
            self.image = self.images[self.frame_index]
