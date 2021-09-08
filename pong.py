# simple game of pong, needs to be run with the simplegui library available on codeskulptor.com

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_pos = 0
paddle1_vel = 0
paddle2_pos = 0
paddle2_vel = 0

ws_player = 0
updown_player = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] = -1
    if direction == RIGHT:
        ball_vel[0] = random.randint(1, 3)
    if direction == LEFT:
        ball_vel[0] = -random.randint(1, 3)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global ws_player, updown_player  # these are ints
    ws_player, updown_player = 0, 0
    paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel = 0, 0, 0, 0
    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, ws_player, updown_player, counter

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[1] - BALL_RADIUS < 0:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 2, 'Red', 'Green')

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0 or paddle1_pos >= HEIGHT - PAD_HEIGHT:
        paddle1_vel = 0
    paddle2_pos += paddle2_vel
    if paddle2_pos <= 0 or paddle2_pos >= HEIGHT - PAD_HEIGHT:
        paddle2_vel = 0

    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), (PAD_WIDTH, paddle1_pos), (PAD_WIDTH, paddle1_pos + PAD_HEIGHT),
                         (0, paddle1_pos + PAD_HEIGHT)], 2, 'Green', 'Blue')
    canvas.draw_polygon([(WIDTH - PAD_WIDTH, paddle2_pos), (WIDTH, paddle2_pos), (WIDTH, paddle2_pos + PAD_HEIGHT),
                         (WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT)], 2, 'Green', 'Pink')

    # determine whether paddle and ball collide
    if ball_pos[0] <= 8 + BALL_RADIUS:
        if ball_pos[0] <= 8 + BALL_RADIUS and ball_pos[1] in range(paddle1_pos - 1, paddle1_pos + PAD_HEIGHT + 1):
            ball_vel[0] = -ball_vel[0] + 1
        else:
            updown_player += 1
            ball_vel[0], ball_vel[1] = 0, 0
            spawn_ball(RIGHT)

    if ball_pos[0] + BALL_RADIUS >= WIDTH - 8:
        if ball_pos[0] >= WIDTH - 8 - BALL_RADIUS and ball_pos[1] in range(paddle2_pos - 1,
                                                                           paddle2_pos + PAD_HEIGHT + 1):
            ball_vel[0] = -ball_vel[0] - 1
        else:
            ws_player += 1
            ball_vel[0], ball_vel[1] = 0, 0
            spawn_ball(LEFT)

    # draw scores
    canvas.draw_text(str(ws_player), (WIDTH / 4, HEIGHT / 5), 50, 'Blue')
    canvas.draw_text(str(updown_player), (WIDTH / 4 * 3, HEIGHT / 5), 50, 'Red')


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
start_button = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()