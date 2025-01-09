class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def set_width(self, new):
        self.width = new

    def set_height(self, new):
        self.height = new

    def get_perimeter(self):
        return (self.width*2) + (self.height*2)

    def get_area(self):
        return self.width * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width>50 or self.height>50:
            return 'Too big for picture.'
        picture=(('*' * self.width) +'\n')* self.height
        return picture

    def get_amount_inside(self, other_shape):
        return self.get_area() // other_shape.get_area()

    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(width=side_length, height=side_length)


    def set_side(self, n):
        self.width = n
        self.height = n

    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"

    def set_width(self, new):
        self.width = new
        self.height = new

    def set_height(self, new):
        self.height = new
        self.width = new


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))