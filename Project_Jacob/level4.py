"""Level 4 boss fight"""

import pygame
import os
import time
import random

# ----------------------------------------------------------------
# Character classes
# ----------------------------------------------------------------

class Character:
    COOLDOWN = 30

    def __init__(self, x_pos, y_pos, health=100, step_velocity=5):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos

        # draw character(jacob, monster, boss) and bullets
        self.health = health
        self.max_health = health
        self.character_img = None
        self.bullet_img = None
        self.bullets = []

        # cooldown before shooting another bullets(magic/kbd)
        self.cool_down_counter = 0

        # character velocity (how many pixel to add when move)
        self.step_velocity = step_velocity

    def draw(self, window):
        # where, color, (xposition, yposition, howbig, howbig), (0-filled/2-hollow)
        # pygame.draw.rect(window, (255,0,0), (self.x_pos, self.y_pos, 50,50), 0
        window.blit(self.character_img, (self.x_pos, self.y_pos))
    

    def get_width(self):
        return self.character_img.get_width()
    
    def get_height(self):
        return self.character_img.get_height()

    def check_colision(self, object):
        offset_x = self.x_pos - object.x_pos
        offset_y = self.y_pos - object.y_pos
        return object.mask.overlap(self.mask, (offset_x, offset_y)) != None

    def was_dead(self):
        return self.health <= 0

    def shoot(self, bullet):
        if self.cool_down_counter == 0:
            self.bullets.append(bullet)
            self.cool_down_counter = 1

    def reset_cooldown(self):
        self.cool_down_counter = 0

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def is_cool(self):
        return self.cool_down_counter == 0

class Jacob(Character):
    def __init__(self, x_pos, y_pos, jocob_images, health=100, step_velocity=10):
        super().__init__(x_pos, y_pos, health, step_velocity)
        self.jocob_images =  jocob_images
        self.character_img = self.jocob_images['rest_image']
        self.bullet_img = self.jocob_images['bullet_magic']
        # pixel perfact
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health

    def was_hit(self, object):
        self.health -= 5

class Enemy(Character):
    """Boss minion - the bats
    """    

    def __init__(self, x_pos, y_pos, monster, monster_image, health=100, step_velocity=1):
        super().__init__(x_pos, y_pos, health, step_velocity)
        self.character_img, self.bullet_img = monster_image[monster]
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health
    
    def move(self):
        self.y_pos += self.step_velocity

    def level_up(self):
        self.step_velocity += 5
        
    def was_hit(self, object):
        if isinstance(object, MagicOrb):
            self.health -= 10

class Boss(Character):
    def __init__(self, x_pos, y_pos, boss_images, health=1000, step_velocity=10):
        super().__init__(x_pos, y_pos, health, step_velocity)
        self.boss_images = boss_images
        self.character_img = boss_images['normal_boss']
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health
    
    def move(self, direction):
        if direction == 'right':
            self.x_pos += self.step_velocity
        else:
            self.x_pos -= self.step_velocity

    def level_up(self):
        self.character_img = self.boss_images['angry_boss']
        self.step_velocity += 10

    def was_hit(self, object):
        # hit by kbd: add health
        if isinstance(object, KBD) :
            self.health += 100
        # hit by magic: minus health
        elif isinstance(object, MagicOrb):
            self.health -= 50

