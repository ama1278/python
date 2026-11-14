class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        if abs(self) > abs(other):
            return True
        else:
            return False 

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
            

    def __str__(self):
        xstr = f"{self.x:+}i"
        ystr = f"{self.y:+}j"
        if self.x == 0:
            xstr = ""
        if self.y == 0:
            ystr = ""
        return f"{xstr}{ystr}"
class Vector3d(Vector):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z=z
        def __str__(self):
                if self.z==0:
                        return super().__str__()
                elif self.z==1:
                        return super().__str__()+f'k'
                elif self.z==-1:
                        return super().__str__()+f'-k'
                elif self.z<0 or self.z>1:
                        return super().__str__()+f'{self.z}k' 
                
ve3=Vector3d(1,2,3)
print(ve3) 