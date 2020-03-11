import unittest

from algorithm_dij import Dijkstra

class TestDijkstra(unittest.TestCase):
    """
    Test Dijkstra algorithm on the example done during class
    """
    def test_case1(self):
        adjacency_list = {
            1: [(2,3), (3,1), (7,10)],
            2: [(1,3), (4,3), (6,5), (7,4)],
            3: [(1,1), (4,4), (6,5)],
            4: [(2,3), (3,4), (5,1)],
            5: [(4,1), (6,4), (7,2)],
            6: [(3,5), (2,5), (5,4), (7,3)],
            7: [(2,4), (5,2), (6,3)]
        }
        self.assertListEqual(Dijkstra(adjacency_list, 1, 7), [1, 2, 7])

if __name__ == "__main__":
    unittest.main()