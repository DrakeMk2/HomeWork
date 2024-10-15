import tests_12_03
import unittest


runner_suite = unittest.TestSuite()
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_03.RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_03.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_suite)

