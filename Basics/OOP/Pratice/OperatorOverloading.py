class Vector:
    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y

    def __add__(self, other):
        if isinstance(other, Vector):
            result_x = self.x_position + other.x_position
            result_y = self.y_position + other.y_position
            return Vector(result_x, result_y)
        else:
            return self

    def __str__(self) -> str: return '('+str(self.x_position)+','+str(self.y_position)+")"

vector1 = Vector(1,2)
vector2 = Vector(3,4)
vector3 = vector1 + vector2
print(vector3)