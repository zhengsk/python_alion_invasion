class Settings():
    """存储游戏的所有设置类"""

    def __init__(self) -> None:
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed = 5
