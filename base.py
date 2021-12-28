import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

NEIGHBOUR_RANGE = 5

def randrange(hwidth, centre=0):
    return (random.random()*2 - 1)*hwidth + centre

class Vector2D(np.ndarray):
    Xs = ["x", "X"]
    Ys = ["y", "Y"]

    def __new__(cls, x=0, y=0):
        return super().__new__(cls, (2,))

    def __init__(self, x=0, y=0):
        self[0] = x
        self[1] = y

    def __abs__(self):
        return (self[0] ** 2 + self[1] ** 2) ** 0.5

    def __getattr__(self, attr):
        if attr in Vector2D.Xs:
            return self[0]
        elif attr in Vector2D.Ys:
            return self[1]
        else:
            return super().__getattr__(attr)

    def __setattr__(self, attr, value):
        if attr in Vector2D.Xs:
            self[0] = value
        elif attr in Vector2D.Ys:
            self[1] = value
        else:
            super().__setattr__(attr, value)

    def __repr__(self):
        return f"Vector2D ({self[0]},{self[1]})"

    def to_string(self, dp=10):
        return f"({round(self[0],dp)},{round(self[1],dp)})"

class Person:
    class Infection:
        pass

    def __init__(self, people, x, y):
        self.pos = Vector2D(x, y)
        self.infection = None
        self.people = people

    def distance(self, other):
        if isinstance(other, Person):
            return abs(self.pos - other.pos)
        elif isinstance(other, Vector2D):
            return abs(self.pos - other)

    def move(self):
        pass

    def infect(self, other):
        pass

    def update(self):
        self.move()
        if self.infected:
            for person in self.get_neighbours():
                self.infect(person)

    def __repr__(self):
        name = "Person"
        if __name__ != "__main__":
            name = __name__+"."+name

        if self.infection is None:
            return f"<{name} at {self.pos.to_string(3)}>"


class BaseModel:
    def __init__(self, person_count, person_type=Person, hwidth=100, hheight=100, neighbour_range=NEIGHBOUR_RANGE):
        self.NEIGHBOUR_RANGE = neighbour_range

        self.hwidth = hwidth
        self.hheight = hheight

        self.person_type = person_type

        self.people = set()
        for person in range(person_count):
            self.people.add(person_type(self, randrange(hwidth), randrange(hheight)))

        self.init_display()

    def __iter__(self):
        return iter(self.people)

    def get_people_around(self, pos):
        pass

    def get_people_between(self, bl, tr):
        pass

    def init_display(self):
        fig, ax = plt.subplots()

        self.fig = fig
        self.ax = ax

    def get_data(self, gran=NEIGHBOUR_RANGE):
        x = np.arange(-self.hwidth,self.hwidth,gran)
        y = np.arange(-self.hheight,self.hheight,gran)
        Y, X = np.meshgrid(y, x)
        person_count = np.zeros(Y.shape)
        infected_count = np.zeros(Y.shape)

        for person in self:
            px = (person.pos.x+self.hwidth)//gran
            py = (person.pos.y+self.hheight)//gran
            person_count[int(px), int(py)] += 1

            if person.infection is not None:
                infected_count[int(px), int(py)] += 1

        data = infected_count/person_count
        data[(person_count==0)] = 0

        return X, Y, data

    def display(self):
        X, Y, data = self.get_data(gran=self.NEIGHBOUR_RANGE)
        plt.pcolormesh(X, Y, data, shading="auto")
        plt.show()


ORIGIN_VECTOR = Vector2D(x=0, y=0)
