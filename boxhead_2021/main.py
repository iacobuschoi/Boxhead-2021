import pygame, sys, math, random

from pygame.time import Clock
pygame.init()

###################################################################################################################
###################################< G A M E _ S E T T I N G >#######################################################
###################################################################################################################
display_width, display_height = 1400, 800 # 창 크기 설정(display_width = 가로, display_height = 세로)
display = pygame.display.set_mode((display_width, display_height)) 
clock = pygame.time.Clock() # 시간 설정
fps = 30 #fps 성정












###################################################################################################################
###################################< I M A G E _ L O A D >#######################################################
###################################################################################################################
############################< P L A Y E R _ I M A G E _ L O A D >#######################################################
# player body image
player_body_image = pygame.transform.scale(pygame.image.load('data/player/player_body/player_body_image.png').convert_alpha(), (200,200))
# player feet image
player_walk_images = []
for i in range(8): player_walk_images.append(pygame.transform.scale(pygame.image.load(f'data/player/player_walk/player_walk_{i}.png'), (200, 200)))
player_static_image = pygame.transform.scale(pygame.image.load('data/player/player_static/player_static_image.png'), (200, 200))
# player stun image
# player_stun_image = pygame.image.load('')
# player dead image
# player_dead_image = pygame.image.load('')

############################< W E A P O N _ I M A G E _ L O A D >#######################################################
bullet_image = pygame.image.load('data/bullet/bullet.png').convert_alpha()
shotgun_static_image = pygame.transform.scale(pygame.image.load('data/guns/shotgun/shotgun_static_image/player_shotgun_static.png').convert_alpha(), (200, 200))
shotgun_fire_images = []
for i in range(5): shotgun_fire_images.append(pygame.transform.scale(pygame.image.load(f'data/guns/shotgun/shotgun_fire_image/player_shotgun_{i}.png').convert_alpha(), (200, 200)))
pistol_static_image = pygame.transform.scale(pygame.image.load('data/guns/pistol/pistol_static_image/player_pistol_static.png').convert_alpha(), (200, 200))
pistol_fire_images = []
for i in range(5): pistol_fire_images.append(pygame.transform.scale(pygame.image.load(f'data/guns/pistol/pistol_fire_image/player_pistol_{i}.png').convert_alpha(), (200, 200)))
rocket_static_image = pygame.transform.scale(pygame.image.load('data/guns/rocket/rocket_static_image/player_rocket_static.png').convert_alpha(), (200, 200))
rocket_fire_images = []
for i in range(5): rocket_fire_images.append(pygame.transform.scale(pygame.image.load(f'data/guns/rocket/rocket_fire_image/player_rocket_{i}.png').convert_alpha(), (200, 200)))
mine_static_image = pygame.transform.scale(pygame.image.load('data/guns/mine/mine_static_image/player_mine_static.png').convert_alpha(), (200, 200))

############################< Z O M B I E _ I M A G E _ L O A D >#######################################################
zombie_body_image_list = []
for i in range(5): zombie_body_image_list.append(pygame.transform.scale(pygame.image.load(f'data/zombie/monster_move_{i}.png').convert_alpha(), (400,400)))

############################< M A P _ I M A G E _ L O A D >#######################################################
map_image = pygame.image.load('data/background/map.png').convert_alpha()
map_image = pygame.transform.scale(map_image, (2400, 2400)) #맵 크기 조정

############################< B O X _ I M A G E _ L O A D >#######################################################
box_image = pygame.transform.scale(pygame.image.load('data/box/box_image.png').convert_alpha(), (200, 200))

############################< B O O M _ I M A G E _ L O A D >#######################################################
boom_image_list = []
for i in range(5): boom_image_list.append(pygame.transform.scale(pygame.image.load(f'data/boom/explosion_{i}.png').convert_alpha(), (200, 200)))

############################< B L O O D _ I M A G E _ L O A D >#######################################################
blood_image = pygame.transform.scale(pygame.image.load(f'data/blood/blood_image.png'), (100, 83))
black_blood_image = pygame.transform.scale(pygame.image.load(f'data/blood/black_blood_image.png'),(200, 200))

############################< B L O O D _ I M A G E _ L O A D >#######################################################
drone_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('data/drone/drone_image.png'), (200, 150)), -90)

king_image_list = []
for i in range(5): king_image_list.append(pygame.transform.scale(pygame.image.load(f'data/king/boss_move_{i}.png').convert_alpha(), (350, 350)))












#####################################################################################################################
############################< S O U N D _ L O A D >#######################################################
#####################################################################################################################
# shotgunfiresound = pygame.mixer.Sound()
backgroundsound = pygame.mixer.Sound('data/sound/background.wav')
kingsound = pygame.mixer.Sound('data/sound/king.wav')
pistolsound = pygame.mixer.Sound('data/sound/pistol.wav')
playersound = pygame.mixer.Sound('data/sound/player.wav')
pistolsound = pygame.mixer.Sound('data/sound/pistol.wav')
rocketsound = pygame.mixer.Sound('data/sound/rocket.wav')
shotgunsound = pygame.mixer.Sound('data/sound/shotgun.wav')
zombiesound = pygame.mixer.Sound('data/sound/zombie.wav')
boomsound = pygame.mixer.Sound('data/sound/boom.wav')
boxsound = pygame.mixer.Sound('data/sound/box.wav')

pistolsound.set_volume(0.1)
shotgunsound.set_volume(0.5)
rocketsound.set_volume(0.2)
boxsound.set_volume(0.5)






