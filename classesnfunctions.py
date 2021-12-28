import pygame
import time
import random
import os


class Platform:
    # класс объекта-платформы, при её отсутствии под живым объектом - он будет падать.
    pass


class Wall:
    # класс стена, его задачей является "не пускать" живой объект сквозь себя
    pass


class AnyCharacter:
    def __init__(self, sprite_coords, sprite_way, sprite_size):
        self.object = pygame.Surface(sprite_size)
        self.coords = sprite_coords
        self.image = pygame.transform.scale(load_image(sprite_way), sprite_size)
        self.sprite = pygame.sprite.Sprite()
        all_sprites.add(self.sprite)
        self.sprite.image = self.image
        self.sprite.rect = self.image.get_rect()


class Projectile:
    # класс, отвечающий за пули, камни всякие летающие и прочие штуки
    pass


class Character(AnyCharacter):
    # класс гг
    pass


class Enemy(AnyCharacter):
    # класс любого агрессивно настроенного товарища
    pass


def load_image(name):
    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    return image
