class Settings:
    """ 存储外星人中所有的类 """

    def __init__(self):
        """ 游戏初始化设置 """

        # 屏幕设置

        self.screen_width = 1200

        self.screen_height = 800

        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed_factor = 2

        #飞船生命设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 4

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #fleet_direction为1表示右移,-1表示左移
        self.fleet_direction = 1



        pass
