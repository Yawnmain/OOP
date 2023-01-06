class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def len(self, second):
        return float(((self.x - second.x) ** 2 + (self.y - second.y) ** 2) ** 0.5)


class Triangle:

    def __init__(self, A, B, C):
        self.A = Point(*A)
        self.B = Point(*B)
        self.C = Point(*C)

        self.ab_side = self.A.len(self.B)
        self.ac_side = self.A.len(self.C)
        self.bc_side = self.B.len(self.C)

    def update_area(self):
        p = (self.ab_side + self.ac_side + self.bc_side) / 2
        return abs((p * (p - self.ab_side) * (p - self.ac_side) * (p - self.bc_side)) ** 0.5)

    def __le__(self, second):
        return self.update_area() <= second.update_area()

    def __ge__(self, second):
        return self.update_area() >= second.update_area()

    def __gt__(self, second):
        return self.update_area() > second.update_area()

    def __lt__(self, second):
        return self.update_area() < second.update_area()

    def __eq__(self, second):
        return self.update_area() == second.update_area()

    def __ne__(self, second):
        return self.update_area() != second.update_area()


with open('plist.txt') as file:
    p_arr = file.readlines()[0].split('][')
    p_arr[0] = p_arr[0][1:]
    p_arr[-1] = p_arr[-1][:-1]
    p_arr = [tuple(map(int, p.split(','))) for p in p_arr]

flag = False
N = len(p_arr)

for i in range(N-2):
    for j in range(i+1, N-1):
        for m in range(j+1, N):
            if flag == True:
                obj = Triangle(p_arr[i], p_arr[j], p_arr[m])
                if obj.__gt__(max_area):
                    max_area = obj
                elif obj.__lt__(min_area):
                    min_area = obj
            else:
                buff = Triangle(p_arr[i], p_arr[j], p_arr[m])
                max_area = min_area = buff
                flag = True

print("Максимальная площадь = ", max_area.update_area())
print("Минимальная площадь = ", min_area.update_area())
