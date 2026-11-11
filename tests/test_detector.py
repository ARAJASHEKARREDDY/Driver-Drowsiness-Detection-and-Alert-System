import unittest
from src.detector import eye_aspect_ratio

class TestEyeAspectRatio(unittest.TestCase):
    def test_open_eye_has_positive_ratio(self):
        points = [(0, 5), (3, 2), (7, 2), (10, 5), (7, 8), (3, 8)]
        self.assertGreater(eye_aspect_ratio(points), 0)

    def test_zero_width_returns_zero(self):
        points = [(1, 1), (2, 2), (2, 2), (1, 1), (2, 2), (2, 2)]
        self.assertEqual(eye_aspect_ratio(points), 0)

    def test_requires_six_points(self):
        with self.assertRaises(ValueError):
            eye_aspect_ratio([(0, 0)] * 5)

if __name__ == "__main__":
    unittest.main()
