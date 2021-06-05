controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    bala = sprites.createProjectileFromSprite(img`
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
        `, Nave, 0, -200)
    sprites.createProjectileFromSprite(img`
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
        `, Nave, 0, -200).startEffect(effects.trail, 500)
    music.pewPew.play()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(50)
    Luna.setPosition(randint(0, 160), randint(50, 120))
    music.baDing.play()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.warmRadial, 1000)
    info.changeScoreBy(1)
    music.magicWand.play()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.disintegrate, 500)
    scene.cameraShake(4, 500)
    music.playTone(277, music.beat(BeatFraction.Whole))
    info.changeLifeBy(-1)
})
let asteroide: Sprite = null
let projectile: Sprite = null
let bala: Sprite = null
let Luna: Sprite = null
let Nave: Sprite = null
scene.setBackgroundColor(15)
Nave = sprites.create(img`
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
    `, SpriteKind.Player)
Nave.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
controller.moveSprite(Nave)
Luna = sprites.create(img`
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
    `, SpriteKind.Food)
music.powerUp.play()
effects.starField.startScreenEffect()
game.onUpdateInterval(1000, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, Nave, randint(10, 30), randint(60, 100))
    projectile.lifespan = 500
    if (projectile.vx < 0) {
        projectile.image.flipX()
    }
})
game.onUpdateInterval(500, function () {
    asteroide = sprites.create(img`
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
        `, SpriteKind.Enemy)
    asteroide.setVelocity(0, 79)
    asteroide.bottom = scene.screenHeight()
    asteroide.y = randint(0, scene.screenWidth())
    asteroide.setFlag(SpriteFlag.AutoDestroy, true)
    asteroide.setPosition(randint(20, 140), 7)
})
