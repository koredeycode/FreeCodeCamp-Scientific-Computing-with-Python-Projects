class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    string = ""
    for i in range(self.height):
      string += "*" * self.width
      string += "\n"
    return string

  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)
    
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width
    
  def set_height(self, height):
    self.height = height
    self.width = height

  def __str__(self):
    return "Square(side={})".format(self.height)
