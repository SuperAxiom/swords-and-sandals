import os
import pygame


# Function for loading image by name
def load_png(name):
    fullname = os.path.join("img", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("hero0/stay_low.png")
        self.hp = 100
        self.power = 10
        self.rect = self.rect.move(200, 200)

    def reinit(self):
        self.image, self.rect = load_png("hero0/stay_low.png")

    def attack(self):
        self.image, self.rect = load_png("hero0/punch.png")
        return self.power

    def receive_damage(self, damage):
        self.image, self.rect = load_png("hero0/damage_stay.png")
        self.hp -= damage


# Main function
def main():
    # Initialise screen
    pygame.display.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Swords And Sandals")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((14, 83, 167))

    # Init hero
    player = Hero()
    player.rect.x = 600

    # Init sprites
    playersprite = pygame.sprite.RenderPlain((player,))

    # Blit
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Get clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        clock.tick(5)
        player.reinit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack()
                if event.key == pygame.K_t:
                    player.receive_damage(30)

        # Game over
        if player.hp <= 0:
            return

        screen.blit(background, player.rect, player.rect)
        playersprite.update()
        playersprite.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
