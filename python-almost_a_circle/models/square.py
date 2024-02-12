#!/usr/bin/python3
"""Square module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string."""
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, attributes[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary method"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
