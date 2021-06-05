def on_a_pressed():
    global bala
    bala = sprites.create_projectile_from_sprite(img("""
            . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c b . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . c 3 . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . 8 8 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Nave,
        0,
        -200)
    sprites.create_projectile_from_sprite(img("""
            . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c d . . . . . . . 
                    . . . . . . . c b . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . c 3 . . . . . . . 
                    . . . . . . . f f . . . . . . . 
                    . . . . . . . 8 8 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Nave,
        0,
        -200).start_effect(effects.trail, 500)
    music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(50)
    Luna.set_position(randint(0, 160), randint(50, 120))
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.warm_radial, 1000)
    info.change_score_by(1)
    music.magic_wand.play()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 500)
    scene.camera_shake(4, 500)
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

asteroide: Sprite = None
projectile: Sprite = None
bala: Sprite = None
Luna: Sprite = None
Nave: Sprite = None
scene.set_background_color(15)
Nave = sprites.create(img("""
        ...........f.............
            ..........444............
            .........44444...........
            .........44444...........
            ........44fff44..........
            ......1.bbf1fbb.1........
            .....111fff1fff111.......
            .....fffff111fffff.......
            .....ffff11111ffff.......
            .....111f15551f111.......
            .....11ff51115f11f.......
            .....111f11111f111.......
            .....111f11111f111.......
            .....111f11511f111.......
            .....111f11111f111.......
            .....111f11111f111.......
            .....111f11111f111.......
            .....111ff111ff111.......
            .....ffff11111ffff.......
            .....11ff11111ff11.......
            .....1ff1111111ff1.......
            .....ff111111111ff.......
            ....ff11111111111ff......
            ...ff1111111111111ff.....
            ..1f111111111111111f1....
            ..1111111bc1cb1111111....
            ..1111111bc1cb1111111....
            ..1111111fd1df1111111....
            ..........1f1............
            .........11f11...........
            .........11f11...........
            .........bbfbb...........
            .........bbfbb...........
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
    """),
    SpriteKind.player)
Nave.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(Nave)
Luna = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
music.power_up.play()
effects.star_field.start_screen_effect()

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . b d b . . . . . b b b b . . 
                    . c b d d b . . . b b d d d b . 
                    . b c c b . . . b c d d d d b . 
                    . . . . . . b b c c b d b b b . 
                    . . . . . b d d b c c b b b c . 
                    . . b b b c d d b b c c c c . . 
                    . b d d d b c b b c . . . . . . 
                    c b d d d d c c c c . b b b . . 
                    c c b b b b c c c . b d d d b . 
                    . c c c b b . . b c b b d d b b 
                    . b b . . . . . b c c b b b b . 
                    b d d b b . . . . . c c c b . . 
                    b b d d b c . . b b b b b b b . 
                    . b c c c b . b d d d b b c b . 
                    . . . . . . b d d d b c c b . . 
                    . . . . . . b b b c c c b . . .
        """),
        Nave,
        randint(10, 30),
        randint(60, 100))
    projectile.lifespan = 500
    if projectile.vx < 0:
        projectile.image.flip_x()
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global asteroide
    asteroide = sprites.create(img("""
            . . . . . . . . . c c 8 . . . . 
                    . . . . . . 8 c c c f 8 c c . . 
                    . . . c c 8 8 f c a f f f c c . 
                    . . c c c f f f c a a f f c c c 
                    8 c c c f f f f c c a a c 8 c c 
                    c c c b f f f 8 a c c a a a c c 
                    c a a b b 8 a b c c c c c c c c 
                    a f c a a b b a c c c c c f f c 
                    a 8 f c a a c c a c a c f f f c 
                    c a 8 a a c c c c a a f f f 8 a 
                    . a c a a c f f a a b 8 f f c a 
                    . . c c b a f f f a b b c c 6 c 
                    . . . c b b a f f 6 6 a b 6 c . 
                    . . . c c b b b 6 6 a c c c c . 
                    . . . . c c a b b c c c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        SpriteKind.enemy)
    asteroide.set_velocity(0, 79)
    asteroide.bottom = scene.screen_height()
    asteroide.y = randint(0, scene.screen_width())
    asteroide.set_flag(SpriteFlag.AUTO_DESTROY, True)
    asteroide.set_position(randint(20, 140), 7)
game.on_update_interval(500, on_update_interval2)
