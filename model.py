import base


class Model(base.People):
    def get_people_around(self, pos):
        people_around = set()

        for person in self:
            if person.distance(pos) < base.NEIGHBOUR_RANGE:
                people_around.add(person)

        return people_around

    def get_people_between(self, bl, tr):
        people_between = set()

        for person in self:
            if bl.x < person.pos.x < tr.x and bl.y < person.pos.y < tr.y:
                people_between.add(person)

        return people_between
