import imp
import pygame
from pygame import mixer
import os
import random
import csv
import modules.button as button
import modules.horntail as horntail
# from modules.messos import Messos


mixer.init()
pygame.init()

bottom_panel = 52.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7) + bottom_panel

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('MapleStory - Shon')

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define game variables
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 30
COLS = 43
TILE_SIZE = (SCREEN_HEIGHT-bottom_panel) // ROWS
TILE_TYPES = 21
MAX_LEVELS = 13
screen_scroll = 0
bg_scroll = 0 
level = 0
start_game = False
start_intro = False


# define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = False
grenade = False
grenade_thrown = False
rasengan_thrown = False
rasengan = False
respawn = False
pickup = False
picked = False
hp_pot = False
mana_pot = False
hp_pot_used = False
mana_pot_used = False
shop_window = False
stat_window = False
stop_music = False
# tail_attack = False
# tail_idle = True

# load music and sounds
pygame.mixer.music.load('audio/login.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0, 3000)
dragon_roar_fx = pygame.mixer.Sound('audio/dragon_roar.mp3')
dragon_roar_fx.set_volume(0.3)
jump_fx = pygame.mixer.Sound('audio/jump.wav')
jump_fx.set_volume(0.3)
double_jump_fx = pygame.mixer.Sound('audio/double_jump.ogg')
double_jump_fx.set_volume(0.3)
sword_skill_slice_fx = pygame.mixer.Sound('audio/sword_skill_slice.mp3')
sword_skill_slice_fx.set_volume(0.3)
portal_fx = pygame.mixer.Sound('audio/portal.ogg')
portal_fx.set_volume(0.3)
attack_fx = pygame.mixer.Sound('audio/attack.wav')
attack_fx.set_volume(0.3)
pickup_fx = pygame.mixer.Sound('audio/pickup.wav')
pickup_fx.set_volume(0.3)
monster_hit_fx = pygame.mixer.Sound('audio/monster_hit.wav')
monster_hit_fx.set_volume(0.3)
monster_death_fx = pygame.mixer.Sound('audio/monster_death.wav')
monster_death_fx.set_volume(0.3)
close_tab_fx = pygame.mixer.Sound('audio/close_tab.wav')
close_tab_fx.set_volume(0.3)


# load images
#mouse
mouse_img = pygame.image.load('img/icons/mouse.png').convert_alpha()
#shop
shop_npc_img = pygame.image.load('img/tile/13.png').convert_alpha()
shop_window_img = pygame.image.load('img/icons/shop.png').convert_alpha()
#stat
stat_window_img = pygame.image.load('img/icons/stat.png').convert_alpha()
stat_add_img = pygame.image.load('img/icons/stat_add.png').convert_alpha()
#portal
portal_img = pygame.image.load('img/tile/20.png').convert_alpha()
portal2_img = pygame.image.load('img/tile/19.png').convert_alpha()
#panel
panel_img = pygame.image.load('img/background/panel3.png').convert_alpha()
panel_img = pygame.transform.scale(
    panel_img, (SCREEN_WIDTH  , 60))
# button images
start_img = pygame.image.load('img/icons/play.jpg').convert_alpha()
start_img = pygame.transform.scale(start_img, (455 , 110))
exit_img = pygame.image.load('img/icons/exit.jpg').convert_alpha()
exit_img = pygame.transform.scale(exit_img, (455 , 80))
restart_img = pygame.image.load('img/icons/play.jpg').convert_alpha()
# background
horntail_img = pygame.image.load('img/Background/horntail.jpg').convert_alpha()
horntail_img = pygame.transform.scale(horntail_img, (SCREEN_WIDTH , SCREEN_HEIGHT))
fantasy_img =    pygame.image.load('img/Background/fantasy.jpg').convert_alpha()
fantasy_img = pygame.transform.scale(fantasy_img, (SCREEN_WIDTH , SCREEN_HEIGHT - 75))
omega_img =    pygame.image.load('img/Background/omega.jpg').convert_alpha()
omega_img = pygame.transform.scale(omega_img, (SCREEN_WIDTH , SCREEN_HEIGHT - 75))
elnath_img =    pygame.image.load('img/Background/elnath.png').convert_alpha()
elnath_img = pygame.transform.scale(elnath_img, (SCREEN_WIDTH , SCREEN_HEIGHT - 75))
ludi_img = pygame.image.load('img/Background/ludi.jpg').convert_alpha()
ludi_img = pygame.transform.scale(ludi_img, (SCREEN_WIDTH , SCREEN_HEIGHT - 75))
login_img = pygame.image.load('img/Background/login.jpg').convert_alpha()
login_img = pygame.transform.scale(login_img, (SCREEN_WIDTH , SCREEN_HEIGHT))
henesys_img = pygame.image.load('img/Background/henesys.jpg').convert_alpha()
henesys_img = pygame.transform.scale(henesys_img, (SCREEN_WIDTH , SCREEN_HEIGHT - 75))
# store tiles in a list
img_list_henesys = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile2/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list_henesys.append(img)
img_list_ludi = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list_ludi.append(img)
img_list_elnath = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile3/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list_elnath.append(img)
img_list_fantasy = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile5/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list_fantasy.append(img)
img_list_omega = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile4/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list_omega.append(img)
#icons
horntail_icon = pygame.image.load('img/icons/horntail.png').convert_alpha()
horntail_icon = pygame.transform.scale(horntail_icon,(25,25))
elnath_icon = pygame.image.load('img/icons/elnath.png').convert_alpha()
elnath_icon = pygame.transform.scale(elnath_icon,(25,25))
fantasy_icon = pygame.image.load('img/icons/fantasy.png').convert_alpha()
fantasy_icon = pygame.transform.scale(fantasy_icon,(25,25))
ludi_icon = pygame.image.load('img/icons/ludi.png').convert_alpha()
ludi_icon = pygame.transform.scale(ludi_icon,(25,25))
omega_icon = pygame.image.load('img/icons/omega.png').convert_alpha()
omega_icon = pygame.transform.scale(omega_icon,(25,25))

# items
sign_img = pygame.image.load('img/icons/sign.png').convert_alpha()
sign_img = pygame.transform.scale(sign_img,(80,100))
name_img = pygame.image.load('img/icons/name.png').convert_alpha()
rope_img = pygame.image.load('img/icons/rope.png').convert_alpha()
tomb_img = pygame.image.load('img/icons/tombstone.png').convert_alpha()
hp_img = pygame.image.load('img/icons/redpot.png').convert_alpha()
hp_img_big = pygame.transform.scale(hp_img,(40,40))
mana_img = pygame.image.load('img/icons/bluepot.png').convert_alpha()
mana_img_big = pygame.transform.scale(mana_img,(40,40))
messos_img = pygame.image.load('img/messos/regular/1.png').convert_alpha()
shop_messos= pygame.transform.scale(messos_img,(15,15))
#throwing
stily_img = pygame.image.load('img/icons/stily1.png').convert_alpha()
ilbi_img = pygame.image.load('img/icons/ilbi.png').convert_alpha()



# define colours
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORNAGE = (255,165,0)

# define font
font_sign = pygame.font.SysFont('rockwell', 10,True,True)
font_tutorial = pygame.font.SysFont('rockwell', 25,True,True)
font_header = pygame.font.SysFont('rockwell', 40,True,True)
font = pygame.font.SysFont('footlight', 25)
font_name = pygame.font.SysFont('Futura', 20)
font_shop = pygame.font.SysFont('Futura',15)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_text_border(text,font,in_color,x ,y,color ):
    draw_text(text,font,color,x -2,y -2)
    draw_text(text,font,color,x -2,y +2)
    draw_text(text,font,color,x +2,y -2)
    draw_text(text,font,color,x +2,y +2)
    draw_text(text,font,in_color,x,y)

def draw_bg(img):
    screen.fill(BLACK)
    width = img.get_width()
    for x in range(5):
        screen.blit(img, ((x * width) - bg_scroll * 0.5, 0))

def draw_panel():
    screen.blit(panel_img, (0, SCREEN_HEIGHT - bottom_panel))



# function to reset level
def reset_level():
    enemy_group.empty()
    enemy2_group.empty()
    enemy3_group.empty()
    enemy4_group.empty()
    enemy5_group.empty()
    enemy6_group.empty()
    enemy7_group.empty()
    enemy8_group.empty()
    bullet_group.empty()
    grenade_group.empty()
    explosion_group.empty()
    item_box_group.empty()
    decoration_group.empty()
    water_group.empty()
    exit_group.empty()
    tombstone_group.empty()
    ladder_group.empty()
    messos_group.empty()
    double_a_group.empty()
    attack_db_group.empty()
    attack_divide_group.empty()
    exit_group_pre.empty()
    exit_group_el.empty()
    exit_group_cross.empty()
    exit_group_fantasy.empty()
    exit_group_omega.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)

    return data

#functions for cutting code lines
def enemy_respawn(self):
    if self.alive == False:
        self.health = self.max_health
        self.speed = 2
        self.alive = True
        self.sound_used = False
        self.ai()
        self.update()
        self.draw()
        self.create = False
        self.got_exp = False
    
