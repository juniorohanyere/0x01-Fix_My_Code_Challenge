#!/usr/bin/python3
"""module to print a square
"""


class Square():
    """prints a square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialise self
        """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """return the perimeter of a square
        """

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """return string representation of the width and height of a square
        """

        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    square = Square(width=12, height=9)
    print(square)
    print(square.area_of_my_square())
    print(square.perimeter_of_my_square())
