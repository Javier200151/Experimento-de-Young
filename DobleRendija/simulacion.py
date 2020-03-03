import unittest
import cnyt

class TestStringMethods(unittest.TestCase):

    def test_ExperimentoYoung(self):            
        self.assertEqual(cnyt.expRendijas([1/2,1/2], 4, 2), [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

if __name__ == '__main__':
    unittest.main()
