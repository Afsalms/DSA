from abc import abstractstaticmethod, ABCMeta


class Shape(metaclass=ABCMeta):

    @abstractstaticmethod
    def say_shape():
        pass



class Circle(Shape):

    @staticmethod
    def say_shape():
        print("circle")


class Rectangle(Shape):

    @staticmethod
    def say_shape():
        print("Rectangle")



class ShapeFactory():

    @staticmethod
    def get_shape(type_):
        if type_ == "circle":
            return Circle()
        else:
            return Rectangle()



c = ShapeFactory.get_shape("circle")

c.say_shape()


r = ShapeFactory.get_shape("rectangle")

r.say_shape()
