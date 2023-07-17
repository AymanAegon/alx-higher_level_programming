#!/usr/bin/python3
"""
Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class implementation
    """

    def verify_int(self, name, value):
        """
        verify that value is int

        Args:
            name (str): name of the attribute
            value (int): value of the attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def verify_positif(self, name, value):
        """
        verify that value is greater then 0

        Args:
            name (str): name of the attribute
            value (int): value of the attribute
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def verify_positif2(self, name, value):
        """
        verify that value is greater then or equals 0

        Args:
            name (str): name of the attribute
            value (int): value of the attribute
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        creates a rectangle

        Args:
            width (int): width
            height (int): height
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(id)
        self.verify_int("width", width)
        self.verify_positif("width", width)
        self.__width = width
        self.verify_int("height", height)
        self.verify_positif("height", height)
        self.__height = height
        self.verify_int("x", x)
        self.verify_positif2("x", x)
        self.__x = x
        self.verify_int("y", y)
        self.verify_positif2("y", y)
        self.__y = y

    @property
    def width(self):
        """
        gets the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        self.verify_int("width", value)
        self.verify_positif("width", value)
        self.__width = value

    @property
    def height(self):
        """
        gets the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        self.verify_int("height", value)
        self.verify_positif("height", value)
        self.__height = value

    @property
    def x(self):
        """
        gets the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the x
        """
        self.verify_int("x", value)
        self.verify_positif2("x", value)
        self.__x = value

    @property
    def y(self):
        """
        gets the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the y
        """
        self.verify_int("y", value)
        self.verify_positif2("y", value)
        self.__y = value

    def area(self):
        """
        calculates the area value of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def display(self):
        """
        print in stdout the Rectangle instance with the
        character # by taking care of x and y
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.verify_int("width", args[1])
                self.verify_positif("width", args[1])
                self.__width = args[1]
            if len(args) >= 3:
                self.verify_int("height", args[2])
                self.verify_positif("height", args[2])
                self.__height = args[2]
            if len(args) >= 4:
                self.verify_int("x", args[3])
                self.verify_positif2("x", args[3])
                self.__x = args[3]
            if len(args) >= 5:
                self.verify_int("y", args[4])
                self.verify_positif2("y", args[4])
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.verify_int("width", value)
                    self.verify_positif("width", value)
                    self.__width = value
                elif key == "height":
                    self.verify_int("height", value)
                    self.verify_positif("height", value)
                    self.__height = value
                elif key == "x":
                    self.verify_int("x", value)
                    self.verify_positif2("x", value)
                    self.__x = value
                elif key == "y":
                    self.verify_int("y", value)
                    self.verify_positif2("y", value)
                    self.__y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        d = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return d
