import numpy as np
import random

class Vector2D(np.ndarray):
    Xs = ['x','X']
    Ys = ['y','Y']

    def __new__(cls, x=0, y=0):
        return super().__new__(cls, (2,))

    def __init__(self, x=0, y=0):
        self[0] = x
        self[1] = y


    def __abs__(self):
        return (self[0]**2 + self[1]**2)**0.5

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

class Person:
    class Infection:
        pass

    def __init__(self, people, x, y):
        self.pos = Vector2D(x,y)
        self.infected = False
        self.infection = None
        self.people = people

    def distance(self, other):
        return abs(self.pos - other.pos)

    def get_neighbours(self):
        neighbours = []
        for person in self.people:
            if self.distance(person) < 5 and self != person:
                neighbours.append(person)

        return neighbours

    def move(self):
        pass

    def infect(self, other):
        pass

    def update(self):
        self.move()
        if self.infected:
            for person in self.get_neighbours():
                self.infect(person)

class People:
    def __init__(self, person_count):
        self.people = set()
        for person in range(person_count):
            self.people.add(Person(self, random.random()*100, random.random()*100))

    def __iter__(self):
        return iter(self.people)
