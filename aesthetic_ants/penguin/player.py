from math import degrees

import pyglet.window.key as key
import pyglet.window.mouse as mouse

from .object import PhysicalObject
from .utils import angle_between, loader, keys
from .weapon import Weapon


class Player(PhysicalObject):
    speed = 90

    def __init__(self, x, y):
        player_image = loader.image("penguin.png")

        # Rotate about the center
        player_image.anchor_x = player_image.width // 2
        player_image.anchor_y = player_image.height // 2

        super().__init__(player_image, x=x, y=y)

        self.weapon = Weapon()

    def update(self, dt):
        if keys[key.W]:
            self.y += dt * self.speed
        if keys[key.S]:
            self.y -= dt * self.speed
        if keys[key.A]:
            self.x -= dt * self.speed
        if keys[key.D]:
            self.x += dt * self.speed

    def fire(self):
        for bullet in self.weapon.get_projectiles(self.x, self.y, self.rotation):
            self.space.add(bullet)

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation = degrees(angle_between(self.x, self.y, x, y))

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.fire()
