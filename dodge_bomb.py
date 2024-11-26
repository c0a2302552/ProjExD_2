import os
import random
import sys

import pygame as pg



WIDTH, HEIGHT = 800, 600
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    # 爆弾の設定
    bb_radius = 10  # 爆弾の半径
    bb_color = (255, 0, 0)  # 赤色
    bb_img = pg.Surface((bb_radius * 2, bb_radius * 2), pg.SRCALPHA)  # 透明部分を持つSurface
    pg.draw.circle(bb_img, bb_color, (bb_radius, bb_radius), bb_radius)  # 爆弾の円を描く
    bb_img.set_colorkey((0, 0, 0))  # 黒を透明にする
    
    # 爆弾の初期位置（ランダム）
    bb_rct = bb_img.get_rect()
    bb_rct.center = random.randint(0, WIDTH ), random.randint(0, HEIGHT)
    
    # 爆弾の速度
    vx, vy = 5, 5

    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        bb_rct.move_ip(vx, vy)
        
        # 画面端で跳ね返るようにする
        if bb_rct.left < 0 or bb_rct.right > WIDTH:
            vx = -vx  # 横方向の速度反転
        if bb_rct.top < 0 or bb_rct.bottom > HEIGHT:
            vy = -vy  # 縦方向の速度反転

        # 爆弾を描画
        screen.blit(bb_img, bb_rct)

        DELTA={
            pg.K_UP:(0, -5),
            pg.K_DOWN:(0, +5),
            pg.K_LEFT:(-5, 0),
            pg.K_RIGHT:(+5, 0),
        }

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]

        
        for key,DELTA in DELTA.items():
            if key_lst[key]:
                sum_mv[0]+=DELTA[0]
                sum_mv[1]+=DELTA[1]
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()   
    sys.exit()
