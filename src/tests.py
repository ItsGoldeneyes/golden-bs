"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python src/tests.py -v

"""
import unittest

import logic


class AvoidNeckTest(unittest.TestCase):
    def test_avoid_neck_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 5}, {"x": 5, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(possible_moves, result_moves)

    def test_avoid_neck_left(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 4, "y": 5}, {"x": 3, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_right(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 6, "y": 5}, {"x": 7, "y": 5}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 6}, {"x": 5, "y": 7}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_neck_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 5}, {"x": 5, "y": 4}, {"x": 5, "y": 3}]
        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._avoid_my_neck(test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_wall_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "height": 11,
            "width": 11,
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._filter_wall_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(expected, result_moves)

    def test_avoid_wall_left(self):
        # Arrange
        test_body = [{"x": 1, "y": 5}, {"x": 2, "y": 5}, {"x": 3, "y": 5}]

        board = {
            "height": 11,
            "width": 11,
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._filter_wall_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_wall_right(self):
        # Arrange
        test_body = [{"x": 10, "y": 5}, {"x": 9, "y": 5}, {"x": 8, "y": 5}]

        board = {
            "height": 11,
            "width": 11,
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._filter_wall_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_wall_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 10}, {"x": 5, "y": 9}, {"x": 5, "y": 8}]

        board = {
            "height": 11,
            "width": 11,
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._filter_wall_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_wall_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 1}, {"x": 5, "y": 2}, {"x": 5, "y": 3}]

        board = {
            "height": 11,
            "width": 11,
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._filter_wall_moves(
            test_body, possible_moves, board)

    #     # Assert
    #     self.assertEqual(len(result_moves), 3)
    #     self.assertEqual(expected, result_moves)

    def test_avoid_self_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}, {"x": 8, "y": 9}]

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._filter_self_moves(
            test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(expected, result_moves)

    def test_avoid_self_left(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}, {"x": 8, "y": 6}, {"x": 4, "y": 6}]

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._filter_self_moves(
            test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_self_right(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}, {"x": 3, "y": 6}, {"x": 6, "y": 6}]

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._filter_self_moves(
            test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_self_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}, {"x": 5, "y": 7}, {"x": 5, "y": 8}]

        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._filter_self_moves(
            test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_self_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}, {"x": 5, "y": 5}, {"x": 5, "y": 8}]

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._filter_self_moves(
            test_body, possible_moves)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

    def test_avoid_enemy_all(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "snakes": [
                {"body": [
                    {"x": 7, "y": 8}
                ]}
            ],
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left", "right"]

        # Act
        result_moves = logic._filter_enemy_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 4)
        self.assertEqual(expected, result_moves)

    def test_avoid_enemy_left(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "snakes": [
                {"body": [
                    {"x": 4, "y": 6}
                ]}
            ],
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "right"]

        # Act
        result_moves = logic._filter_enemy_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)
        
    def test_avoid_enemy_right(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "snakes": [
                {"body": [
                    {"x": 6, "y": 6}
                ]}
            ],
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "down", "left"]

        # Act
        result_moves = logic._filter_enemy_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)
        
    def test_avoid_enemy_up(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "snakes": [
                {"body": [
                    {"x": 5, "y": 7}
                ]}
            ],
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["down", "left", "right"]

        # Act
        result_moves = logic._filter_enemy_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)
        
    def test_avoid_enemy_down(self):
        # Arrange
        test_body = [{"x": 5, "y": 6}]

        board = {
            "snakes": [
                {"body": [
                    {"x": 5, "y": 5}
                ]}
            ],
        }

        possible_moves = ["up", "down", "left", "right"]
        expected = ["up", "left", "right"]

        # Act
        result_moves = logic._filter_enemy_moves(
            test_body, possible_moves, board)

        # Assert
        self.assertEqual(len(result_moves), 3)
        self.assertEqual(expected, result_moves)

if __name__ == "__main__":
    unittest.main()
