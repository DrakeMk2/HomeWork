from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        r1 = Runner('Иван')
        for i in range(10):
            r1.walk()
        self.assertEquals(r1.distance, 50)

    def test_run(self):
        r2 = Runner('Павел')
        for i in range(10):
            r2.run()
        self.assertEquals(r2.distance, 100)

    def test_challenge(self):
        r1 = Runner('Иван')
        r2 = Runner('Павел')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEquals(r1.distance, r2.distance)
