import codesters
import time
stage = codesters.Environment()
stage.set_background("summer")

#sprite = codesters.Sprite("Alien-2")
#sprite2 = codesters.Sprite('')

#sprite.move_up(100)
# sprite.turn_left(90)
# sprite.wait(2)
#text = sprite.ask("hello: ")
#sprite.say(text)
# print sprite.get_wait_time(), "CHECKER 1"
# sprite.set_speed(4)
#sprite.glide_to(-100,200)
# sprite.wait(3)
# print sprite.get_total_wait_time(), "checker 2"


# sprite.set_size(1)
# sprite.physics_on()
# sprite.jump(10)
#
# sprite.set_x_speed(4)
#
# stage.set_bounce(1)
#
# stage.enable_all_walls()
#
# sprite.set_drag_on()

"""
sprite.pen_down()
sprite.left(50)
sprite.forward(100)
sprite.forward(100)
sprite.flip_horizontal()
sprite.left(20)
sprite.pen_size(8)
sprite.set_color('red')
sprite.fill_color('red')
sprite.fill_on()
sprite.forward(100)
sprite.right(50)
sprite.forward(100)
sprite.pen_size(6)
sprite.set_color('blue')
sprite.fill_off()
sprite.backward(200)
sprite.pen_size(20)
sprite.set_color('green')
sprite.fill_color('magenta')
sprite.fill_on()
sprite.forward(300)
sprite.move_up(50)
sprite.move_left(50)
sprite.wait(4)
sprite.pen_clear()
"""
# sprite.left(50)
# sprite.set_opacity(.5)
# sprite.set_color('green')
# sprite.set_size(0.5)
# sprite.pen_size(4)
# sprite.pen_down()
# sprite.physics_on()
# sprite.set_x_speed(10)
# sprite.jump(8)

# stage.set_bounce(1)
# stage.enable_all_walls()


# sprite.set_height(500)
# sprite.set_width(100)

#sprite.set_top(200)
#sprite.set_opacity(.5)
#sprite.left(50)
# print sprite.get_rotation()
# print sprite.get_top()
# print sprite.get_right()
# print sprite.get_bottom()
# print sprite.get_left()

sprite = codesters.Sprite("Alien-2")

sprite2 = codesters.Sprite("Alien1")

print codesters.Manager.elements


def collision():
    sprite.jump(5)
    # add any other actions...
sprite.event_collision(collision)
sprite2.goto(0,100)
sprite2.collision_on()
sprite.collision_on()
sprite.set_x_speed(-2)
sprite.physics_on()
stage.enable_all_walls()
stage.set_bounce(0.8)



# sprite.set_x_speed(5)
# sprite.physics_on()
# sprite.set_gravity_on()
#sprite.set_size(0.5)
#sprite.forward(200)

#sprite.set_direction(0,0)
#sprite.setwidth(0.5)
#sprite.forward(100)
# sprite.print_corners()
# sprite.glide_to(100,100)
# sprite.print_corners()
# sprite.left(200)
def moveToMouse(event):
    global sprite
    print event.x-250, 250-event.y
stage.event_click(moveToMouse)

#sprite.gravity_on()
#
# sprite2 = codesters.Sprite("")
# sprite2.set_speed(4)
#
# sprite2.glide_to(0,0)
# sprite2.wait(1)
# sprite2.set_direction(10,-10)
# sprite2.forward(200)
# sprite2.glide_to(0,0)
