import base

class COVID(base.BaseInfection):
    pass

class Model(base.BaseModel):
    def get_people_around(self, pos):
        people_around = set()

        for person in self:
            if person.distance(pos) < self.NEIGHBOUR_RANGE:
                people_around.add(person)

        return people_around

    def get_people_between(self, bl, tr):
        people_between = set()

        for person in self:
            if bl.x < person.pos.x < tr.x and bl.y < person.pos.y < tr.y:
                people_between.add(person)

        return people_between

    def infect_random_people(self, infection_type=COVID, p_num=1):
        for _ in range(p_num):
            person = self.get_random_person()
            person.infect_with(infection_type)
            person.finalise_update()

def main():
    m = Model(100,hwidth=20,hheight=20)
    m.infect_random_people()
    m.run(100)

if __name__=="__main__":
    main()
