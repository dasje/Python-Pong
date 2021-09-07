# Implementation of classic arcade game Pong

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

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [-1,-1]
paddle1_pos = 0
paddle1_vel = 0
paddle2_pos = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction == True:
        ball_vel = [0,3]
    elif direction == False:
        ball_vel == [0,-3]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1]-BALL_RADIUS < 0:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1]+BALL_RADIUS > HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle((ball_pos[0], ball_pos[1]), BALL_RADIUS, 2, 'Red', 'Blue')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0 or paddle1_pos >= HEIGHT-PAD_HEIGHT:
        paddle1_vel = 0
    paddle2_pos += paddle2_vel
    if paddle2_pos <= 0 or paddle2_pos >= HEIGHT-PAD_HEIGHT:
        paddle2_vel = 0
    
    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos),(PAD_WIDTH,paddle1_pos),(PAD_WIDTH,paddle1_pos+PAD_HEIGHT),(0,paddle1_pos+PAD_HEIGHT)], 2, 'Green', 'Blue')
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,0),(WIDTH,0),(WIDTH,PAD_HEIGHT),(WIDTH-PAD_WIDTH,PAD_HEIGHT)], 2, 'Green', 'Pink')

    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel += 3
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 3
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 3
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 3
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['up']:
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


# start frame
new_game()
frame.start()