#####################################################################################################################
############################< F U N C T I O N S >#######################################################
#####################################################################################################################
def IsInMap(x,y): #캐릭터의 이동 가능 영역 체크 함수(1프래임 후의 좌표로 예상되는 값의 x,y좌표를 대입, 이동 가능 여부를 반환(가능시 1, 물가능시 0))
    if x < 300 or 2100<=x:return 0
    elif 300<=x<450 or 1950<=x<2100:
        if 300<=y<2100:return 1
        else: return 0
    elif 450<=x<600 or 1800<=x<1950:
        if 300<=y<450 or 1100<=y<1300 or 1950<=y<2100:return 1
        else: return 0
    elif 600<=x<1000 or 1400<=x<1800:
        if 300<=y<450 or 600<=y<1800 or 1950<=y<2100:return 1
        else: return 0
    elif 1000<=x<1100 or 1300<=x<1400:
        if 300<=y<450 or 600<=y<1000 or 1400<=y<1800 or 1950<=y<2100:return 1
        else: return 0
    elif 1100<=x<1300:
        if 300<=y<1000 or 1400<=y<2100:return 1
        else: return 0


def length(a,b): # 두 오브젝트 사이의 유클리드 거리의 제곱값을 반환한다
    return ((a.x - b.x)**2 + (a.y - b.y)**2)












#####################################################################################################################
###################################< C L A S S _ S E T T I N G >#######################################################
#####################################################################################################################
##############################< B O D Y _ C L A S S _ S E T T I N G >#######################################################
class Body:
    def __init__(self,name, image, hp, speed, x, y):
        #캐릭터 이름 지정
        self.name = name

        #체력, 데미지
        self.hp = hp
        self.damage = 0
        
        #이동 속도
        self.speed = speed
        self.speed = self.speed // fps
        self.x_vel = 0
        self.y_vel = 0
        self.ospeed = self.speed
        
        #이미지 처리
        self.image = image
        self.rect = image.get_rect()
        #충돌저리를 위한 surface처리
        self.mask = pygame.mask.from_surface(self.image)
        self.AnimationCount = 0

        #실제 좌표(캐릭터의 좌측 상단 좌표)
        self.x = x
        self.y = y
        
        #스크린상의 좌표
        self.x_d = 0
        self.y_d = 0 
        self.angle = 0

        #생사 여부
        self.IsAlive = 1

        #스턴처리
        self.IsStun = 0
        self.RealStunTime = 1000 #ms단위
        self.StunTime = int(self.RealStunTime * fps / 1000)

        #움직임 체크
        self.IsMove = 0

    #객체의 모든 연산을 처리하는 함수(반드시 while문에 포함)
    def main(self, display, O_pos):
        self.Hp()
        self.ImageDefine()
        self.xy(O_pos)
        self.Angle()
        self.stun()
        self.move()
        self.DisplayBlit(display)

    #각도 계산
    def Angle(self):
        pass

    #이미지 지정
    def ImageDefine(self):
        pass

    #스크린상의 좌표 연산
    def xy(self, O_pos):
        #O_pos는 절대 좌표로 player의 좌표를 가리킴(스크린상의 center 좌표)
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0]  - self.rect.center[0], display_height//2 + self.y - O_pos[1] - self.rect.center[1]


    #display에 표시
    def DisplayBlit(self,display):
        display.blit(self.image, (self.x_d, self.y_d))

    #체력 계산(사망처리 포함)
    def Hp(self):
        #매 프래임당 누적된 데미지를 hp에서 빼줌(순서상 모든 충돌처리 뒤에 와야함)
        self.hp -= self.damage
        self.damage = 0
        if self.hp <= 0:
            self.IsAlive = 0

    #스턴 처리
    def stun(self):
        if 0 < self.IsStun < self.StunTime:
            self.IsStun += 1
            self.x += self.x_vel
            self.y += self.y_vel
        elif self.IsStun >= self.StunTime:
            self.IsStun = 0
    
    #움직임 처리
    def move(self):
        if not self.IsStun:
            if self.IsMove:
                self.x += self.x_vel
                self.y += self.y_vel

