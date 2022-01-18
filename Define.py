from PIL import ImageFont

class Define:
    HANDSHAPE_ROCK_IMG = "./image/janken_gu.png"
    HANDSHAPE_SCISSORS_IMG = "./image/janken_choki.png"
    HANDSHAPE_PAPPERS_IMG = "./image/janken_pa.png"
    HANDSHAPE_ROCK = "グー"
    HANDSHAPE_SCISSOR = "チョキ"
    HANDSHAPE_PAPPER = "パー"
    YOUWIN = "you win"
    YOULOSE = "you lose"
    YOUDRAW = "draw"

    JANKEN_JANWAV = "./audio/janken.wav"
    JANKEN_PONWAV = "./audio/pon.wav"

    FONT = ImageFont.truetype('C:\Windows\Fonts\meiryo.ttc' , 32)
