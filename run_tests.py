import model
import time

def test(person_num=1000, hwidth=100, hheight=100, run_time=100):
    start = time.time()
    print("Initilising model")
    m = model.Model(person_num,hwidth=hwidth,hheight=hheight)

    print("Infecting random person")
    m.infect_random_people(p_num=1)

    print("Running model")
    m.run(run_time, display=False)

    end = time.time()
    return end - start

def small_test():
    return test(400, 50, 50, 100)
