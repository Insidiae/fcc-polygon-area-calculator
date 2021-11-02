class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        res = ""

        for i in range(0, self.height):
            for i in range(0, self.width):
                res += "*"
            res += "\n"

        return res

    def get_amount_inside(self, shape):
        amount = 0

        i = 0
        while i < self.height:
            j = 0
            if i + shape.height <= self.height:
                while j < self.width:
                    if j + shape.width <= self.width:
                        amount += 1
                    j += shape.width
            i += shape.height
            
        return amount


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_height(self, side):
        self.height = side
        self.width = side
        self.side = side