##############################< P L A Y E R _ C L A S S _ S E T T I N G >#######################################################
class Player(Body):
    def __init__(self, PlayerName, guns):
        super().__init__(PlayerName, image = player_body_image, hp = 3000000, speed = 300, x = 1200, y = 1500)
        self.path_index = 0
        self.path = []
        self.fulhp = self.hp
        self.feet_image = player_static_image
        self.guns = guns
        self.gun_number = 0
        self.gun = self.guns[self.gun_number]
        self.animationtime = fps // 15
    
        #객체의 모든 연산을 처리하는 함수(반드시 while문에 포함)
    
    def main(self, display, O_pos):
        if self.IsAlive:
            self.mask = pygame.mask.from_surface(self.image)
            self.gun.mask = pygame.mask.from_surface(self.gun.image)
            self.gun.rect = self.gun.image.get_rect()
            self.gun = self.guns[self.gun_number]
            self.Hp()
            self.ImageDefine()
            self.xy(O_pos)
            self.Angle()
            self.stun()
            self.move()
            self.DisplayBlit(display)
        else:

            display.blit(self.image, (display_width/2 - self.rect.center[0], display_height/2 - self.rect.center[1]))

    def DisplayBlit(self, display):
        if self.IsAlive:
            if not self.IsStun:
                display.blit(self.feet_image, (self.x_d, self.y_d))
                display.blit(self.gun.image, (self.x_d, self.y_d))
                display.blit(self.image, (self.x_d, self.y_d))
            else:
                display.blit(self.image, (self.x_d, self.y_d))
        else: display.blit(self.image, (self.x_d, self.y_d))
    # 정지, 이동, 스턴, 사망시 플래이어의 이미지를 지정하는 함수
    def ImageDefine(self):
        if self.IsStun:
            self.feet_image = player_static_image
            self.image = player_stun_image
        elif self.IsMove:
            if self.AnimationCount >= len(player_walk_images) * self.animationtime - 1:
                self.AnimationCount = 0
            self.AnimationCount += 1
            img = player_walk_images[self.AnimationCount // self.animationtime]
            self.feet_image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
            img = player_body_image
            self.image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
            self.rect = self.image.get_rect()
        else:
            img = player_static_image
            self.feet_image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
            img = player_body_image
            self.image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
            self.rect = self.image.get_rect()
    #플래이어의 각도를 마우스 포인터가 가르키는 방향으로 지정하는 함수
    def Angle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.angle = math.atan2(display_height/2 - mouse_y, display_width/2 - mouse_x)
    #플래이어의 모든 움직임을 제어하는 함수
    def move(self):
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.path = [[-self.x_vel, -self.y_vel], [self.x_vel, self.y_vel], [self.y_vel, -self.x_vel], [-self.y_vel, self.x_vel]]
        if not self.IsStun:
            if self.IsMove:
                tx = self.x - self.path[self.path_index][0]
                ty = self.y - self.path[self.path_index][1]
                MoveAbleX = IsInMap(tx, self.y)
                MoveAbleY = IsInMap(self.x, ty)
                self.x -= MoveAbleX * self.path[self.path_index][0]
                self.y -= MoveAbleY * self.path[self.path_index][1]
                self.gun.vel = [MoveAbleX * self.path[self.path_index][0], MoveAbleY * self.path[self.path_index][1]]                
                self.IsMove = 0
            else:self.gun.vel = [0,0]

##############################< Z O M B I E _ C L A S S _ S E T T I N G >#######################################################
class Zombie(Body):
    def __init__(self, x, y, zspeed):
        super().__init__(name = 'f', image = zombie_body_image_list[0], hp = 100, speed = zspeed, x = x, y = y)
        self.animationtime = fps // 15
    #객체의 모든 연산을 처리하는 함수(반드시 while문에 포함)
    def main(self, display, O_pos):
        self.Hp()
        self.ImageDefine()
        self.mask = pygame.mask.from_surface(self.image)
        self.Angle(O_pos)
        self.stun()
        self.x_vel =  math.sin(self.angle) * self.speed
        self.y_vel =  - math.cos(self.angle) * self.speed
        self.xy(O_pos)
        self.move()
        self.DisplayBlit(display)

    def Angle(self, O_pos):
        self.angle = math.atan2(O_pos[0] - self.x, self.y - O_pos[1])
    
    def ImageDefine(self):
        if self.AnimationCount >= len(zombie_body_image_list) * self.animationtime - 1:
            self.AnimationCount = 0
        self.AnimationCount += 1
        self.image = zombie_body_image_list[self.AnimationCount // self.animationtime]
        self.rect = self.image.get_rect()

##############################< B L O O D _ C L A S S _ S E T T I N G >#######################################################
class blood:
    def __init__(self, zombie, image):
        self.x = zombie.x
        self.y = zombie.y
        self.image = image
        self.rect = self.image.get_rect()
        self.dx = 0
        self.dy = 0
        self.tum = 3
        self.tum = self.tum * fps
        self.timer = self.tum
        self.IsAlive = 1
    def main(self, O_pos, display):
        self.xy(O_pos)
        display.blit(self.image, (self.x_d - self.rect.center[0], self.y_d - self.rect.center[1]))
    def xy(self, O_pos):
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0], display_height//2 + self.y - O_pos[1]
        self.x_d, self.y_d = int(self.x_d), int(self.y_d)

##############################< M A P _ C L A S S _ S E T T I N G >#######################################################
class Map:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_d = 0
        self.y_d = 0
        self.image = map_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    #객체의 모든 연산을 처리하는 함수(반드시 while문에 포함)
    def main(self, display, O_pos):
        self.xy(O_pos)
        self.DisplayBlit(display)
    #스크린상의 좌표 연산
    def xy(self, O_pos):
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0], display_height//2 + self.y - O_pos[1]
        self.x_d, self.y_d = int(self.x_d), int(self.y_d)
    #display에 표시
    def DisplayBlit(self,display):
        display.blit(self.image, (self.x_d, self.y_d))

##############################< B O X _ C L A S S _ S E T T I N G >#######################################################
class box(Body):
    def __init__(self, xb, yb):
        super().__init__(name = 'box', image = box_image, hp = 100, speed = 0, x = xb, y = yb)
        self.list = ['shotgun', 'rocket', 'mine', 'hp']
        self.blittum = 20 * fps
        self.blittimer = self.blittum
    
    def main(self, display, O_pos):
        self.xy(O_pos)
        self.DisplayBlit(display)

