import pygame, sys, random

def draw_floor():
    win.blit(floor_surface(floor_x_pos, 900))
    win.blit(floor_surface,(floor_x_pos + 576, 900)) # drawing 2 floors.. so that the image moves continuously

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx = -5
    return pipes
    
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            win.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            win.blit(flip_pipe, pipe)

def check_for_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            game_over_sound.play()
            return False
    
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    
    return True

def rotate_the_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1) # rotating the bird
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def display_score(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255)) # here true is value of anti aliasing : true
        score_rect = score_surface.get_rect( center = (288, 100))
        win.blit(score_surface, score_rect)

    if game_state == 'game_oveer':
        score_surface = game_font.render(f'Score: {(int(score)}', True, (255, 255, 255)) # here true is value of anti aliasing : true
        score_rect = score_surface.get_rect( center = (288, 100))
        win.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {(int(high_score)}', True, (255, 255, 255)) # here true is value of anti aliasing : true
        high_score_rect = score_surface.get_rect( center = (288, 850))
        win.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# pre initialising mixer so that there is no delay while plying the sound
# by default, pygame buffers so that sound comes of pure quality
# the values are kept default ecept the buffer which is kept at 512
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512 )
pygame.init()
win = pygame.display.set_mode((576), 1024)) # a window of size 576*1024
clock = pygame.time.Clock()
game_font = pygame.font.font('04B_19.ttf', 40) # setting the font type we want to display which is 04B_19 of size 40

# Game Variables
gravity = 0.25 # the rate at which bid will fall down or fly
bird_movement = 0
game_active = True
scpre = high_score = 0 # setting both score values

bg_surface = pygame.image.load('assets/background-day.jpg').convert() # loading the images
bg_surface = pygame.transform.scale2x(bg_surface) # scaling the images

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# if convert_alpha is not used, then everywhere where image graphics is not shown will be black
bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_time(BIRDFLAP, 200)

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set.timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800] # spawning pipes at this much height

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
game_over_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active: 
                bird_movement = 0
                bird_movement -= 12
                flap_sound.play() # play the sound when space is pressed

            if event.key == pygame.K_SPACE and game_active == False: # when game is over and on pressing space game is restarted
                # on restarting any change to any variable should be reverted
                game_active = True 
                pipe_list.clear() # clearing the list
                bird_rect.center(100, 512)
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        
        if event.type == BIRDFLAP:
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index = 0

			bird_surface,bird_rect = bird_animation()

    win.blit(bg_surface, (0,0))

    if game_active:

        bird_movement += gravity
        rotated_bird = rotate_the_bird(bird_surface)
        bird_rect.centery += bird_movement
        win.blit(rotated_bird, bird_rect)
        game_active = check_for_collision(pipe_list)

        # pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        display_score('main_game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
		win.blit(game_over_surface,game_over_rect)
		high_score = update_score(score,high_score)
		display_score('game_over')

    floor_x_pos = -1
    draw_floor()
    if floor_x_pos <= -576: # moving it to left
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120) # 120 frames