def lvl_load(self):
    old_messos = self.messos
    old_stat = self.stat
    old_stat_have = self.stat_have
    old_hp = self.health
    old_mana = self.mana
    old_exp = self.exp
    old_max_exp = self.max_exp
    old_max_mana = self.max_mana
    old_max_health = self.max_health
    old_hp_pot = self.hp_pots
    old_mp_pot = self.mana_pots
    old_lvl = self.lvl
    world_data = reset_level()
    if level <= MAX_LEVELS:
        # load in level data and create world
        with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)
        world = World()
        player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag,shop_npc = world.process_data(
            world_data)
        portal_fx.play()
        self.messos = old_messos
        self.health = old_hp
        self.mana = old_mana
        self.exp = old_exp
        self.max_exp = old_max_exp
        self.max_mana = old_max_mana
        self.max_health = old_max_health
        self.hp_pots = old_hp_pot
        self.mana_pots = old_mp_pot
        self.lvl = old_lvl
        self.stat = old_stat
        self.stat_have = old_stat_have
    

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, hp_pots, mana_pots):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.attack_cooldown = 0
        self.animation_cooldown = 0
        self.shoot_cooldown = 0
        self.shoot_bijudama_cooldown = 0
        self.shoot_rasengan_cooldown = 0
        self.attack_cooldown_enemy = 0
        self.portal_cooldown = 0
        self.doubleshoot_ = False
        self.tripleshoot_ = False
        self.quadshoot_ = False
        self.respawn = False
        self.respawn_time = 0
        self.rasengan_time = 0
        self.shooting = False
        self.hp_pots = hp_pots
        self.mana_pots = mana_pots
        #self.grenades = grenades
        #self.rasengans = rasengans
        #scale
        self.stat = 1
        self.stat_have = 0
        #health
        self.health = 100
        self.max_health = 100
        if self.char_type == 'enemy' or self.char_type == 'enemy2':
            self.health = 10000
            self.max_health = 10000
        if self.char_type == 'enemy3' or self.char_type == 'enemy4':
            self.health = 100
            self.max_health = 100
        if self.char_type == 'enemy5' or self.char_type == 'enemy6':
            self.health = 1000
            self.max_health = 1000
        if self.char_type == 'enemy7' or self.char_type == 'enemy8':
            self.health = 100000
            self.max_health = 100000
        self.mana = 100
        self.max_mana = 100
        self.exp = 0
        self.max_exp = 100
        self.got_exp = False
        self.lvl = 1
        self.dmg = -1
        self.dmg2 = -1
        self.dmg3 = -1
        self.dmg4 = -1
        self.dmg5 = -1
        self.real_dmg = 0
        self.direction = 1
        self.vel_y = 0
        self.vel_x = 0
        self.attacking = False
        self.attacking_big = False
        self.attacking_divide = False
        self.hit = False
        self.create= False
        self.died = False
        self.can_portal = False
        #sound
        self.sound_used = False
        # jump
        self.jump_down = False
        self.jump = False
        self.d_jump = False
        self.cant_jump = False
        self.in_air = True
        # rope
        self.can_move = False
        self.on_rope = False
        #mesos
        self.can_pickup = False
        self.messos = 0

        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.vision_yetti = pygame.Rect(0,50,200,20)
        self.vision_boss = pygame.Rect(0, 0, 200, 20)
        self.idling = False
        self.idling_counter = 0
        # boss variables

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump',
                           'Death', 'Attack', 'Hit', 'Attack1', 'Climb','down']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(
                f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(
                    f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(
                    img, (int(img.get_width() * scale), int(img.get_height() * scale)))   
                img = pygame.transform.flip(img, True, False)
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.portal_cooldown > 0 :
            self.portal_cooldown -= 1
            if self.portal_cooldown ==0:
                print('cooldowning')
            # self.can_portal = True
        if self.respawn_time > 0:
            self.respawn_time -= 1
        if self.attack_cooldown_enemy > 0:
            self.attack_cooldown_enemy -= 1
        if self.shoot_rasengan_cooldown > 0:
            self.shoot_rasengan_cooldown -= 1
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.shoot_bijudama_cooldown > 0:
            self.shoot_bijudama_cooldown -= 1
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1
            if self.animation_cooldown == 0:
                self.hit = False
        if self.char_type == 'enemy' and self.health <= 0 and self.create == False:
            messos = Messos(enemy.rect.centerx + screen_scroll,enemy.rect.centery, random.randint(1, 5000),self.direction)
            messos_group.add(messos)
            self.create = True
            if messos.amount < 100:
                messos.update_action(0)
            elif messos.amount >= 100 and messos.amount < 500:
                messos.update_action(1)
            elif messos.amount >= 500 and messos.amount < 2000:
                messos.update_action(2)
            elif messos.amount >= 2000 and messos.amount < 5000:
                messos.update_action(3)
        for x in range(2,8):
            if self.char_type == f'enemy{x}' and self.health <= 0 and self.create == False:
                messos = Messos(enemy.rect.centerx + screen_scroll,enemy.rect.centery, random.randint(1, 5000),self.direction)
                messos_group.add(messos)
                self.create = True
                if messos.amount < 100:
                    messos.update_action(0)
                elif messos.amount >= 100 and messos.amount < 500:
                    messos.update_action(1)
                elif messos.amount >= 500 and messos.amount < 2000:
                    messos.update_action(2)
                elif messos.amount >= 2000 and messos.amount < 5000:
                    messos.update_action(3)
        if self.exp >= self.max_exp:
            self.lvl += 1
            self.exp = 0 
            self.max_exp *= 1.2
            self.max_health += 10
            self.max_mana += 10  
            self.stat_have += 1
            
    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        #boss rects
        rope_left1 = pygame.Rect(175,510,5,240)
        rope_left2 = pygame.Rect(135,280,5,200)
        rope_right1 = pygame.Rect(1075,510,5,250)
        rope_right2 = pygame.Rect(955,215,5,200)

        #boss rects
        left_top = pygame.Rect(50,300,270,5)
        left_top1 = pygame.Rect(350,230,50,5)
        left_top2 = pygame.Rect(430,158,50,5)
        left_bot = pygame.Rect(50,525,175,5)
        left_bot1 = pygame.Rect(265,600,50,5)
        right_top = pygame.Rect(945,225,220,5)
        right_top1 = pygame.Rect(865,305,50,5)
        right_top2 = pygame.Rect(855,158,50,5)
        right_bot = pygame.Rect(1030,530,120,5)
        right_bot1 = pygame.Rect(940,600,50,5)
        right_bot2 = pygame.Rect(940,452,50,5)

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #jump down
        if moving_down and self.jump and self.rect.y < 700 and self.in_air == False:
            self.jump_down = True

        # jump
        if self.jump == True and self.in_air == False and self.cant_jump == False and moving_down== False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
            self.d_jump = True

        # double jump
        if self.d_jump == True and self.in_air == True and self.jump == True:
            self.vel_y = -11
            self.vel_x = 7 * self.direction
            double_a = DoubleJump(self.rect.centerx, self.rect.centery)
            double_a_group.add(double_a)
            double_jump_fx.play()
            self.d_jump = False
            self.cant_jump = True

        # apply gravity
        if self.on_rope:
            self.vel_x = 0
            if level == -1:
                if self.rect.colliderect(rope_right1):
                    self.rect.centerx = rope_right1.centerx
                if self.rect.colliderect(rope_right2):
                    self.rect.centerx = rope_right2.centerx
                if self.rect.colliderect(rope_left1):
                    self.rect.centerx = rope_left1.centerx
                if self.rect.colliderect(rope_left2):
                    self.rect.centerx = rope_left2.centerx
            
            self.update_action(7)
            for ladder in ladder_group:
                self.rect.centerx = ladder.rect.centerx
            if self.jump:
                self.on_rope = False
        else:
            self.vel_y += GRAVITY
            if self.vel_y > 10:
                self.vel_y
            dy += self.vel_y
            dx += self.vel_x
        
    
        # check for collision
        if not self.on_rope:
            for tile in world.obstacle_list:
                # check collision in the x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = dx
                    #dx = 0
                    # if the ai has hit a wall then make it turn around
                    if self.char_type == 'enemy':
                        self.direction *= -1
                        self.move_counter = 0
                # check for collision in the y direction
                if self.char_type == 'player':
                    if tile[1].colliderect(self.rect.x, self.rect.bottom + dy, self.width, self.height):
                        # check if below the ground, i.e. jumping
                        # if self.vel_y < 0:
                        #     self.vel_y = 0
                        #     dy = tile[1].bottom - self.rect.top

                        # check if above the ground, i.e. falling
                        if self.vel_y >= 1:
                            self.vel_y = 0
                            self.vel_x = 0
                            self.in_air = False
                            self.cant_jump = False
                            dy = tile[1].top - self.rect.bottom
                        elif self.action == 8:
                            dy = tile[1].top - self.rect.bottom + 22
                        elif self.jump_down and level != -1:
                            dy = tile[1].bottom - self.rect.bottom 
                            self.jump_down = False
                    if level == -1:
                        if self.rect.colliderect(right_bot):
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_bot.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_bot.bottom - self.rect.bottom + 60
                                self.jump_down = False
                        if self.rect.colliderect(right_bot1):
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_bot1.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_bot1.bottom - self.rect.bottom + 60 
                                self.jump_down = False
                        if self.rect.colliderect(right_bot2):
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_bot2.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_bot2.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(right_top):    
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_top.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_top.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(right_top1):   
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_top1.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_top1.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(right_top2):   
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = right_top2.top - self.rect.bottom
                            elif self.jump_down :
                                dy = right_top2.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(left_bot): 
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = left_bot.top - self.rect.bottom
                            elif self.jump_down :
                                dy = left_bot.bottom - self.rect.bottom  + 60
                                self.jump_down = False    
                        if self.rect.colliderect(left_bot1):    
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = left_bot1.top - self.rect.bottom
                            elif self.jump_down :
                                dy = left_bot1.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(left_top): 
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = left_top.top - self.rect.bottom
                            elif self.jump_down :
                                dy = left_top.bottom - self.rect.bottom  + 60
                                self.jump_down = False    
                        if self.rect.colliderect(left_top1):    
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = left_top1.top - self.rect.bottom
                            elif self.jump_down :
                                dy = left_top1.bottom - self.rect.bottom + 60 
                                self.jump_down = False    
                        if self.rect.colliderect(left_top2):    
                            if self.vel_y >= 1:
                                self.vel_y = 0
                                self.vel_x = 0
                                self.in_air = False
                                self.cant_jump = False
                                dy = left_top2.top - self.rect.bottom
                            elif self.jump_down :
                                dy = left_top2.bottom - self.rect.bottom + 60 
                                self.jump_down = False    

                elif self.char_type == 'enemy' or self.char_type == 'enemy2' or self.char_type == 'enemy3' or self.char_type == 'enemy4' \
                        or self.char_type == 'enemy5' or self.char_type == 'enemy6' or self.char_type == 'enemy7' or self.char_type == 'enemy8':
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        if self.vel_y >= 0:
                            self.vel_y = 0
                            self.in_air = False
                            dy = tile[1].top - self.rect.bottom
                    

        if self.attacking == True:
            self.attack()
        if self.attacking_divide:
            self.attack_divide()

        if level == -1 :
            #collide with flame boss
            if pygame.sprite.spritecollide(player, flame_agroup, False) and horntail.flame:
                player.health -= (player.max_health * 1/100)
            #coliide with tail dmg
            tail_dmg = pygame.Rect(50,800,1050,10)
            if self.rect.colliderect(tail_dmg) and horntail.tail_dmg:
                player.health -= (player.max_health * 2/100)
            #collide with lightning boss
            if pygame.sprite.spritecollide(player, light_agroup, False) and horntail.lightning:
                player.health -= (player.max_health * 1/100)
            #collide with fire boss
            if pygame.sprite.spritecollide(player, fire_agroup, False) and horntail.fire:
                player.health -= (player.max_health * 1/100)
        # check collision with tile 18
        if self.char_type == 'player':   
            if pygame.sprite.spritecollide(self, ladder_group, False) or self.rect.colliderect(rope_right1) and level == -1 or self.rect.colliderect(rope_right2) and level == -1\
                 or self.rect.colliderect(rope_left2) and level == -1 or self.rect.colliderect(rope_left1) and level == -1:
                self.can_move = True
                # climb
                if self.char_type == 'player' and self.can_move == True and moving_up or moving_down:
                    self.on_rope = True
                if self.on_rope and moving_up:
                    dy -= 5
                    
                    self.update_action(7)
                elif self.on_rope and moving_down:
                    dy += 5
                    self.update_action(7)
            else:
                self.on_rope = False
                self.can_move = False
        
        #check for collision with portal (9)  omega map
        level_omega = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group_omega, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            self.portal_cooldown -=1
            level_omega = True
        #check for collision with portal (10)  fantassy map
        level_fantasy = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group_fantasy, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            self.portal_cooldown -=1
            level_fantasy = True
        #check for collision with portal (11) cross way map
        level_cross = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group_cross, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            self.portal_cooldown -=1
            level_cross = True
        #check for collision with portal (12) el nath map
        level_elnath = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group_el, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            self.portal_cooldown -=1
            level_elnath = True
        #check for collision with portal (19) previous map
        level_previous = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group_pre, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            self.portal_cooldown -=1
            level_previous = True
        #check for collision with portal (20) next map
        level_complete = False
        # if self.portal_cooldown == 0:
        if pygame.sprite.spritecollide(self, exit_group, False) and moving_up and self.portal_cooldown == 0:
            self.portal_cooldown = 300
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # check if going off the edges of the screen
        if self.char_type == 'player':
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # update scroll based on player position
        # if self.char_type == 'player':
        #     if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (world.level_length * TILE_SIZE) - SCREEN_WIDTH)\
        #             or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
        #         self.rect.x -= dx
        #         screen_scroll = -dx

        return screen_scroll, level_complete ,level_previous , level_elnath,level_cross,level_fantasy,level_omega

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0 and self.mana >= 10:
            self.mana -= 5
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (1 *
                            self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            # reduce ammo
            attack_fx.play()
            bullet.timer = 5
            self.doubleshoot_ = True
            bullet.timer2 = 10
            self.tripleshoot_ =True
            bullet.timer3 = 15
            self.quadshoot_ = True
            self.update_action(4)
            
    
    def doubleshoot(self):
        self.mana -= 5
        if self.doubleshoot_:
            bullet = Bullet(self.rect.centerx + (1 *
                            self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.doubleshoot_ = False
            self.update_action(4)
    
    def tripleshoot(self):
        self.mana -= 5
        if self.tripleshoot_:
            bullet = Bullet(self.rect.centerx + (1 *
                            self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.tripleshoot_ = False
            self.update_action(4)

    def quadshoot(self):
        self.mana -= 5
        if self.quadshoot_:
            bullet = Bullet(self.rect.centerx + (1 *
                            self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            print('quad')
            self.quadshoot_ = False
            self.update_action(4)
            

    def ai(self):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)  # 0: idle
                self.idling = True
                self.idling_counter = 50
            # check if the ai in near the player
            if self.vision_yetti.colliderect(player.rect):
                # stop running and face the player
                if self.char_type == 'enemy' or self.char_type == 'enemy2' or self.char_type == 'enemy3' or self.char_type == 'enemy4' \
                        or self.char_type == 'enemy7' or self.char_type == 'enemy8' :
                        self.update_action(4)  # 4: attack
                self.enemy_attack()
            else:
                if self.idling == False and self.hit == False:
                    if self.direction == 1 :
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision_yetti.center = (
                        self.rect.centerx  * self.direction, self.rect.centery)
                    # pygame.draw.rect(screen,WHITE,self.vision_yetti)
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            # if self.action == 8:
            #     player.rect.y += 22
            if self.action == 3 and self.died == False:
                self.frame_index = len(self.animation_list[self.action]) -1
                if self.char_type == 'player':
                    tombstone =Tombstone(self.rect.centerx,self.rect.centery - 700,self.direction)
                    tombstone_group.add(tombstone)
                    self.died=True
                elif self.char_type == 'enemy' and self.got_exp == False:
                    player.exp += 200
                    self.got_exp = True
                elif self.char_type == 'enemy2' and self.got_exp == False:
                    player.exp += 250
                    self.got_exp = True
                elif self.char_type == 'enemy3' and self.got_exp == False:
                    player.exp += 30
                    self.got_exp = True
                elif self.char_type == 'enemy4' and self.got_exp == False:
                    player.exp += 40
                    self.got_exp = True
                elif self.char_type == 'enemy5' and self.got_exp == False:
                    player.exp += 100
                    self.got_exp = True
                elif self.char_type == 'enemy6' and self.got_exp == False:
                    player.exp += 125
                    self.got_exp = True
                elif self.char_type == 'enemy7' and self.got_exp == False:
                    player.exp += 400
                    self.got_exp = True
                elif self.char_type == 'enemy8' and self.got_exp == False:
                    player.exp += 500
                    self.got_exp = True
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            if self.char_type == 'enemy' and self.sound_used == False:
                monster_death_fx.play()
                self.sound_used= True
            for x in range(2,8):
                if self.char_type == f'enemy{x}' and self.sound_used == False:
                    monster_death_fx.play()
                    self.sound_used= True
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(
            self.image, self.flip, False), self.rect)
        if self.char_type == 'enemy' and self.health < 10000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 13, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 15, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 15, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy2' and self.health < 10000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 43, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 45, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 45, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy3' and self.health < 100 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy4' and self.health < 100 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy5' and self.health < 1000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy6' and self.health < 1000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy7' and self.health < 100000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        if self.char_type == 'enemy8' and self.health < 100000 and self.alive:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (self.rect.x + 33, self.rect.y -2, 54, 14))
            pygame.draw.rect(screen, WHITE, (self.rect.x + 35, self.rect.y, 50, 10))
            pygame.draw.rect(screen, GREEN, (self.rect.x + 35, self.rect.y, 50 * ratio, 10))
        
        


    def attack(self):
        if self.stat >= 1:
            self.dmg = random.randint(0,9) 
            self.dmg2 = random.randint(1,9) *10
            self.real_dmg = self.dmg + self.dmg2
        if self.stat >= 5:
            self.dmg2 = random.randint(5,9) *10
        if self.stat >= 10:
            self.dmg2 = random.randint(0,9) *10
            self.dmg3 = random.randint(1,9) * 100
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3
        if self.stat >= 15:
            self.dmg3 = random.randint(5,9) * 100
        if self.stat >= 20:
            self.dmg3 = random.randint(0,9) *100
            self.dmg4 = random.randint(1,9) * 1000
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3 + self.dmg4
        if self.stat >= 25:
            self.dmg4 = random.randint(0,9) *1000
            self.dmg5 = random.randint(1,5) * 10000
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3 + self.dmg4 + self.dmg5
        if self.stat >= 30:
            self.dmg5 = random.randint(1,9) *10000

        if self.attack_cooldown == 0 and self.attacking == True and self.mana >= 10:
            # execute attak
            self.mana -= 10
            attacking_rect = pygame.Rect(
                self.rect.centerx - (2*self.rect.width), self.rect.y, 4*self.rect.width, self.rect.height)
            # pygame.draw.rect(screen,WHITE,attacking_rect)
            self.attack_cooldown = 20

            attack_db = DualBlade(self.rect.centerx, self.rect.centery)
            attack_db_group.add(attack_db)
            sword_skill_slice_fx.play()
            def dmgskin():
                dmg = DmgSkin(enemy.rect.centerx +40 ,enemy.rect.centery)
                dmg_group.add(dmg)
                dmg2 = DmgSkin2(enemy.rect.centerx +20 ,enemy.rect.centery)
                dmg_group.add(dmg2)
                if self.dmg3 >= 0:
                    dmg3=DmgSkin3(enemy.rect.centerx ,enemy.rect.centery)
                    dmg_group.add(dmg3)
                if self.dmg4 >= 0:
                    dmg4=DmgSkin4(enemy.rect.centerx -20,enemy.rect.centery)
                    dmg_group.add(dmg4)
                if self.dmg5 >= 0:
                    dmg5=DmgSkin5(enemy.rect.centerx -40,enemy.rect.centery)
                    dmg_group.add(dmg5)
                

            for enemy in enemy_group :
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        print(enemy.health)
                        print(self.real_dmg)
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy2_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy3_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        print(self.real_dmg)
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy4_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy5_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy6_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy7_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy8_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()

    def attack_divide(self):
        if self.stat >= 1:
            self.dmg = random.randint(0,9) 
            self.dmg2 = random.randint(1,9) *10
            self.real_dmg = self.dmg + self.dmg2
        if self.stat >= 5:
            self.dmg2 = random.randint(5,9) *10
        if self.stat >= 10:
            self.dmg2 = random.randint(0,9) *10
            self.dmg3 = random.randint(1,9) * 100
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3
        if self.stat >= 15:
            self.dmg3 = random.randint(5,9) * 100
        if self.stat >= 20:
            self.dmg3 = random.randint(0,9) *100
            self.dmg4 = random.randint(1,9) * 1000
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3 + self.dmg4
        if self.stat >= 25:
            self.dmg4 = random.randint(0,9) *1000
            self.dmg5 = random.randint(1,5) * 10000
            self.real_dmg = self.dmg + self.dmg2 + self.dmg3 + self.dmg4 + self.dmg5
        if self.stat >= 30:
            self.dmg5 = random.randint(1,9) *10000

        if self.attack_cooldown == 0 and self.attacking_divide == True and self.mana >= 10:
            # execute attak
            self.mana -= 10
            if player.direction == 1:
                attacking_rect = pygame.Rect(
                    player.rect.centerx , player.rect.y - 80, 10*player.rect.width, 4*player.rect.height)
            elif player.direction == -1:
                attacking_rect = pygame.Rect(
                    player.rect.centerx - 400 , player.rect.y - 80, 10*player.rect.width, 4*player.rect.height)
            # pygame.draw.rect(screen,WHITE,attacking_rect)
            self.attack_cooldown = 60

            attack_db = Adele_divide(self.rect.centerx, self.rect.centery)
            attack_db_group.add(attack_db)
            sword_skill_slice_fx.play()
            def dmgskin():
                dmg = DmgSkin(enemy.rect.centerx +40 ,enemy.rect.centery)
                dmg_group.add(dmg)
                dmg2 = DmgSkin2(enemy.rect.centerx +20 ,enemy.rect.centery)
                dmg_group.add(dmg2)
                if self.dmg3 >= 0:
                    dmg3=DmgSkin3(enemy.rect.centerx ,enemy.rect.centery)
                    dmg_group.add(dmg3)
                if self.dmg4 >= 0:
                    dmg4=DmgSkin4(enemy.rect.centerx -20,enemy.rect.centery)
                    dmg_group.add(dmg4)
                if self.dmg5 >= 0:
                    dmg5=DmgSkin5(enemy.rect.centerx -40,enemy.rect.centery)
                    dmg_group.add(dmg5)
                    
            for enemy in enemy_group :
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        print(enemy.health)
                        print(self.real_dmg)
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()

            for enemy in enemy2_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            
            for enemy in enemy3_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        print(self.real_dmg)
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            
            for enemy in enemy4_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy5_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy6_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy7_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()
            for enemy in enemy8_group:
                if attacking_rect.colliderect(enemy.rect):
                    if enemy.alive:
                        enemy.health -= self.real_dmg
                        enemy.hit = True
                        monster_hit_fx.play()
                        enemy.animation_cooldown = 10
                        enemy.update_action(5)
                        dmgskin()

            global horn_legs 
            global horn_wings
            global horn_right
            global horn_left 
            global horn_tail 
            global horn_heada
            global horn_headb
            global horn_headc
            global horn_health
            #horntail collide
            head_ar = pygame.Rect(420,250,150,150)
            head_br = pygame.Rect(590,225,120,170)
            head_cr = pygame.Rect(730,250,150,150)
            tail_r = pygame.Rect(815,750,200,70)
            wings_r = pygame.Rect(550,470,200,130)
            legs_r = pygame.Rect(510,630,300,200)
            left_r = pygame.Rect(430,435,100,170)
            right_r = pygame.Rect(764,435,100,170)
            def dmgskinboss(self):
                dmg = DmgSkin(self.centerx +40 ,self.centery)
                dmg_group.add(dmg)
                dmg2 = DmgSkin2(self.centerx +20 ,self.centery)
                dmg_group.add(dmg2)
                if player.dmg3 >= 0:    
                    dmg3=DmgSkin3(self.centerx ,self.centery)
                    dmg_group.add(dmg3)
                if player.dmg4 >= 0:
                    dmg4=DmgSkin4(self.centerx -20,self.centery)
                    dmg_group.add(dmg4)
                if player.dmg5 >= 0:
                    dmg5=DmgSkin5(self.centerx -40,self.centery)
                    dmg_group.add(dmg5)
                
            if level == -1:
                if attacking_rect.colliderect(head_ar) and horn_heada > 0:
                    horn_heada -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(head_ar)
                if attacking_rect.colliderect(head_br) and horn_headb > 0:
                    horn_headb -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(head_br)
                if attacking_rect.colliderect(head_cr) and horn_headc > 0:
                    horn_headc -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(head_cr)
                if attacking_rect.colliderect(tail_r) and horn_tail > 0:
                    horn_tail -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    dmgskinboss(tail_r)
                    self.kill()
                if attacking_rect.colliderect(wings_r) and horn_wings > 0:
                    horn_wings -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(wings_r)
                if attacking_rect.colliderect(legs_r) and horn_legs > 0:
                    horn_legs -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(legs_r)
                if attacking_rect.colliderect(left_r) and horn_left > 0:
                    horn_left -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(left_r)
                if attacking_rect.colliderect(right_r) and horn_right > 0:
                    horn_right -= player.dmg5 // 10000
                    horn_health -= player.dmg5 // 10000
                    self.kill()
                    dmgskinboss(right_r)


    def enemy_attack(self):
        if self.attack_cooldown_enemy == 0:
            # execute attak
            attacking_rect_enemy = pygame.Rect(
                self.rect.centerx - self.rect.width, self.rect.y, 2*self.rect.width, self.rect.height)
            #pygame.draw.rect(screen,WHITE,attacking_rect_enemy)
            self.attack_cooldown_enemy = 100
            if attacking_rect_enemy.colliderect(player.rect):
                if player.alive:
                    if self.char_type == 'enemy3' or self.char_type == 'enemy4':
                        player.health -= 10
                    if self.char_type == 'enemy5' or self.char_type == 'enemy6':
                        player.health -= 20
                    if self.char_type == 'enemy' or self.char_type == 'enemy2':
                        player.health -= 30
                    if self.char_type == 'enemy7' or self.char_type == 'enemy8':
                        player.health -= 40
                    
                    player.hit = True


    def attack_big(self, target):
        self.attacking_big = True
        attacking_rect_r = pygame.Rect(
            self.rect.centerx  , self.rect.centery , 400, 400)
        #pygame.draw.rect(screen, BLACK, attacking_rect_r)
        attacking_rect_l = pygame.Rect(
            self.rect.centerx  - 400 , self.rect.centery , 400, 400)
        #pygame.draw.rect(screen, BLACK, attacking_rect_l)
        attacking_rect_u = pygame.Rect(
            self.rect.centerx -400 , self.rect.centery - 400 , 400, 400)
        #pygame.draw.rect(screen, BLACK, attacking_rect_u)
        attacking_rect_d = pygame.Rect(
            self.rect.centerx   , self.rect.centery - 400 , 400, 400)
        #pygame.draw.rect(screen, BLACK, attacking_rect_d)
        dragon_roar = DragonRoar(self.rect.centerx, self.rect.centery)
        dragon_roar_group.add(dragon_roar)
        dragon_roar_fx.play()

        
        if attacking_rect_r.colliderect(target.rect):
            target.health -= target.max_health
            monster_hit_fx.play()
        if attacking_rect_l.colliderect(target.rect):
            target.health -= target.max_health
            monster_hit_fx.play()
        if attacking_rect_u.colliderect(target.rect):
            target.health -= target.max_health
            monster_hit_fx.play()
        if attacking_rect_d.colliderect(target.rect):
            target.health -= target.max_health
            monster_hit_fx.play()

class Messos(pygame.sprite.Sprite):
    def __init__(self, x, y,amount,direction):
        pygame.sprite.Sprite.__init__(self)
        self.drop = False
        self.amount = amount
        self.created = False
        self.update_time = pygame.time.get_ticks() 
        self.meso_type = 0
        self.picked = False
        self.speed = 2
        self.direction = direction
        self.vel_x = 0
        self.vel_y = -11
        self.frame_index = 0
        self.can_pickup = False
        self.animation_list = [] 
        animation_types = ['regular', 'special', 'cash','bag']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(
                f'img/messos/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(
                    f'img/messos/{animation}/{i}.png').convert_alpha()
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.meso_type][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def update(self):
        self.update_animation()
        self.vel_y += GRAVITY
        dy = self.vel_y
        dx = self.direction * self.speed

        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                if self.vel_y > 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        collided_messos = pygame.sprite.spritecollideany(player, messos_group)
        if collided_messos != None and pickup:
            player.messos += collided_messos.amount
            print(player.messos)
            pickup_fx.play()
            collided_messos.kill()
            
    


    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.meso_type][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.meso_type]):
            if self.meso_type == 3:
                self.frame_index = len(self.animation_list[self.meso_type]) -1
            else:
                self.frame_index = 0

    def update_action(self, meso_type):
        # check if the new action is different to the previous one
        if meso_type != self.meso_type:
            self.meso_type = meso_type
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        

    def draw(self):
        screen.blit(self.image, self.rect)

class World():
    def __init__(self):
        self.obstacle_list = []
    def process_data(self, data):
        self.level_length = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    if level == 1 or level == 0 or level == -1:
                        img = img_list_henesys[tile]
                    elif level >= 2 and level <= 4:
                        img = img_list_ludi[tile]
                    elif level >= 5 and level <= 7:
                        img = img_list_elnath[tile]
                    elif level >= 8 and level <= 10:
                        img = img_list_fantasy[tile]
                    elif level >= 11 and level <= 13:
                        img = img_list_omega[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE 
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 3 or tile >= 5 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile == 4:
                        decoration = Decoration(img,x*TILE_SIZE,y*TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 9: 
                        exit6 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group_omega.add(exit6)
                    elif tile == 10:
                        exit5 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group_fantasy.add(exit5)
                    elif tile == 11:
                        exit4 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group_cross.add(exit4)
                    elif tile == 12:
                        exit3 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group_el.add(exit3)
                    elif tile == 13:
                        shop_npc = ShopNPC(x,y)
                    elif tile == 14:
                        boss = Soldier('boss', x * TILE_SIZE,
                                       y * TILE_SIZE, 1, 3, 10, 0, 0)
                        health_bar_boss = HealthBar(
                            625, 10, boss.health, boss.health)
                    elif tile == 15:  # create player
                        player = Soldier('player', x * TILE_SIZE,
                                         y * TILE_SIZE, 0.8, 5, 1000, 10, 100)
                        health_bar = HealthBar(
                            200, 870, player.health, player.max_health)
                        mana_bar = ManaBar(
                            370, 870, player.mana, player.max_mana)
                        exp_bar = ExpBar(
                            540, 870, player.exp, player.max_exp)
                        name_tag = NameTag(player.rect.centerx,player.rect.bottom,'shon')
                    elif tile == 16:  # create enemies
                        if level >= 2 and level <= 4:
                            enemy = Soldier('enemy', x * TILE_SIZE,
                                            y * TILE_SIZE, 1, 2, 20, 0, 0)
                            enemy_group.add(enemy)
                        elif level >= 5 and level <= 7:
                            enemy3 = Soldier('enemy3', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy3_group.add(enemy3)
                        elif level >= 8 and level <= 10:
                            enemy5 = Soldier('enemy5', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy5_group.add(enemy5)
                        elif level >= 11 and level <= 13:
                            enemy7 = Soldier('enemy7', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy7_group.add(enemy7)
                    elif tile == 17:  
                        if level >= 2 and level <= 4:
                            enemy2 = Soldier('enemy2', x * TILE_SIZE,
                                         y * TILE_SIZE, 1, 2, 20, 0, 0)
                            enemy2_group.add(enemy2)
                        elif level >= 5 and level <= 7:
                            enemy4 = Soldier('enemy4', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy4_group.add(enemy4)
                        elif level >= 8 and level <= 10:
                            enemy6 = Soldier('enemy6', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy6_group.add(enemy6)
                        elif level >= 11 and level <= 13:
                            enemy8 = Soldier('enemy8', x * TILE_SIZE,
                                            y * TILE_SIZE , 1, 1, 20, 0, 0)
                            enemy8_group.add(enemy8)
                    elif tile == 18:  # create grenade box
                        ladder = Ladder(
                            x * TILE_SIZE, y * TILE_SIZE)
                        ladder_group.add(ladder)
                    elif tile == 19:  # create portal previous
                        exit2 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group_pre.add(exit2)
                    elif tile == 20:  # create portal next
                        exit1 = Exit( x * TILE_SIZE, y * TILE_SIZE)
                        exit_group.add(exit1)

        return player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc

    
    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])

class Decoration(pygame.sprite.Sprite):
	def __init__(self, img, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

class NameTag(pygame.sprite.Sprite):
    def __init__(self, x, y,name):
        self.image = name_img
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.name = name
    
    def draw(self,name):
        screen.blit(self.image,(player.rect.centerx - 33,player.rect.bottom + 5))
        draw_text(f'{name}',font_name,WHITE,player.rect.centerx - 15 , player.rect.bottom + 8 )

    def update(self):
        self.rect.x += screen_scroll

class Mouse(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = mouse_img
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        pygame.mouse.get_pos(x,y)
    
    def draw():
        screen.blit(mouse_img,(pygame.mouse.get_pos(x),pygame.mouse.get_pos(y)))
    
    def update(self):
        self.rect.x += screen_scroll

class DmgSkin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = player.dmg
        self.image = pygame.image.load(f'img/dmg/{self.dmg}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.distance = 0

    def update(self):
        self.rect.x += screen_scroll
        self.rect.y -= 1
        self.distance +=1
        if self.distance > 100:
            self.kill()

class DmgSkin2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = player.dmg2 // 10
        self.image = pygame.image.load(f'img/dmg/{self.dmg}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.distance = 0

    def update(self):
        self.rect.x += screen_scroll
        self.rect.y -= 1
        self.distance +=1
        if self.distance > 100:
            self.kill()

class DmgSkin3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = player.dmg3 // 100
        self.image = pygame.image.load(f'img/dmg/{self.dmg}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.distance = 0

    def update(self):
        self.rect.x += screen_scroll
        self.rect.y -= 1
        self.distance +=1
        if self.distance > 100:
            self.kill()

class DmgSkin4(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = player.dmg4 // 1000
        self.image = pygame.image.load(f'img/dmg/{self.dmg}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.distance = 0

    def update(self):
        self.rect.x += screen_scroll
        self.rect.y -= 1
        self.distance +=1
        if self.distance > 100:
            self.kill()

class DmgSkin5(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = player.dmg5 // 10000
        self.image = pygame.image.load(f'img/dmg/{self.dmg}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.distance = 0

    def update(self):
        self.rect.x += screen_scroll
        self.rect.y -= 1
        self.distance +=1
        if self.distance > 100:
            self.kill()

class Sign(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =sign_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def draw():
        screen.blit(sign_img,(340,465))
        screen.blit(fantasy_icon,(350,495))
        screen.blit(sign_img,(880,465))
        screen.blit(omega_icon,(890,495))
        screen.blit(sign_img,(340,660))
        screen.blit(elnath_icon,(350,690))
        screen.blit(sign_img,(880,660))
        screen.blit(ludi_icon,(890,690))

    def update(self):
        self.rect.x += screen_scroll

class SignBoss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image =sign_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def draw():
        screen.blit(sign_img,(140,730))
        screen.blit(horntail_icon,(150,760))


    def update(self):
        self.rect.x += screen_scroll

class ShopNPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = shop_npc_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def draw(self):
        screen.blit(shop_npc_img,(700,558))

    def update(self):
        self.rect.x += screen_scroll

class ShopWindow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = shop_window_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def draw():
        screen.blit(shop_window_img,(400,300))
        screen.blit(hp_img,(413,468))
        draw_text('10',font_shop,BLACK,413,485)
        draw_text('Red Pot x10',font_shop,BLACK,453,468)
        screen.blit(mana_img,(413,510))
        draw_text('10',font_shop,BLACK,413,527)
        draw_text('Blue Pot x10',font_shop,BLACK,453,510)
        screen.blit(shop_messos,(450,480))
        draw_text('1000 messos',font_shop,BLACK,470,485)
        screen.blit(shop_messos,(450,522))
        draw_text('1000 messos',font_shop,BLACK,470,527)

    def update(self):
        self.rect.x += screen_scroll

class StatWindow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = stat_window_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def draw():
        screen.blit(stat_window_img,(300,200))
        screen.blit(stat_add_img,(465,464))
        draw_text(f'{player.stat_have}',font_shop,BLACK,378,438)
        draw_text(f'{player.stat}',font_shop,BLACK,375,464)
        draw_text('4',font_shop,BLACK,375,482)
        draw_text('4',font_shop,BLACK,375,500)
        draw_text('4',font_shop,BLACK,375,518)
        draw_text('shon',font_shop,BLACK,375,234)
        draw_text('GM',font_shop,BLACK,375,252)
        draw_text(f'{player.lvl}',font_shop,BLACK,375,270)
        draw_text(f'{player.exp}/{player.max_exp}',font_shop,BLACK,375,288)
        draw_text(f'{player.health}/{player.max_health}',font_shop,BLACK,375,360)
        draw_text(f'{player.mana}/{player.max_mana}',font_shop,BLACK,375,378)
        draw_text('999',font_shop,BLACK,375,396)
        draw_text('999,999 ~ 999,999',font_shop,BLACK,565,255)
        draw_text('100 %',font_shop,BLACK,565,273)
        draw_text('9,999',font_shop,BLACK,565,291)
        draw_text('9,999',font_shop,BLACK,565,309)
        draw_text('9,999',font_shop,BLACK,565,327)
        draw_text('9,999',font_shop,BLACK,565,345)
        draw_text('9,999',font_shop,BLACK,565,363)
        draw_text('9,999',font_shop,BLACK,565,381)
        draw_text('160',font_shop,BLACK,565,399)
        draw_text('123',font_shop,BLACK,565,417)

    def update(self):
        self.rect.x += screen_scroll

class PlayerLevel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 64, 44))
        pygame.draw.rect(screen, ORNAGE, (self.x, self.y, 60, 40))

    def update(self):
        self.rect.x += screen_scroll

class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = portal_img
        self.image = pygame.transform.scale(img,(60,100))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll

class Potion(pygame.sprite.Sprite):
    def __init__(self,img, x, y,potion_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.potion_type = potion_type
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = player.health / player.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))

    def update(self):
        self.x += screen_scroll
        self.max_health = player.max_health
        self.health = player.health

class HealthBarEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, health, max_health):
        super().__init__()
        self.image = pygame.Surface([50, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.rect.x - 2, self.rect.y - 2, 52, 12))
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y , 50, 10))
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y , 50 * ratio, 10))

    def update(self):
        #ratio = self.health / self.max_health
        self.rect.x += screen_scroll    
        for enemy in enemy_group:
            self.rect.x = enemy.rect.centerx - 25
            self.rect.y = enemy.rect.centery - 35
            if enemy.alive == False:
                self.rect.x = -200

class HealthBarHorn():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.screen = screen

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y - 3, 1010, 46))
        pygame.draw.rect(screen, RED, (self.x, self.y, 1000, 40))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 1000 * ratio, 40))

    def update(self):
        self.health = horn_health

class ManaBar():
    def __init__(self, x, y, mana, max_mana):
        self.x = x
        self.y = y
        self.mana = mana
        self.max_mana = max_mana

    def draw(self, mana):
        # update with new mana
        self.mana = mana
        # calculate mana ratio
        ratio = player.mana / player.max_mana
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 150 * ratio, 20))

    def update(self):
        self.x += screen_scroll
        self.max_mana = player.max_mana
        self.mana = player.mana

class ExpBar():
    def __init__(self, x, y, exp, max_exp):
        self.x = x
        self.y = y
        self.exp = exp
        self.max_exp = max_exp

    def draw(self, exp ):
        # update with new mana
        self.exp = exp
        # calculate mana ratio
        ratio = player.exp / player.max_exp
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, 150 * ratio, 20))

    def update(self):
        self.x += screen_scroll
        self.max_exp = player.max_exp
        self.exp = player.exp

class Tombstone(pygame.sprite.Sprite):
    def __init__(self, x, y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.vel_y = 5
        self.image = tomb_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.timer = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction


    def update(self):
        dy = self.vel_y
        # move tomb
        if self.direction == 1:
            self.image = pygame.transform.flip(tomb_img, True, False)
        # check for collision with player
        if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):   
            if self.vel_y >= 0:
                self.vel_y = 0
                dy = player.rect.bottom - self.rect.bottom
    
        self.rect.x += screen_scroll
        self.rect.y += dy

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = ilbi_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.timer = 0
        self.timer2 = 0
        self.timer3 = 0

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll
        if self.direction == 1:
            self.image = pygame.transform.flip(ilbi_img, True, False)
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        # check for collision with level
        # for tile in world.obstacle_list:
        #     if tile[1].colliderect(self.rect):
        #         self.kill()
        self.timer -= 1
        self.timer2 -= 1
        self.timer3 -= 1
        if self.timer == 0:
            player.doubleshoot()
        if self.timer2 == 0 and player.lvl >= 10:
            player.tripleshoot()
        if self.timer3 == 0 and player.lvl >= 20:
            player.quadshoot()
        
        if player.stat >= 1:
            player.dmg = random.randint(0,9) 
            player.dmg2 = random.randint(1,9) *10
            player.real_dmg = player.dmg + player.dmg2
        if player.stat >= 5:
            player.dmg2 = random.randint(5,9) *10
        if player.stat >= 10:
            player.dmg2 = random.randint(0,9) *10
            player.dmg3 = random.randint(1,9) * 100
            player.real_dmg = player.dmg + player.dmg2 + player.dmg3
        if player.stat >= 15:
            player.dmg3 = random.randint(5,9) * 100
        if player.stat >= 20:
            player.dmg3 = random.randint(0,9) *100
            player.dmg4 = random.randint(1,9) * 1000
            player.real_dmg = player.dmg + player.dmg2 + player.dmg3 + player.dmg4
        if player.stat >= 25:
            player.dmg4 = random.randint(0,9) *1000
            player.dmg5 = random.randint(1,5) * 10000
            player.real_dmg = player.dmg + player.dmg2 + player.dmg3 + player.dmg4 + player.dmg5
        if player.stat >= 30:
            player.dmg5 = random.randint(1,9) *10000
        # check collision with characters
        def dmgskin():
            dmg = DmgSkin(enemy.rect.centerx +40 ,enemy.rect.centery)
            dmg_group.add(dmg)
            dmg2 = DmgSkin2(enemy.rect.centerx +20 ,enemy.rect.centery)
            dmg_group.add(dmg2)
            if player.dmg3 >= 0:
                dmg3=DmgSkin3(enemy.rect.centerx ,enemy.rect.centery)
                dmg_group.add(dmg3)
            if player.dmg4 >= 0:
                dmg4=DmgSkin4(enemy.rect.centerx -20,enemy.rect.centery)
                dmg_group.add(dmg4)
            if player.dmg5 >= 0:
                dmg5=DmgSkin5(enemy.rect.centerx -40,enemy.rect.centery)
                dmg_group.add(dmg5)

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
                
        
        for enemy in enemy2_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()

        for enemy in enemy3_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        
        for enemy in enemy4_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        for enemy in enemy5_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        for enemy in enemy6_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        for enemy in enemy7_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        for enemy in enemy8_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= player.real_dmg 
                    self.kill()
                    enemy.hit = True
                    monster_hit_fx.play()
                    enemy.animation_cooldown = 10
                    enemy.update_action(5)
                    dmgskin()
        
        #vars health
        global horn_legs 
        global horn_wings
        global horn_right
        global horn_left 
        global horn_tail 
        global horn_heada
        global horn_headb
        global horn_headc
        global horn_health
        #horntail collide
        head_ar = pygame.Rect(420,250,150,150)
        head_br = pygame.Rect(590,225,120,170)
        head_cr = pygame.Rect(730,250,150,150)
        tail_r = pygame.Rect(815,750,200,70)
        wings_r = pygame.Rect(550,470,200,130)
        legs_r = pygame.Rect(510,630,300,200)
        left_r = pygame.Rect(430,435,100,170)
        right_r = pygame.Rect(764,435,100,170)
        def dmgskinboss(self):
            dmg = DmgSkin(self.centerx +40 ,self.centery)
            dmg_group.add(dmg)
            dmg2 = DmgSkin2(self.centerx +20 ,self.centery)
            dmg_group.add(dmg2)
            if player.dmg3 >= 0:    
                dmg3=DmgSkin3(self.centerx ,self.centery)
                dmg_group.add(dmg3)
            if player.dmg4 >= 0:
                dmg4=DmgSkin4(self.centerx -20,self.centery)
                dmg_group.add(dmg4)
            if player.dmg5 >= 0:
                dmg5=DmgSkin5(self.centerx -40,self.centery)
                dmg_group.add(dmg5)
        if level == -1:
            if self.rect.colliderect(head_ar) and horn_heada > 0:
                horn_heada -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(head_ar)
            if self.rect.colliderect(head_br) and horn_headb > 0:
                horn_headb -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(head_br)
            if self.rect.colliderect(head_cr) and horn_headc > 0:
                horn_headc -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(head_cr)
            if self.rect.colliderect(tail_r) and horn_tail > 0:
                horn_tail -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                dmgskinboss(tail_r)
                self.kill()
            if self.rect.colliderect(wings_r) and horn_wings > 0:
                horn_wings -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(wings_r)
            if self.rect.colliderect(legs_r) and horn_legs > 0:
                horn_legs -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(legs_r)
            if self.rect.colliderect(left_r) and horn_left > 0:
                horn_left -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(left_r)
            if self.rect.colliderect(right_r) and horn_right > 0:
                horn_right -= player.dmg5 // 10000
                horn_health -= player.dmg5 // 10000
                self.kill()
                dmgskinboss(right_r)


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = rope_img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y +
                            (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll

class DoubleJump(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 13):
            img = pygame.image.load(
                f'img/doublejump/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (100, 50))
            if player.direction == 1:
                img = pygame.transform.flip(img, True, False)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        self.rect.y = player.rect.y + 20
        if player.direction == -1:
            self.rect.x = player.rect.x + 40
        else:
            self.rect.x = player.rect.x - 100

        # update explosion amimation
        if self.animation_tick == 1: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.frame_index]

class Adele_divide(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 9):
            img = pygame.image.load(
                f'img/adele_divide/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (500, 300))
            if player.direction == 1:
                img = pygame.transform.flip(img, True, False)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_tick = 0

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        self.rect.y = player.rect.y - 100
        if player.direction == -1:
            self.rect.x = player.rect.x - 450
        else:
            self.rect.x = player.rect.x - 50

        # update explosion amimation
        if self.animation_tick == 3: #change 20 to how ever many ticks in between animation frames
            self.frame_index += 1
            self.animation_tick = 0 #reset tick back to 0 after changing frame
        self.animation_tick += 1 #add 1 each iteration of the while loop
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.frame_index]

class DualBlade(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 6):
            img = pygame.image.load(
                f'img/dualblade/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (100, 100))
            if player.direction == -1:
                img = pygame.transform.flip(img, True, False)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        # update explosion amimation
        self.frame_index += 1
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.frame_index]

class DragonRoar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 15):
            img = pygame.image.load(
                f'img/dragon_roar/{num}.png').convert_alpha()
            img = pygame.transform.scale(
                img, (100, 100))
            if player.direction == -1:
                img = pygame.transform.flip(img, True, False)
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        # update explosion amimation
        self.frame_index += 1
        # if the animation is complete then delete the explosion
        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.frame_index]

class ScreenFade():
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:  # whole screen fade
            pygame.draw.rect(
                screen, self.colour, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (SCREEN_WIDTH //
                             2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, 0 -
                             self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
            pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT //
                             2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.direction == 2:  # vertical screen fade down
            pygame.draw.rect(screen, self.colour,
                             (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if self.fade_counter >= SCREEN_WIDTH:
            fade_complete = True

        return fade_complete

# create screen fades
intro_fade = ScreenFade(1, BLACK, 6)
death_fade = ScreenFade(0, PINK, 4)

# create buttons
start_button = button.Button(560,335, start_img, 1)
exit_button = button.Button(560,510, exit_img, 1)
restart_button = button.Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, restart_img, 2)

# create sprite groups
head_a_group = pygame.sprite.Group()  
part = horntail.Head_a(525,335)
head_a_group.add(part)
head_aa_group = pygame.sprite.Group()  
part = horntail.Head_aa(525,355)
head_aa_group.add(part)
head_adgroup = pygame.sprite.Group()  
dead = horntail.Head_ad(525,335)
head_adgroup.add(dead)
head_b_group = pygame.sprite.Group()  
part = horntail.Head_b(648,275)
head_b_group.add(part)
head_ba_group = pygame.sprite.Group()  
part = horntail.Head_ba(648,275)
head_ba_group.add(part)
head_bdgroup = pygame.sprite.Group()  
dead = horntail.Head_bd(648,275)
head_bdgroup.add(dead)
head_c_group = pygame.sprite.Group()  
part = horntail.Head_c(770,335)
head_c_group.add(part)
head_cagroup = pygame.sprite.Group()  
part = horntail.Head_ca(770,335)
head_cagroup.add(part)
head_cdgroup = pygame.sprite.Group()  
dead = horntail.Head_cd(770,335)
head_cdgroup.add(dead)
left_group = pygame.sprite.Group()  
part = horntail.Left_Hand(535,534)
left_group.add(part)
left_agroup = pygame.sprite.Group()  
part = horntail.Left_aHand(491,504)
left_agroup.add(part)
left_dgroup = pygame.sprite.Group()  
dead = horntail.Left_d(535,534)
left_dgroup.add(dead)
right_group = pygame.sprite.Group()  
part = horntail.Right_Hand(764,534)
right_group.add(part)
right_agroup = pygame.sprite.Group()  
part = horntail.Right_aHand(809,504)
right_agroup.add(part)
right_dgroup = pygame.sprite.Group()  
dead = horntail.Right_d(764,534)
right_dgroup.add(dead)
tail_group = pygame.sprite.Group()  
part = horntail.Tail(865,725)
tail_group.add(part)
tail_agroup = pygame.sprite.Group()  
part = horntail.Tail_a(865,725)
tail_agroup.add(part)
tail_dgroup = pygame.sprite.Group()  
dead = horntail.Tail_d(865,725)
tail_dgroup.add(dead)
legs_group = pygame.sprite.Group()  
part = horntail.Legs(650,730)
legs_group.add(part)
legs_agroup = pygame.sprite.Group()  
part = horntail.Legs_a(650,730)
legs_agroup.add(part)
legs_dgroup = pygame.sprite.Group()  
dead = horntail.Legs_d(650,730)
legs_dgroup.add(dead)
wings_group = pygame.sprite.Group()  
part = horntail.Wings(650,600)
wings_group.add(part)
wings_agroup = pygame.sprite.Group()  
part = horntail.Wings_a(650,600)
wings_agroup.add(part)
wings_dgroup = pygame.sprite.Group()  
dead = horntail.Wings_d(650,600)
wings_dgroup.add(dead)
fire_agroup = pygame.sprite.Group()  
attack = horntail.Fire(200,200)
fire_agroup.add(attack)
attack = horntail.Fire(200,400)
fire_agroup.add(attack)
attack = horntail.Fire(350,150)
fire_agroup.add(attack)
light_agroup = pygame.sprite.Group()  
attack = horntail.Lightning(990,80)
light_agroup.add(attack)
attack = horntail.Lightning(1040,380)
light_agroup.add(attack)
flame_agroup = pygame.sprite.Group()  
attack = horntail.Flame(630,600)
flame_agroup.add(attack)
#vars health
horn_legs = 100
horn_wings = 100
horn_right = 100
horn_left = 100
horn_tail = 100
horn_heada = 130
horn_headb = 150
horn_headc = 130
horn_health = horn_legs + horn_wings + horn_right + horn_left + horn_tail + horn_heada + horn_headb + horn_headc
horntail_health = HealthBarHorn(70,5,horn_health,910)

enemy_group = pygame.sprite.Group()
enemy2_group = pygame.sprite.Group()
enemy3_group = pygame.sprite.Group()
enemy4_group = pygame.sprite.Group()
enemy5_group = pygame.sprite.Group()
enemy6_group = pygame.sprite.Group()
enemy7_group = pygame.sprite.Group()
enemy8_group = pygame.sprite.Group()
attack_db_group = pygame.sprite.Group()
attack_divide_group = pygame.sprite.Group()
double_a_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
bijudama_group = pygame.sprite.Group()
rasengan_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
r_explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
exit_group_pre = pygame.sprite.Group()
exit_group_el = pygame.sprite.Group()
exit_group_cross = pygame.sprite.Group()
exit_group_fantasy = pygame.sprite.Group()
exit_group_omega = pygame.sprite.Group()
messos_group = pygame.sprite.Group()
tombstone_group = pygame.sprite.Group()
dmg_group = pygame.sprite.Group()
dmg2_group = pygame.sprite.Group()
dragon_roar_group = pygame.sprite.Group()

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
# load in level data and create world
with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)
world = World()
player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
    world_data)

pygame.time.set_timer(pygame.USEREVENT, 10000)
counter = 10
playerlevel = PlayerLevel(70,850)
#shop var
timer = 0
dt = 0.02
pygame.mouse.set_visible(False)

run = True
while run:
    
    clock.tick(FPS)

    if start_game == False:
        # draw menu
        screen.blit(login_img,(0,0))
        # add buttons
        if start_button.draw(screen):
            start_game = True
            start_intro = True
        if exit_button.draw(screen):
            run = False
        Mouse.draw()
    else:
        if stop_music:
            pygame.mixer.music.stop()
        # update background
        if level >= 2 and level <= 4:    
            draw_bg(ludi_img)
        if level >= 5 and level <= 7:
            draw_bg(elnath_img)
        if level >= 8 and level <= 10:
            draw_bg(fantasy_img)
        if level >= 11 and level <= 13:
            draw_bg(omega_img)
        if level == -1:
        
            draw_bg(horntail_img)
            horntail_health.update()
            horntail_health.draw(horn_health)


        if level == 1:
            draw_bg(henesys_img)
            Sign.draw()
            draw_text_border('Fantasy Park',font_sign,BLACK,350,480,WHITE)
            draw_text_border('Lv.10',font_sign,BLACK,380,500,WHITE)
            draw_text_border('Omega Sector',font_sign,BLACK,887,480,WHITE)
            draw_text_border('Lv.25',font_sign,BLACK,917,500,WHITE)
            draw_text_border('El Nath',font_sign,BLACK,360,675,WHITE)
            draw_text_border('Ludibrium',font_sign,BLACK,893,675,WHITE)
            draw_text_border('Lv.20',font_sign,BLACK,923,695,WHITE)
        if level == 0:
            draw_bg(henesys_img)
            SignBoss.draw()
            draw_text_border('Boss - Horntail',font_sign,BLACK,145,745,WHITE)
            draw_text_border('Lv.25',font_sign,BLACK,180,765,WHITE)
            draw_text_border('Welcome to My MapleStory',font_header,BLACK,150,150,WHITE)
            draw_text_border('basic keys:',font_tutorial,BLACK,150,190,WHITE)
            draw_text_border('arrows - up , down , left , right',font_tutorial,BLACK,150,210,WHITE)
            draw_text_border('alt - jump , double alt - double jump',font_tutorial,BLACK,150,230,WHITE)
            draw_text_border('c - skill : throw ilbis (5 mana each) (skill upgrades in lvl 10 and lvl 20):',font_tutorial,BLACK,150,250,WHITE)
            draw_text_border('space - skill : slice & dice (10 mana)',font_tutorial,BLACK,150,270,WHITE)
            draw_text_border('z - pick up',font_tutorial,BLACK,150,290,WHITE)
            draw_text_border('e - close shop (can open shop with double click on cassandra)',font_tutorial,BLACK,150,310,WHITE)
            draw_text_border('s - open and close stat window (you gain stats as you lvl up assign them to get stronger)',font_tutorial,BLACK,150,330,WHITE)
            draw_text_border('x - use hp pot',font_tutorial,BLACK,150,350,WHITE)
            draw_text_border('left shift - use mp pot',font_tutorial,BLACK,150,370,WHITE)
            draw_text_border('d - new skill adele divide attack',font_tutorial,BLACK,150,390,WHITE)
            draw_text_border('for now secret key ctrl - dragon roar GM skill',font_tutorial,BLACK,150,410,WHITE)
        draw_panel()
        # draw world map
        world.draw()
        # show player health
        health_bar.draw(player.health)
        mana_bar.draw(player.mana)
        exp_bar.draw(player.exp)
        playerlevel.draw()
        # show messos
        draw_text(str(player.messos) , font , WHITE,950,862)
        screen.blit(hp_img_big, (750 , 850))
        draw_text(str(player.hp_pots),font,WHITE,750,870)
        screen.blit(mana_img_big, (830 , 850))
        draw_text(str(player.mana_pots),font,WHITE,830,870)
        screen.blit(messos_img, (910 , 860))
        draw_text(f'LV.      {player.lvl}',font,WHITE,30,860)
        draw_text(f'HP {player.health}/{player.max_health}',font,WHITE,200,850)
        draw_text(f'MP {player.mana}/{player.max_mana}',font,WHITE,370,850)
        draw_text(f'EXP {player.exp}/{int(player.max_exp)}',font,WHITE,540,850)
        
        def enemy_active(self):
            self.ai()
            self.update()
            self.draw()
            
        if level == 1:
            shop_npc.update()
            shop_npc.draw()
        for enemy in enemy_group: 
            enemy_active(enemy)
        for enemy in enemy2_group:
            enemy_active(enemy)
        for enemy in enemy3_group:
            enemy_active(enemy)
        for enemy in enemy4_group:
            enemy_active(enemy)
        for enemy in enemy5_group:
            enemy_active(enemy)
        for enemy in enemy6_group:
            enemy_active(enemy)
        for enemy in enemy7_group:
            enemy_active(enemy)
        for enemy in enemy8_group:
            enemy_active(enemy)
        #update boss
        if level == -1:
            
            if horntail.tail_idle and horntail.tail_d == False:
                tail_group.update()
                tail_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.tail_d == False:
                horntail.tail_attack = True
                horntail.tail_idle = False
            if horntail.tail_attack:
                tail_agroup.update()
                tail_agroup.draw(screen)
            elif horntail.tail_d:
                tail_dgroup.update()
                tail_dgroup.draw(screen)
                
            if horntail.wings_idle  and horntail.wings_d == False:
                wings_group.update()
                wings_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.wings_d == False:
                horntail.wings_attack = True
                horntail.wings_idle = False
            if horntail.wings_attack:
                wings_agroup.update()
                wings_agroup.draw(screen)
            elif horntail.wings_d:
                wings_dgroup.update()
                wings_dgroup.draw(screen)

            if horntail.head_aidle and horntail.head_ad == False:
                head_a_group.update()   
                head_a_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.head_ad == False:
                horntail.head_aattack = True
                horntail.head_aidle = False
            if horntail.head_aattack:
                head_aa_group.update()
                head_aa_group.draw(screen)
            elif horntail.head_ad:
                head_adgroup.update()
                head_adgroup.draw(screen)

            if horntail.head_cidle  and horntail.head_cd == False:
                head_c_group.update()
                head_c_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.head_cd == False:
                horntail.head_cattack = True
                horntail.head_cidle = False
            if horntail.head_cattack:
                head_cagroup.update()
                head_cagroup.draw(screen)
            elif horntail.head_cd:
                head_cdgroup.update()
                head_cdgroup.draw(screen)

            if horntail.left_idle and horntail.left_d == False:
                left_group.update()
                left_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.left_d == False:
                horntail.left_attack = True
                horntail.left_idle = False
            if horntail.left_attack:
                left_agroup.update()
                left_agroup.draw(screen)
            elif horntail.left_d:
                left_dgroup.update()
                left_dgroup.draw(screen)

            if horntail.right_idle and horntail.right_d == False:
                right_group.update()
                right_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.right_d == False:
                horntail.right_attack = True
                horntail.right_idle = False
            if horntail.right_attack:
                right_agroup.update()
                right_agroup.draw(screen)
            elif horntail.right_d:
                right_dgroup.update()
                right_dgroup.draw(screen)

            if horntail.legs_d == False:
                legs_group.update()
                legs_group.draw(screen)
            elif horntail.legs_d:
                legs_dgroup.update()
                legs_dgroup.draw(screen)

            if horntail.head_bidle and horntail.head_bd == False:
                head_b_group.update()
                head_b_group.draw(screen)
            if random.randint(0,200) == 1 and horntail.head_bd == False:
                horntail.head_battack = True
                horntail.head_bidle = False
            if horntail.head_battack:
                head_ba_group.update()
                head_ba_group.draw(screen)
            elif horntail.head_bd:
                head_bdgroup.update()
                head_bdgroup.draw(screen)

            if horntail.fire:
                fire_agroup.update()
                fire_agroup.draw(screen)
            if horntail.lightning:    
                light_agroup.update()
                light_agroup.draw(screen)
            if horntail.flame:
                flame_agroup.update()
                flame_agroup.draw(screen)
            if horn_tail <= 0:
                horntail.tail_d = True
            if horn_legs <= 0:
                horntail.legs_d = True
            if horn_wings <= 0:
                horntail.wings_d = True
            if horn_right <= 0:
                horntail.right_d = True
            if horn_left <= 0:
                horntail.left_d = True
            if horn_heada <= 0:
                horntail.head_ad = True
            if horn_headb <= 0:
                horntail.head_bd = True
            if horn_headc <= 0:
                horntail.head_cd = True
            

            head_ar = pygame.Rect(420,250,150,150)
            head_br = pygame.Rect(590,225,120,170)
            head_cr = pygame.Rect(730,250,150,150)
            tail_r = pygame.Rect(815,750,200,70)
            wings_r = pygame.Rect(550,470,200,130)
            legs_r = pygame.Rect(510,630,300,200)
            left_r = pygame.Rect(430,435,100,170)
            right_r = pygame.Rect(764,435,100,170)
    
        # update player actions
        if player.alive:
            # shoot bullets
            if shoot:
                player.shoot()
            if hp_pot and player.hp_pots > 0 and hp_pot_used == False:
                player.hp_pots -= 1
                player.health += 50
                hp_pot_used = True
                if player.health >= player.max_health:
                    player.health = player.max_health
            if mana_pot and player.mana_pots > 0 and mana_pot_used == False:
                player.mana_pots -= 1
                player.mana += 50
                mana_pot_used = True
                if player.mana >= player.max_mana:
                    player.mana = player.max_mana

            if player.in_air:
                player.update_action(2)  # 2: jump
            elif moving_left or moving_right:
                player.update_action(1)  # 1: run
            elif player.attacking:
                player.update_action(4)  # 4: attack
            elif player.hit == True:
                player.update_action(5)   # 5 : hit
                player.animation_cooldown = 10
            elif player.on_rope == False and moving_down:
                player.update_action(8)
            else:
                player.update_action(0)  # 0: idle
            screen_scroll, level_complete ,level_previous , level_elnath,level_cross,level_fantasy,level_omega= player.move(
                moving_left, moving_right) 
            bg_scroll -= screen_scroll
            # check if player has completed the level
            if level_complete:
                player.portal_cooldown = 300
                level_complete = False
                start_intro = True    
                level += 1
                print(level)
                if level == 1:
                    pygame.mixer.music.load('audio/henesys.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1, 0.0, 3000)
                if level == 2:
                    pygame.mixer.music.load('audio/ludi.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_exp = player.max_exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag,shop_npc = world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
            elif level_previous:
                print('prev')
                start_intro = True
                level -= 1
                if level == -1:
                    pygame.mixer.music.load('audio/horntail.ogg')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1, 0.0, 3000)
                if level == 1:
                    pygame.mixer.music.load('audio/henesys.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_exp = player.max_exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health  
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
                    for exit in exit_group:
                        player.rect.x = exit.rect.x
                        player.rect.y = exit.rect.y
                    bg_scroll = 0

            elif level_elnath:
                print('elnath')
                start_intro = True
                level += 4
                pygame.mixer.music.load('audio/elnath.mp3')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_max_exp = player.max_exp
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
                    bg_scroll = 0

            elif level_fantasy:
                print('fantasy')
                start_intro = True
                level += 7
                pygame.mixer.music.load('audio/fantasy.mp3')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_exp = player.max_exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
                    bg_scroll = 0
            
            elif level_omega:
                print('omega')
                start_intro = True
                level += 10
                pygame.mixer.music.load('audio/omega.mp3')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_exp = player.max_exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
                    bg_scroll = 0

            elif level_cross:
                print('cross way')
                start_intro = True
                old_level = level
                level = 1
                pygame.mixer.music.load('audio/henesys.mp3')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1, 0.0, 3000)
                old_messos = player.messos
                old_stat = player.stat
                old_stat_have = player.stat_have
                old_hp = player.health
                old_mana = player.mana
                old_exp = player.exp
                old_max_exp = player.max_exp
                old_max_mana = player.max_mana
                old_max_health = player.max_health
                old_hp_pot = player.hp_pots
                old_mp_pot = player.mana_pots
                old_lvl = player.lvl
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    portal_fx.play()
                    player.messos = old_messos
                    player.health = old_hp
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
                    if old_level == 5 :
                        for exit in exit_group_el:
                            player.rect.x = exit.rect.x
                            player.rect.y = exit.rect.y
                    if old_level == 8 :
                        for exit in exit_group_fantasy:
                            player.rect.x = exit.rect.x
                            player.rect.y = exit.rect.y
                    if old_level == 11 :
                        for exit in exit_group_omega:
                            player.rect.x = exit.rect.x
                            player.rect.y = exit.rect.y
                    bg_scroll = 0     
                    
        else:
            screen_scroll = 0
            if death_fade.fade():
                if restart_button.draw(screen):
                    death_fade.fade_counter = 0
                    start_intro = True
                    level = 1
                    pygame.mixer.music.load('audio/henesys.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1, 0.0, 3000)
                    bg_scroll = 0
                    player.health = 50
                    old_stat = player.stat
                    old_stat_have = player.stat_have
                    old_messos = player.messos
                    old_mana = player.mana
                    old_exp = player.exp
                    old_max_exp = player.max_exp
                    old_max_mana = player.max_mana
                    old_max_health = player.max_health
                    old_hp_pot = player.hp_pots
                    old_mp_pot = player.mana_pots
                    old_lvl = player.lvl
                    world_data = reset_level()
                    player.died = False
                    # load in level data and create world
                    with open(f'./levels/level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, boss, health_bar_boss,  mana_bar , exp_bar,name_tag ,shop_npc= world.process_data(
                        world_data)
                    player.health = 50
                    player.messos = old_messos
                    player.mana = old_mana
                    player.exp = old_exp
                    player.max_exp = old_max_exp
                    player.max_mana = old_max_mana
                    player.max_health = old_max_health
                    player.hp_pots = old_hp_pot
                    player.mana_pots = old_mp_pot
                    player.lvl = old_lvl
                    player.stat = old_stat
                    player.stat_have = old_stat_have
    
        #updates
        ladder_group.update()
        ladder_group.draw(screen)
        #player
        player.update()
        player.draw()
        name_tag.draw('shon')
        attack_db_group.update()
        attack_divide_group.update()
        double_a_group.update()
        bullet_group.update()
        fire_group.update()
        bijudama_group.update()
        rasengan_group.update()
        grenade_group.update()
        explosion_group.update()
        r_explosion_group.update()
        item_box_group.update()
        decoration_group.update()
        water_group.update()
        exit_group.update()
        messos_group.update()
        tombstone_group.update()
        dmg_group.update()
        dmg2_group.update()
        exit_group_pre.update()
        exit_group_el.update()
        exit_group_cross.update()
        exit_group_fantasy.update()
        exit_group_omega.update()
        dragon_roar_group.update()
        attack_db_group.draw(screen)
        attack_divide_group.draw(screen)
        double_a_group.draw(screen)
        bullet_group.draw(screen)
        fire_group.draw(screen)
        bijudama_group.draw(screen)
        rasengan_group.draw(screen)
        grenade_group.draw(screen)
        explosion_group.draw(screen)
        r_explosion_group.draw(screen)
        item_box_group.draw(screen)
        decoration_group.draw(screen)
        water_group.draw(screen)
        exit_group.draw(screen)
        exit_group_pre.draw(screen)
        exit_group_el.draw(screen)
        exit_group_cross.draw(screen)
        exit_group_fantasy.draw(screen)
        exit_group_omega.draw(screen)
        messos_group.draw(screen)
        tombstone_group.draw(screen)
        dmg_group.draw(screen)
        dmg2_group.draw(screen)
        dragon_roar_group.draw(screen)

        #draw shop
        if shop_window:
            ShopWindow.draw()
        if stat_window:
            StatWindow.draw()
        #draw mouse
        Mouse.draw()
        # show intro
        if start_intro == True:
            if intro_fade.fade():
                start_intro = False
                intro_fade.fade_counter = 0
    
    for event in pygame.event.get():
        
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if stat_window:
                    close_tab_fx.play()
                    stat_window = False
                else:
                    stat_window = True
            if event.key == pygame.K_e:
                if shop_window:
                    close_tab_fx.play()
                shop_window = False
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_x:
                hp_pot = True
            if event.key == pygame.K_LSHIFT:
                mana_pot = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                player.attacking = True
            if event.key == pygame.K_d:
                player.attacking_divide = True
            if event.key == pygame.K_c:
                player.shoot()
            if event.key == pygame.K_LCTRL:
                for enemy in enemy_group:    
                    player.attack_big(enemy)
                for enemy in enemy2_group:    
                    player.attack_big(enemy)
                for enemy in enemy3_group:    
                    player.attack_big(enemy)
                for enemy in enemy4_group:    
                    player.attack_big(enemy)
                for enemy in enemy5_group:    
                    player.attack_big(enemy)
                for enemy in enemy6_group:    
                    player.attack_big(enemy)
                for enemy in enemy7_group:    
                    player.attack_big(enemy)
                for enemy in enemy8_group:    
                    player.attack_big(enemy)
                
            if event.key == pygame.K_z:
                pickup = True
            if event.key == pygame.K_LALT and player.alive:
                player.jump = True
                if player.in_air == False:    
                    jump_fx.play()
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.USEREVENT:
            print('resp')
            for enemy in enemy_group:
                enemy_respawn(enemy)
            for enemy in enemy2_group:
                enemy_respawn(enemy)
            for enemy in enemy3_group:
                enemy_respawn(enemy)
            for enemy in enemy4_group:
                enemy_respawn(enemy)
            for enemy in enemy5_group:
                enemy_respawn(enemy)
            for enemy in enemy6_group:
                enemy_respawn(enemy)
            for enemy in enemy7_group:
                enemy_respawn(enemy)
            for enemy in enemy8_group:
                enemy_respawn(enemy)
            
        #mouse attemp
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() # gets the current mouse coords
            rect_npc = pygame.Rect(700,558,100,70)
            hp_shop = pygame.Rect(412,468,30,30)
            mp_shop = pygame.Rect(412,510,30,30)
            stat_add = pygame.Rect(465,465,10,10)

            if rect_npc.collidepoint(pos):
                if event.button == 1:
                    if timer == 0:  # First mouse click.
                        timer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    elif timer < 0.5:
                        print('double click')
                        shop_window = True
                        timer = 0
                    elif timer >= 0.5:
                        print('too late')
                        timer = 0
                        print(timer)
            elif hp_shop.collidepoint(pos):
                if event.button == 1:
                    if timer == 0:  # First mouse click.
                        timer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    elif timer < 0.5:
                        print('double click')
                        if player.messos >= 1000:
                            player.messos -= 1000
                            player.hp_pots += 10
                        timer = 0
                    elif timer >= 0.5:
                        print('too late')
                        timer = 0
            elif mp_shop.collidepoint(pos):
                if event.button == 1:
                    if timer == 0:  # First mouse click.
                        timer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    elif timer < 0.5:
                        print('double click')
                        if player.messos >= 1000:
                            player.messos -= 1000
                            player.mana_pots += 10
                        timer = 0
                    elif timer >= 0.5:
                        print('too late')
                        timer = 0
            elif stat_add.collidepoint(pos):
                if event.button == 1:
                    if player.stat_have > 0:
                        player.stat_have -= 1
                        player.stat += 1
                    
        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
            if event.key == pygame.K_x:
                hp_pot = False
                hp_pot_used = False
            if event.key == pygame.K_LSHIFT:
                mana_pot = False
                mana_pot_used = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                player.attacking = False
            if event.key == pygame.K_d:
                player.attacking_divide = False
            if event.key == pygame.K_z:
                pickup = False
            if event.key == pygame.K_LALT and player.alive:
                player.jump = False
            if event.key == pygame.K_LCTRL:
                player.attacking_big = False
                player.attacking_big_boss = False
    if timer != 0:
        timer += dt
    pygame.display.update()

pygame.quit()