##############################< G U N _ C L A S S _ S E T T I N G >#######################################################
class Gun:
    def __init__(self, image, name, power, bullet_r, bullet_n, bullet_s, bullet_c, bullet_m, alive, x_o, y_o):
        self.x_o = x_o
        self.y_o = y_o
        self.name = name
        self.power = power
        self.bullet_r = bullet_r
        self.bullet_n = bullet_n
        self.bullet_s = bullet_s / fps
        self.bullet_c = bullet_c * fps
        self.bullet_m = bullet_m
        self.fullbulletnum = bullet_m
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 0
        self.y = 0
        self.x_d = 0
        self.y_d = 0
        self.angle = 0
        self.AnimationCount = 0
        self.animationtime = fps//15
        self.IsFire = 0
        self.IsAlive = 0
        self.vel = []
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.alive = alive
        if self.name == 'mine': self.BulletImage = pygame.transform.scale(mine_static_image, (400, 400))
        else:
            self.BulletImage = pygame.transform.scale(bullet_image, (self.bullet_r * 2, self.bullet_r * 2))

    def main(self, O_pos):
        self.ImageDefine()
        self.xy(O_pos)

    def xy(self, O_pos):
        self.x, self.y = O_pos[0], O_pos[1]
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0]  - self.rect.center[0], display_height//2 + self.y - O_pos[1] - self.rect.center[1]

    def ImageDefine(self):
        if self.name == 'shotgun':
            if self.IsFire:
                if self.AnimationCount >= len(shotgun_fire_images) * self.animationtime - 1:
                    self.AnimationCount = 0
                self.AnimationCount += 1
                img = shotgun_fire_images[self.AnimationCount // self.animationtime]
                self.image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
                self.rect = self.image.get_rect()
            elif self.IsAlive:
                img = shotgun_static_image
                self.image = pygame.transform.rotate(img, -self.angle/math.pi*180+90)
                self. rect = self.image.get_rect()
        elif self.name == 'pistol':
            if self.IsFire:
                if self.AnimationCount >= len(pistol_fire_images) * self.animationtime - 1:
                    self.AnimationCount = 0
                img = pistol_fire_images[self.AnimationCount // self.animationtime]
                self.AnimationCount += 1
                self.image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
                self.rect = self.image.get_rect()
            elif self.IsAlive:
                img = pistol_static_image
                self.image = pygame.transform.rotate(img, -self.angle/math.pi*180+90)
                self. rect = self.image.get_rect()
        elif self.name == 'rocket':
            if self.IsFire:
                if self.AnimationCount >= len(rocket_fire_images) * self.animationtime - 1:
                    self.AnimationCount = 0
                img = rocket_fire_images[self.AnimationCount // self.animationtime]
                self.AnimationCount += 1
                self.image = pygame.transform.rotate(img, -self.angle / math.pi * 180 + 90)
                self.rect = self.image.get_rect()
            elif self.IsAlive:
                img = rocket_static_image
                self.image = pygame.transform.rotate(img, -self.angle/math.pi*180+90)
                self.rect = self.image.get_rect()
        elif self.name == 'mine':
            if self.IsAlive:
                img = mine_static_image
                self.image = pygame.transform.rotate(img, -self.angle/math.pi*180+90)
                self.rect = self.image.get_rect()

##############################< B U L L E T _ C L A S S _ S E T T I N G >#######################################################
class Bullet:
    def __init__(self, x, y, gun, angle, alive):
        self.gun = gun
        self.x_o = gun.x_o
        self.y_o = gun.y_o
        self.x_d = 0
        self.y_d = 0
        self.power = gun.power #공격력
        self.bullet_r = gun.bullet_r #총알 크기
        self.bullet_n = gun.bullet_n #총알 개수
        self.bullet_s = gun.bullet_s #속도
        self.bullet_c = gun.bullet_c #재장전 시간
        self.bullet_m = gun.bullet_m #총알 개수
        self.image = gun.BulletImage
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.angle = gun.angle
        self.angle = gun.angle - math.pi / 2 
        self.x = x + self.x_o * math.cos(self.angle) + self.y_o * math.sin(self.angle)
        self.y = y + self.x_o * math.sin(self.angle) - self.y_o * math.cos(self.angle)
        self.x_vel = math.cos(angle) * self.bullet_s #+ gun.vel[0]
        self.y_vel = math.sin(angle) * self.bullet_s #+ gun.vel[1]
        self.ox = self.x
        self.oy = self.y
        self.d = 0
        self.alive = alive
        self.lastcolision = None
    
    def main(self, display, O_pos):
        self.d = (self.x - self.ox)**2 + (self.y - self. oy) ** 2
        self.xy(O_pos)
        display.blit(self.image, (self.x_d - self.rect.center[0], self.y_d - self.rect.center[1]))
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
    def xy(self, O_pos):
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0], display_height//2 + self.y - O_pos[1]

##############################< B O O M _ C L A S S _ S E T T I N G >#######################################################
class boom:
    def __init__(self, bullet):
        self.bullet = bullet
        self.x = bullet.x
        self.y = bullet.y
        self.image = boom_image_list[0]
        self.IsAlive = 1
        self.x_d = 0
        self.y_d = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.AnimationCount = 0
        self.animationtime = fps // 15
        if bullet.gun.name == 'mine': self.size = 200
        else: self.size = 300
    
    def main(self, O_pos, display):
        self.xy(O_pos)
        self.ImangeDefine()
        display.blit(self.image, (self.x_d - self.rect.center[0], self.y_d - self.rect.center[1]))
    
    def xy(self, O_pos):
        self.x_d, self.y_d = display_width//2 + self.x - O_pos[0], display_height//2 + self.y - O_pos[1]

    def ImangeDefine(self):
        if self.AnimationCount >= len(boom_image_list) * self.animationtime - 1:
            self.AnimationCount = 0
            self.IsAlive = 0
        img = boom_image_list[self.AnimationCount // self.animationtime]
        self.AnimationCount += 1
        self.image = pygame.transform.scale(img, (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

##############################< D R O N E B O O M _ C L A S S _ S E T T I N G >#######################################################
class droneboom(boom):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.image = boom_image_list[0]
        self.IsAlive = 1
        self.x_d = 0
        self.y_d = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.AnimationCount = 0
        self.animationtime = fps // 15
        self.size = size

##############################< D R O N E _ C L A S S _ S E T T I N G >#######################################################
class drone(Body):
    def __init__(self, yb, player):
        super().__init__(name = 'drone', image = drone_image, hp = 100, speed = 900, x = random.randrange(200), y = yb)
        self.xo = player.x
        self.animationtime = fps // 15
        self.x_vel = self.speed
        self.boommaketum = 0.1 * fps
        self.boommaketimer = self.boommaketum
        self.boomlist = []
        self.IsMove = 1
    def main(self, display, O_pos, booms):
        self.boommaketimer -= 1
        if self.boommaketimer < 0: self.boommaketimer = self.boommaketum
        self.ImageDefine()
        self.xy(O_pos)
        self.move()
        self.IsInMapDrone()
        self.boommake(booms)
        self.DisplayBlit(display)
    def Angle(self):
        self.angle == 0
    def ImageDefine(self):
        '''
        if self.AnimationCount >= len(drone_image_list) * self.animationtime - 1:
            self.AnimationCount = 0
        self.image = drone_image_list[self.AnimationCount // self.animationtime]
        self.AnimationCount += 1'''
        self.image = drone_image
        self.rect = self.image.get_rect()
    def IsInMapDrone(self):
        if (self.x<0 or self.x>2400):
            self.IsAlive = 0
    def boommake(self, booms):
        if self.boommaketimer == 0:
            boomsound.play()
            booms.append(droneboom(self.x - 100, self.y + (-1)**random.randrange(2)*random.randrange(200), 200))

##############################< K I N G _ C L A S S _ S E T T I N G >#######################################################
class king(Zombie):
    def __init__(self):
        super().__init__(x = 1200, y = 1200, zspeed = 100)
        self.firetum = 0.2*fps
        self.fiertimer = self.firetum
        self.BulletSize = 20
        self.image = king_image_list[0]
        self.hp = 3000
        self.animationtime = 120 // fps
    def fire(self, player, balls):
        if length(self, player) < 300 ** 2 and IsInMap(self.x, self.y):
            if player.IsAlive:
                if self.fiertimer > 0: self.fiertimer -= 1
                else:
                    boomsound.play()
                    balls.append(Zombie(self.x, self.y, 800))
                    self.fiertimer = self.firetum
            self.IsMove = 0
    def ImageDefine(self):
        if self.IsMove:
            if self.AnimationCount >= len(king_image_list) * self.animationtime - 1:
                self.AnimationCount = 0
            self.AnimationCount += 1
            img = king_image_list[self.AnimationCount // self.animationtime]
            self.image = pygame.transform.rotate(img, int(- self.angle * 180 / math.pi))
            self.rect = self.image.get_rect()
        else: 
            self.image = pygame.transform.rotate(king_image_list[0], int(- self.angle * 180 / math.pi))
            self.rect = self.image.get_rect()
    def main(self, display, O_pos, player, balls):
        self.fire(player, balls)
        self.Hp()
        self.ImageDefine()
        self.mask = pygame.mask.from_surface(self.image)
        self.Angle(O_pos)
        self.stun()
        self.x_vel =  math.sin(self.angle) * self.speed
        self.y_vel =  - math.cos(self.angle) * self.speed
        self.xy(O_pos)
        self.move()
        self.IsMove = 1
        self.DisplayBlit(display)





def run():
    ########################################################################################################################
    ###################################< O B J E C T  _ S E T T I N G >#######################################################
    ########################################################################################################################
    ###################################< S C O R E _ S E T T I N G >#######################################################
    score = 1000
    bloods = []
    stage = 1
    stageblittime = 4 * fps
    stageblittimer = stageblittime
    stagefont = pygame.font.SysFont('malgungothicsemilight',30)
    stagefontimage = stagefont.render(f'STAGE {stage}', True, (0,0,0))
    ix = 1
    
    
    drones = []
    dronetum = 0
    
    
    selectfonttum = 3*fps
    selectfonttimer = 0
    ci = 1
    ptum = 0
    
    ###################################< W E A P O N _ S E T T I N G >#######################################################
    #무기 오브젝트 생성
    shotgun = Gun(shotgun_static_image, 'shotgun', 15, 3, 10, 600, 0.1, 800, 5, 12.5, 82.25)#공격력, 총알 반지름, 1회 발사당 총알 개수, 탄속, 재장전 시간, 총알 개수, 관통 횟수, 총구x좌표, 총구y좌표
    pistol = Gun(pistol_static_image, 'pistol', 34, 4, 1, 600, 0.2, 1000000000, 2, 5.5, 65.5)
    rocket = Gun(rocket_static_image, 'rocket', 100, 10, 1, 900, 0.5, 10, 1, 14, 69)
    mine = Gun(mine_static_image, 'mine', 100, 10, 1, 0, 0.5, 15, 1, 0, 0)
    Guns = [pistol, shotgun, rocket, mine]
    reload = 0 # 무기 재장전 타이머
    bullets = [] #총알 오브젝트의 리스트
    booms = []
    

    ###################################< Z O M B I E _ S E T T I N G >#######################################################
    ZombiePoint = [[1200, 100],[1200, 2300], [100, 1200], [2300, 1200], [100, 100], [100, 2300], [2300, 100], [2300, 2300]] # 좀비 스폰 좌표 list
    zombies = [] #좀비 오브젝트의 리스트
    zombinum = 50 #한 단계동안 스폰되는 좀비의 수
    zombitum = 0.5 #좀비 스폰 시간간격 설정
    zombitum = int(zombitum * fps) #좀비 스폰 시간간격 프래임 계산
    zombitimer = 6 * fps #좀비 출현 시간간격 타이머
    pzombinum = 50 * stage
    zombiespeed = 180 + 30 * (stage - 1)
    kings = []
    kingnum = stage
    kingtum = int(5 * fps)
    kingtimer = zombitimer * 2
    skillstack = 0

    ###################################< B O X _ S E T T I N G >#############################################################
    boxlist = [[],[],[],[]] #보급품 오브젝트의 리스트
    boxposlist = [[375, 375], [375, 2025], [2025, 375], [2025, 2025]] # 보급품 스폰 좌표 리스트
    #보급품 오브젝트 생성
    for i in range(4):
        boxlist[i].append(box(boxposlist[i][0], boxposlist[i][1]))

    ###################################< M A P _ S E T T I N G >#######################################################
    map = Map()

    ###################################< P L A Y E R _ S E T T I N G >#######################################################
    player = Player('d', Guns)
    player.ospeed = (300 + 30 * (stage - 1))/fps
    player.fulhp = 300 + 100 * (stage - 1)
    player.hp = player.fulhp











    ###################################################################################################################
    ###################################< G A M E _ R U N >############################################################
    ###################################################################################################################
    backgroundsound.play(-1)
    while True:
        if not IsInMap(player.x, player.y):
            boomsound.play()
            boomplayer = droneboom(player.x,player.y,300)
            while boomplayer.IsAlive:
                boomplayer.main(O_pos,display)
                clock.tick(fps)
                pygame.display.update()
            player.x = 1200
            player.y = 1500
        
        
        player.speed = player.ospeed *(1.5 - player.hp/player.fulhp/2)
        if kingnum == 0 and len(kings) == 0 and zombinum == 0 and len(zombies) == 0:
            if player.IsAlive:
                stage += 1
                pzombinum = stage * 50
                player.ospeed = (300 + 30 * (stage - 1))/fps
                player.fulhp = 300 + 100 * (stage - 1)
                player.hp = player.fulhp
                zombiespeed = 180 + 30 * (stage - 1)
                zombinum = pzombinum
                kingnum = stage
                zombitimer = 6 * fps
                kingtimer = zombitimer * 2
                for i in range(4):
                    boxlist[i] = [box(boxposlist[i][0], boxposlist[i][1])]
                stageblittimer = stageblittime
        
        
        zombitimer -= 1
        kingtimer -= 1
        display.fill((204, 204, 204))
        O_pos =[player.x, player.y]
        #재장전 시간 처리
        if reload > 0:
            reload -= 1
        
        # Zombie object 생성
        if zombitimer == 0 and zombinum:
            ZombiePointIndex = random.randrange(4)
            zombies.append(Zombie(ZombiePoint[ZombiePointIndex][0], ZombiePoint[ZombiePointIndex][1], zombiespeed))
            zombinum -= 1
            zombitimer = zombitum
        
        if kingtimer == 0 and kingnum:
            kings.append(king())
            kingnum -= 1
            kingtimer = kingtum

        # Zombie - Zombie 충돌 감지
        for i in zombies:
            for j in zombies:
                if i != j:
                    if i.mask.overlap(j.mask, (int(j.x - i.x - j.rect.center[0] + i.rect.center[0]), int(j.y - i.y - j.rect.center[1]+ i.rect.center[1]))):
                        if length(i,player) - length(j,player) > 0:
                            i.IsMove = 0
        
        # king - king 충돌 감지
        for i in kings:
            for j in kings:
                if i != j:
                    if i.mask.overlap(j.mask, (int(j.x - i.x - j.rect.center[0] + i.rect.center[0]), int(j.y - i.y - j.rect.center[1]+ i.rect.center[1]))):
                        if length(i,player) - length(j,player) > 0:
                            i.IsMove = 0
                        else: j.IsMove = 0

        # Player - Zombie 충돌 감지
        for i in zombies:
            if i.mask.overlap(player.mask, (int(player.x -player.rect.center[0] - i.x + i.rect.center[0]), int(player.y -player.rect.center[1] - i.y + i.rect.center[1]))) or i.mask.overlap(player.gun.mask, (int(player.gun.x -player.gun.rect.center[0] - i.x + i.rect.center[0]), int(player.gun.y -player.gun.rect.center[1] - i.y + i.rect.center[1]))):
                player.damage += 15
                i.IsAlive = 0
                bloods.append(blood(i, black_blood_image))
                player.x += i.x_vel * 2
                player.y += i.y_vel * 2
                if player.IsAlive: pygame.mixer.Sound.play(playersound)
                
                if player.IsAlive: score = score - score//10 - 1000*stage

        # Zombie - Bullet 충돌 감지
        for i in zombies:
            for j in bullets:
                if i.mask.overlap(j.mask, (int(j.x - j.rect.center[0] - i.x +i.rect.center[0]), int(j.y - j.rect.center[1] - i.y + i.rect.center[1]))):
                    i.x -= 1.5*i.x_vel
                    i.y -= 1.5*i.y_vel
                    if j.lastcolision != i:
                        i.damage += j.power
                        j.alive -= 1
                        j.lastcolision = i
                        bloods.append(blood(i, blood_image))
        
        # king - bullet 충돌 감지
        for i in kings:
            for j in bullets:
                if i.mask.overlap(j.mask, (int(j.x - j.rect.center[0] - i.x +i.rect.center[0]), int(j.y - j.rect.center[1] - i.y + i.rect.center[1]))):
                    if j.lastcolision != i:
                        i.damage += j.power
                        j.alive -= 1
                        j.lastcolision = i
                        i.x -= i.x_vel*2
                        i.y -= i.y_vel*2
        # Zomboe - boom 충돌 감지
        for i in booms:
            for j in zombies:
                if i.mask.overlap(j.mask, (int(j.x - j.rect.center[0] - i.x +i.rect.center[0]), int(j.y - j.rect.center[1] - i.y + i.rect.center[1]))):
                    j.IsAlive = 0
                    bloods.append(blood(j, blood_image))
        # king - boom
        for i in booms:
            for j in kings:
                if i.mask.overlap(j.mask, (int(j.x - j.rect.center[0] - i.x +i.rect.center[0]), int(j.y - j.rect.center[1] - i.y + i.rect.center[1]))):
                    j.damage += 50
                    bloods.append(blood(j, blood_image))
        
        # box - player 충돌 감지
        for v in boxlist:
            if len(v) == 1:
                i = v[0]
                if i.mask.overlap(player.mask, (int(player.x - player.rect.center[0] - i.x +i.rect.center[0]), int(player.y - player.rect.center[1] - i.y +i.rect.center[1]))):
                    i.IsAlive = 0
                    if (player.hp == player.fulhp) and (len(Guns) == 4) and (Guns[i].bullet_m == Guns[i].fullbulletnum for i in range(1,4)):
                        j = 'nothing'
                    else:
                        while ci:
                            j = i.list[random.randrange(4)]
                            ci = 0
                            if j == 'hp':
                                if player.hp == player.fulhp: ci = 1
                            else:
                                for guni in Guns:
                                    if guni.name == j and guni.fullbulletnum == guni.bullet_m: ci = 1
                        ci = 1
                    selectfont = pygame.font.SysFont('malgungothicsemilight',13)
                    selectimg = selectfont.render(f'picked up {j}',True,(0,0,0))
                    selectfonttimer = selectfonttum
                    p = 0
                    for k in Guns:
                        if j == k.name:
                            k.bullet_m = k.fullbulletnum
                            p = 1
                    if p == 0:
                        if j == 'shotgun':Guns.append(shotgun)
                        elif j == 'rocket':Guns.append(rocket)
                        elif j == 'mine': Guns.append(mine)
                        else: player.hp = player.fulhp
                    v.pop(0)
                    boxsound.play()
                    del i
                    


        # 충돌한 총알 제거 + boom object 생성
        p = 0
        while p < len(bullets):
            i = bullets[p]
            if i.alive:p += 1
            else:
                if i.gun.name == 'mine' or i.gun.name == 'rocket':
                    boomsound.play()
                    booms.append(boom(i))
                bullets.pop(p)
                del i
        
        # blood main 실행
        for i in bloods:
            i.main(O_pos, display)
        

        p = 0
        while p < len(kings):
            i = kings[p]
            i.main(display, O_pos, player, zombies)
            if i.IsMove == 0:i.IsMove = 1
            if i.IsAlive == 0:
                kings.pop(p)
                skillstack += 1
                boomsound.play()
                booms.append(droneboom(i.x, i.y, 400))
                kingsound.play()
                del i
            else: p += 1
        
        # box object main 실행
        for i in boxlist:
            if len(i) == 1: i[0].main(display, O_pos)
        # zombie object main 실행, 사망처리
        p = 0
        while p < len(zombies):
            i = zombies[p]
            i.main(display, O_pos)
            if i.IsMove == 0:i.IsMove = 1
            if i.IsAlive == 0:
                zombies.pop(p)
                del i
                if player.IsAlive: score += 1000 * stage
            else: p += 1
        # map object main 실행
        map.main(display, O_pos)
        # player 무기 지정
        gun = Guns[player.gun_number]
        # 마우스 이벤트 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.gun_number += 1
                    if player.gun_number > len(Guns) - 1:
                        player.gun_number = 0
                        LastGunAngle = player.gun.angle
        
        # 키 이벤트 감지
        keys = pygame.key.get_pressed()
        if player.IsAlive:
            if keys[pygame.K_s]:
                player.IsMove = 1
                player.path_index = 0

            if keys[pygame.K_w]:
                player.IsMove = 1
                player.path_index = 1

            if keys[pygame.K_a]:
                player.IsMove = 2
                player.path_index = 2

            if keys[pygame.K_d]:
                player.IsMove = 2
                player.path_index = 3

            if keys[pygame.K_SPACE]:
                if not reload:
                    if gun.bullet_m > 0:
                        if gun.name == 'pistol': pistolsound.play()
                        elif gun.name == 'shotgun': shotgunsound.play()
                        elif gun.name == 'rocket': rocketsound.play()
                        for i in range(gun.bullet_n):
                            bullets.append(Bullet(player.x, player.y, gun, gun.angle + (-1)**random.randrange(2) * math.pi/5/gun.bullet_n*random.randrange(gun.bullet_n), gun.alive))
                            gun.IsFire = 20
                            reload = int(gun.bullet_c)
                            gun.bullet_m -= 1
            # skill
            if keys[pygame.K_f] and skillstack > 0:
                if dronetum == 0:
                    drones.append(drone(player.y, player))
                    drones.append(drone(player.y + 250, player))
                    drones.append(drone(player.y - 250, player))
                    dronetum = 1*fps
                    boomsound.play()
                    booms.append(droneboom(player.x, player.y, 600))
                    skillstack -= 1
            #자폭
            if keys[pygame.K_p]:
                if ptum == 0:
                    #if random.randrange(2):
                    player.hp = 0
                    player.IsAlive = 0
                    boomsound.play()
                    booms.append(droneboom(player.x, player.y, 1000))
                ptum = 1*fps
        
        # skill 쿨타임
        if dronetum > 0: dronetum -= 1
        if ptum > 0: ptum -= 1
        
        # 게임 restart
        else:
            if ix>3*fps:
                if keys[pygame.K_SPACE]: 
                    break
                    main()


        if selectfonttimer > 0: selectfonttimer -= 1
        
        # blood 사망처리
        for i in bloods:
            i.timer -= 1
            if i.timer == 0:
                i.IsAlive = 0
        
        # blood 제거
        p = 0
        while p < len(bloods):
            i = bloods[p]
            if player.IsAlive and i.IsAlive == 0:
                bloods.pop(p)
                del i
            else: p += 1


        if gun.IsFire >0:gun.IsFire -= 1
        gun.angle = player.angle
        gun.IsAlive = player.IsAlive
        gun.main(O_pos)
        j = 0

        # bullet main실행 및 제거, boom 생성
        while j < len(bullets):
            i = bullets[j]
            if not IsInMap(i.x, i.y):
                if i.gun.name == 'mine' or i.gun.name == 'rocket':
                    boomsound.play()
                    booms.append(boom(i))
                del i
                bullets.pop(j)
            else: 
                i.main(display,O_pos)
                j += 1
        
        player.main(display, O_pos)
        
        # boom main 실행
        for i in booms:
            i.main(O_pos, display)
        
        # boom 제거, blood 생성(폭발 흔적)
        p = 0
        while p < len(booms):
            i = booms[p]
            if i.IsAlive == 0:
                booms.pop(p)
                r = i.size
                img = pygame.transform.scale(black_blood_image, (r,r))
                bloods.append(blood(i, img))
                del i
            else: p += 1
        
        # drone main 실행
        for i in drones:
            i.main(display, O_pos, booms)
        
        # drone 제거
        p = 0
        while p < len(drones):
            i = drones[p]
            if i.IsAlive == 0:
                drones.pop(p)
                del i
            else: p += 1
        

        player.speed = player.ospeed
        pygame.draw.rect(display, (0,0,0), [267 - 300 + display_width // 2, 217  - 300 + display_height // 2, 66, 16], 0)
        pygame.draw.rect(display, (255, 255, 255), [268 - 300 + display_width // 2, 218  - 300 + display_height // 2, 64, 14], 0)
        pygame.draw.rect(display, (0,0,0), [270 - 300 + display_width // 2, 220 - 300 + display_height // 2, 60 * player.hp / player.fulhp, 10], 0)
        for i in range(skillstack):
            pygame.draw.circle(display, (243, 152, 0), [display_width - 50 * (i + 1), 50], 20, 0)
            pygame.draw.circle(display, (0, 0, 0), [display_width - 50 * (i + 1), 50], 20, 4)
        
        font = pygame.font.SysFont('malgungothicsemilight',13)
        fontimg = font.render(f'{gun.name}',True,(0,0,0))
        stagefontimagetitle = stagefontimage = stagefont.render(f'STAGE {stage}', True, (0,0,0))
        if gun.name == 'pistol': fontimg2 = font.render(f'unlimited' ,True, (0,0,0))
        else: fontimg2 = font.render(f'{gun.bullet_m}/{gun.fullbulletnum}',True, (0,0,0))
        font1 = pygame.font.SysFont('malgungothicsemilight',40)
        fontimage3 = font1.render(f'SCORE {score}', True, (0,0,0))
        display.blit(fontimg, (270 - 300 + display_width // 2, 184 - 300 + display_height // 2))
        display.blit(fontimg2, (270 - 300 + display_width // 2, 197 - 300 + display_height // 2))
        display.blit(fontimage3, (5,0))
        display.blit(stagefontimagetitle, (5, 50))
        if selectfonttimer >0: display.blit(selectimg, (270 - 300 + display_width // 2 , 500 - 300 + display_height // 2))
        if player.IsAlive: score += stage
        
        if stageblittimer >0 and stage > 1:
            stagefontimage = stagefont.render(f'STAGE {stage - 1} CLEAR', True, (0,0,0))
            display.blit(stagefontimage, (600, 500))
            stageblittimer -= 1
        if player.IsAlive == 0:
            if ix >= 3*fps:
                diefont = stagefont.render('PRESS THE SPACE BAR', True, (0,0,0))
                display.blit(diefont, (140, 380))
            elif ix > 0:
                diefont = stagefont.render('YOU DIE', True, (0,0,0))
                display.blit(diefont, (250, 380))
                if ix == 1: 
                    boomsound.play()
                    backgroundsound.fadeout(1000)
            ix += 1
        clock.tick(fps)
        pygame.display.update()
while True: run()
def main():
    pass