class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.kun_acc = 0.7
        self.kun_friction = -0.12
        self.ball_speed=0.5
        self.ball_maxnum = 7
        self.FPS = 60
        self.BALL_RES = "game/img/ball.png"
        self.PLAYER_RES = (
    'game/img/player/0.png',
    'game/img/player/1.png',
    'game/img/player/2.png',
    'game/img/player/3.png',
    'game/img/player/4.png',
    'game/img/player/5.png',
    'game/img/player/6.png',
)
        self.loseimg = "img/lose.png"
        self.PLAYER_SIZE_W = 96
        self.PLAYER_SIZE_H = 128
        self.SPRITE_SIZE_W = 40
        self.SPRITE_SIZE_H = 40
        self.Punch_snd = "game/snd/punch.WAV"
        self.Ji_snd = "game/snd/ji.WAV"
        self.Jntm_snd = "game/snd/jntm.WAV"
        self.niganma_snd = "game/snd/niganma.WAV"
        self.mei_snd = "game/snd/mei.WAV"
        self.ni_snd = "game/snd/ni.WAV"