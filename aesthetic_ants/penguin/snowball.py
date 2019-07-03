import pyglet

from .object import PhysicalObject


class Snowball(PhysicalObject):
    image_file = 'snowball.png'

    def __init__(self, x, y, velocity_x, velocity_y, image=None):
        snowball_image = pyglet.resource.image(self.image_file)

        snowball_image.anchor_x = snowball_image.width // 2
        snowball_image.anchor_y = snowball_image.height // 2

        super().__init__(img=snowball_image, x=x, y=y)

        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self, dt):
        self.x += self.velocity_x
        self.y += self.velocity_y
