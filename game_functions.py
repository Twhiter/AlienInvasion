import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    """ 响应按键和鼠标事件 """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 按键按下 """

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 发射子弹
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        #按q退出游戏
        sys.exit()


def check_keyup_events(event, ship):
    """ 按键松开 """

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen( ai_settings, screen, ship,aliens, bullets):
    """ 更新屏幕上的图像，并切换到新屏幕 """

    # 每次更新都会冲绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外新人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子弹位置，并删除已消失的子弹'''
    #更新子弹的位置
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中外星人
    #如果是这样,就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    check_bullet_alien_collisions(aliens,bullets,ai_settings,screen,ship)


def check_bullet_alien_collisions(aliens,bullets,ai_settings,screen,ship):
    if  len(aliens) == 0:
        '''删除子弹并创造新的外星人群'''
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullets(ai_settings,screen,ship,bullets):
    # 创造一颗子弹,如果小于限制的数量,并将其加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen,ship,aliens):
    '''创造外星人群'''
    #创建一个外星人，并计算一行可以容纳多少个外星人
    #外星人的间距为外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings,alien_width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #创建外星人群
    for row_num in  range(number_rows):

        for alien_num in range(number_aliens_x):
            '''创造一个外新人并将其加入其中'''
            create_alien(ai_settings,screen,aliens,alien_num,row_num)


def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_num,row_number):
        #创建一个外星人并把他加入其中
        alien = Alien(ai_settings,screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)


def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可以容纳多少外星人'''
    available_space_y = (ai_settings.screen_height -
                            3 * alien_height - ship_height)
    number_rows = int( available_space_y/( 2 * alien_height ) )
    return number_rows

def check_fleet_edges(ai_settings,aliens):
    '''有外星人达到边缘时采取相应措施'''
    for alien in aliens.sprites():
        if  alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break



def change_fleet_direction(ai_settings,aliens):
    '''将外星人群下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,ship,aliens):
    '''更新外星人群中的外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print('Ship hit!')






