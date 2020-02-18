import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                print("canonicalized_path",canonicalized_path)
                image = pygame.image.load(canonicalized_path)
                
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()


x = 20
y = 20

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('test_images/fish-bowl-small.png'), (x,y))
        #screen.blit(get_image('celtic-small.png'), (20, 20))
        
        pygame.display.flip()
        clock.tick(60)