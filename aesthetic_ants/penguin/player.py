from math import degrees

import pyglet.window.key as key
import pyglet.window.mouse as mouse

from .constants import CollisionType
from .object import PhysicalObject
from .resources import PLAYER_IMAGE
from .utils import angle_between, keys
from .weapon import Hand, RocketPropelledSnowball, SnowSpread


class Player(PhysicalObject):
    speed = 90
    collision_type = CollisionType.PLAYER

    def __init__(self, x, y):
        super().__init__(PLAYER_IMAGE, x=x, y=y)

        self.weapons = {
            key._1: Hand(),
            key._2: SnowSpread(),
            key._3: RocketPropelledSnowball(),

        }
        self.weapon = self.weapons[key._1]
        self.firing = False

    def update(self, dt):
        if keys[key.W]:
            self.y += dt * self.speed
        if keys[key.S]:
            self.y -= dt * self.speed
        if keys[key.A]:
            self.x -= dt * self.speed
        if keys[key.D]:
            self.x += dt * self.speed

        if self.firing:
            self.fire()

    def fire(self):
        if self.weapon.reloading:
            return

        for bullet in self.weapon.fire(self.x, self.y, self.rotation):
            self.space.add(bullet)

    def unlock_weapons(self, score):
        for weapon in self.weapons.values():
            if score >= weapon.unlock_score:
                weapon.locked = False

    def on_mouse_motion(self, x, y, dx, dy):
        self.rotation = degrees(angle_between(self.x, self.y, x, y))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.rotation = degrees(angle_between(self.x, self.y, x, y))

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.firing = True

    def on_mouse_release(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            self.firing = False

    def on_key_press(self, button, modifiers):
        weapon = self.weapons.get(button)
        if not weapon:
            return

        if weapon.locked:
            return

        self.weapon = weapon
