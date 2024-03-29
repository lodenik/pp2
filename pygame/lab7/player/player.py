import pygame

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((900 , 512)) #size of window
pygame.display.set_caption("Music Player") #the name of display
player = pygame.image.load("player.jpg") #main object

process = True 

color = (255, 0, 0)

playlist = ["song1.mp3", "song2.mp3" , "song3.mp3"] #music

index_of_playlist = 0

def volume_down():
    pygame.mixer.music.set_volume(0.4)

def volume_up():
    pygame.mixer.music.set_volume(0.8)

def play_music():
    pygame.mixer.music.load(playlist[index_of_playlist])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist + 1) % len(playlist)
    play_music()

def previous_track():
    global index_of_playlist
    index_of_playlist = (index_of_playlist - 1) % len(playlist)
    play_music()

while process:
    
    pygame.display.update()
    
    screen.blit(player , (0 , 0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            process = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()

            elif event.key == pygame.K_TAB:
                stop_music()

            elif event.key == pygame.K_RIGHT:
                next_track()

            elif event.key == pygame.K_LEFT:
                previous_track()

            elif event.key == pygame.K_UP:
                volume_up()
                
            elif event.key == pygame.K_DOWN:
                volume_down()

pygame.display.flip()
clock.tick(10)
pygame.quit()