# ----------------------------------------------------------------
# Bullets classes
# ----------------------------------------------------------------
class Bullet:
    def __init__(self, x_pos, y_pos, img, velocity, direction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

        self.velocity = velocity
        self.direction = direction
        
    def get_width(self):
        return self.img.get_width()
    
    def get_height(self):
        return self.img.get_height()

    def draw(self, window):
        window.blit(self.img, (self.x_pos, self.y_pos))
    
    def move(self):
        if self.direction == 'down':
            self.y_pos += self.velocity
        else:
            self.y_pos -= self.velocity
    
    def speed_up(self):
        self.velocity += 10

    def off_screen(self, height):
        return not(self.y_pos <= height and self.y_pos >= 0)

    def check_colision(self, object):
        offset_x = self.x_pos - object.x_pos
        offset_y = self.y_pos - object.y_pos
        return self.mask.overlap(object, (offset_x, offset_y)) != None

    def hit(self, object):
        return self.check_colision(object)

class KBD(Bullet):
    def __init__(self, x_pos, y_pos, img, velocity, direction):
        super().__init__(x_pos, y_pos, img, velocity, direction)

class MagicOrb(Bullet):
    def __init__(self, x_pos, y_pos, img, velocity, direction):
        super().__init__(x_pos, y_pos, img, velocity, direction)

class BatBall(Bullet):
    def __init__(self, x_pos, y_pos, img, velocity, direction):
        super().__init__(x_pos, y_pos, img, velocity, direction)

class BossBall(Bullet):
    def __init__(self, x_pos, y_pos, img, velocity, direction):
        super().__init__(x_pos, y_pos, img, velocity, direction)

# ----------------------------------------------------------------
# Level 4 Game
# ----------------------------------------------------------------

class Level4():
    def __init__(self):
        self.CURRENT_DIREC = os.getcwd()
        self.GAME_FOLDER = os.path.dirname(self.CURRENT_DIREC)
        self.IMG_FOLDER = os.path.join(self.GAME_FOLDER, "Project_Jacob")

        # pixel perfect collision / skip the transparent part of the image
        self.WIDTH, self.HEIGHT = 800, 800
        self.FPS = 60
        
        # background
        self.background = pygame.transform.scale(pygame.image.load("page_10bg.png"), (self.WIDTH, self.HEIGHT))

        # monster image
        self.BOSS = pygame.transform.scale(pygame.image.load("level4_boss.png"), (240,170))
        self.BOSS_ANGRY = pygame.transform.scale(pygame.image.load("level4_boss_angry.png"), (240,170))
        self.BOSS_BABY_1 = pygame.transform.scale(pygame.image.load("boss_baby1.png"), (95,45))
        self.BOSS_BABY_2 = pygame.transform.scale(pygame.image.load("boss_baby2.png"), (95,45))

        # jacob side
        self.JACOB_REST = pygame.transform.scale(pygame.image.load("level4__jacob_rest.png"), (100,220))
        self.JACOB_SHOOT = pygame.transform.scale(pygame.image.load("level4__jacob_shoot.png"), (100,220))

        # bullets
        self.BULLET_MAGIC = pygame.transform.scale(pygame.image.load("level4_magic_orb.png"), (20,20))
        self.BULLET_KBD = pygame.transform.scale(pygame.image.load("level4_kbd.png"), (20,20))
        self.BULLET_BOSS = pygame.transform.scale(pygame.image.load("boss_ball.png"), (20,20))
        self.BULLET_ANGRY_BOSS = pygame.transform.scale(pygame.image.load("boss_ball2.png"), (27,27))
        self.BULLET_BABYBOSS = pygame.transform.scale(pygame.image.load("baby_ball.png"), (15,15))
    
        self.JCOB_IMAGES = {
            'rest_image': self.JACOB_REST,
            'shoot_image': self.JACOB_SHOOT,
            'bullet_magic': self.BULLET_MAGIC,
            'bullet_kbd': self.BULLET_KBD
        }
        
        self.MOSTER_IMAGES = {
            'baby_boss1': (self.BOSS_BABY_1, self.BULLET_BABYBOSS),
            'baby_boss2': (self.BOSS_BABY_2, self.BULLET_BABYBOSS)
        }

        self.BOSS_IMAGES = {
            'normal_boss': self.BOSS,
            'angry_boss': self.BOSS_ANGRY
        }

        # max level means boss will gets angry
        self.MAX_LEVEL = 2
        
        self.BOSS_START_HP = 1000
        self.BOSS_MAX_HP = 5000
        self.JACOB_START_HP = 100

        self.BOSS_START_SPEED = 3
        self.BAT_START_SPEED = 1

    def draw_text(self, text, font_size, font_color, x, y):
        font = pygame.font.Font("victor-pixel.ttf", font_size)
        font_surface = font.render(text, True, font_color)
        self.window.blit(font_surface, (x,y))

    def clear_unused_images(self):
        for enemy in self.enemies:
            if enemy.y_pos + enemy.get_height() > self.HEIGHT:
                self.enemies.remove(enemy)

        for bullet in self.jcob_char.bullets:
            if bullet.off_screen(self.HEIGHT):
                self.jcob_char.bullets.remove(bullet)
        
        for bullet in self.boss_char.bullets:
            if bullet.off_screen(self.HEIGHT):
                self.boss_char.bullets.remove(bullet)

    def redraw_window(self):
        # this will draw everything on screen, anything that has to be rendered
        self.window.blit(self.background, (0,0))
        self.draw_text(f"Jacob's Lives: {self.jcob_char.health}", 25, (255, 255, 255), 20, 20)
        self.draw_text(f"Lord Edward's HP: {self.boss_char.health}", 25, (255, 255, 255), 20, 50)
        self.draw_text(f"Your kibi dungo: {self.kbd}", 25, (255, 255, 255), 20, 80)
        
        # draw characters
        for enemy in self.enemies:
            enemy.draw(self.window)
        self.jcob_char.draw(self.window)
        self.boss_char.draw(self.window)
        
        # draw bullets
        for each in self.jcob_char.bullets:
            each.draw(self.window)
        
        for each in self.boss_char.bullets:
            each.draw(self.window)

        pygame.display.update()

    def level_up(self):
        if self.level <= self.MAX_LEVEL:
            self.level += 1

        if self.level == self.MAX_LEVEL:
            self.boss_char.level_up()
            self.generate_enermies()
            for each_bat in self.enemies:
                each_bat.level_up()

    def generate_enermies(self):
        if len(self.enemies) == 0:
            self.enermies_per_level = 5 * self.level
            for i in range(self.enermies_per_level):
                enemy = Enemy(
                    # random starting position
                    random.randrange(50, self.WIDTH-100), 
                    random.randrange(-1500, -100), random.choice(["baby_boss1", "baby_boss2"]), 
                    self.MOSTER_IMAGES,
                    health=1,
                    step_velocity=self.BAT_START_SPEED
                )
                self.enemies.append(enemy)

    def run(self, kbd):
        # start game level 4 - Boss room
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("level IV - boss fight")

        # start with level 1
        self.level = 1
        self.kbd = kbd

        clock = pygame.time.Clock()

        self.lost = False

        # bats list
        self.enemies = []
        self.enermies_per_level = 0

        # create game characters:
        self.jcob_char = Jacob(340, 550, self.JCOB_IMAGES, 
            health=self.JACOB_START_HP, step_velocity = 10
        )
        self.boss_char = Boss(random.randrange(50, self.WIDTH-100), 20, self.BOSS_IMAGES, 
            health=self.BOSS_START_HP, step_velocity = self.BOSS_START_SPEED
        )
        self.boss_current_direction = 'right'
        self.generate_enermies()

        run = True
        while run:
            clock.tick(self.FPS)
            if len(self.jcob_char.bullets) == 0:
                self.jcob_char.reset_cooldown()

            # lost if jcob health == 0
            if self.jcob_char.was_dead():
                return 'die'
            
            if self.boss_char.health >= self.BOSS_MAX_HP:
                return 'secret_ending'

            # win if boss health == 0
            if self.boss_char.was_dead():
                return 'win'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    pass

            # dictionary of all of the keys and tells whether they are pressed or not at a current time
            self.keys = pygame.key.get_pressed()
            
            # -----------------------
            # Player moves
            # -----------------------
            # move (player_vel) pixel to the left and not off screen
            if (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]) and ((self.jcob_char.x_pos - self.jcob_char.step_velocity) > 0): # move left
                self.jcob_char.x_pos -= self.jcob_char.step_velocity

            # move (player_vel) pixel to the right and not off screen
            if (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]) and ((self.jcob_char.x_pos + self.jcob_char.step_velocity) < (self.WIDTH-100)): # move right
                self.jcob_char.x_pos += self.jcob_char.step_velocity

            if (self.keys[pygame.K_UP] or self.keys[pygame.K_w]) and ((self.jcob_char.y_pos - self.jcob_char.step_velocity) > (self.HEIGHT-350)):
                self.jcob_char.y_pos -= self.jcob_char.step_velocity

            if (self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]) and ((self.jcob_char.y_pos + self.jcob_char.step_velocity) < (self.HEIGHT-220)):
                self.jcob_char.y_pos += self.jcob_char.step_velocity

            # Jcob shooting
            # k to shoot magic orb
            if self.keys[pygame.K_h]:
                if self.jcob_char.is_cool():
                    magicOrb = MagicOrb(self.jcob_char.x_pos, self.jcob_char.y_pos, self.BULLET_MAGIC, 10, 'up')
                    self.jcob_char.shoot(magicOrb)

            # j to shoot KBD
            if self.keys[pygame.K_j]:
                if self.kbd > 0 and self.jcob_char.is_cool():
                    kbd_bullet = KBD(self.jcob_char.x_pos, self.jcob_char.y_pos, self.BULLET_KBD, 10, 'up')
                    self.jcob_char.shoot(kbd_bullet)
                    self.kbd -= 1

            # -----------------------
            # boss moves
            # -----------------------
            if self.boss_current_direction == 'right' and ((self.boss_char.x_pos + self.boss_char.step_velocity) > self.WIDTH - 100):
                self.boss_current_direction = 'left'
            elif self.boss_current_direction == 'left' and ((self.boss_char.x_pos - self.boss_char.step_velocity) <= 0):
                self.boss_current_direction = 'right'
            self.boss_char.move(self.boss_current_direction)

            if random.randrange(0, 2*60) == 1:
                bossBall = BossBall(self.boss_char.x_pos + 5 , self.boss_char.y_pos + self.BOSS.get_height() , 
                    self.BULLET_BOSS, 2, 'down'
                )
                self.boss_char.shoot(bossBall)

            # -----------------------
            # bats moves
            # -----------------------
            for enemy in self.enemies:
                enemy.move()
                if enemy.y_pos + enemy.get_height() > self.HEIGHT:
                    # a bat reaches the bottom of the screen -> critical hit on Jacob
                    self.jcob_char.health -= 20
                    self.enemies.remove(enemy)
            
            # -----------------------
            # bullets moves
            # -----------------------
            for bullet in self.jcob_char.bullets:
                bullet.move()
                self.jcob_char.cooldown()

            for bullet in self.boss_char.bullets:
                bullet.move()
                self.boss_char.cooldown()
            
            # -----------------------
            # bullets check collisions
            # -----------------------
            for bullet in self.jcob_char.bullets:
                for enemy in self.enemies:
                    if enemy.check_colision(bullet):
                        enemy.was_hit(bullet)
                        self.jcob_char.bullets.remove(bullet)
                        
                        self.enemies.remove(enemy)
                        self.jcob_char.reset_cooldown()
            for bullet in self.jcob_char.bullets:
                if self.boss_char.check_colision(bullet):
                    self.boss_char.was_hit(bullet)
                    
                    self.jcob_char.bullets.remove(bullet)
                    self.jcob_char.reset_cooldown()
                        

            for bullet in self.boss_char.bullets:
                if self.jcob_char.check_colision(bullet):
                    self.jcob_char.was_hit(bullet)
                    self.boss_char.bullets.remove(bullet)
                    

            # if kill all bats -> level up
            if len(self.enemies) == 0:
                self.level_up()

            self.clear_unused_images()
            self.redraw_window()

if __name__ == "__main__":
    pygame.init()
    level4 = Level4()
    result = level4.run(100)
    print(result)
    pygame.quit()