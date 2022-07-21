"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

    python src/tests.py -v

"""
import unittest
import numpy as np
from minimax import MiniMaxSnake


# class CollisionTests(unittest.TestCase):
#     def test_filter_none(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": 1, "y": 1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, False)

#     def test_filter_body(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {
#                 "id": "snake-508e96ac-94ad-11ea-bb37",
#                 "body": [{"x": 1, "y": 1}],
#                 "head": {"x": 1, "y": 1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_snake(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 1, "y": 1}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": 1, "y": 1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_hazards(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 1, "y": 1}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": 1, "y": 1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_wall_up(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": 1, "y": 11}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_wall_down(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": 1, "y": -1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_wall_left(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                 "head": {"x": -1, "y": 1}, }}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)

#     def test_filter_wall_right(self):
#         # Arrange
#         data = {"board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#                 "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                         "body": [{"x": 0, "y": 0}],
#                         "head": {"x": 11, "y": 1}}}

#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         # Act
#         result = logic._collision_check(data["you"]["head"])

#         # Assert
#         self.assertEqual(result, True)


# class FindMovesTests(unittest.TestCase):
#     def test_find_moves(self):
#         # Arrange
#         move = {"x": 1, "y": 1}
#         logic = MiniMaxSnake()

#         correct = {
#             "up": {"x": 1, "y": 2},
#             "down": {"x": 1, "y": 0},
#             "right": {"x": 2, "y": 1},
#             "left": {"x": 0, "y": 1}
#         }

#         # Act
#         result = logic._find_moves(move)

#         # Assert
#         self.assertEqual(result, correct)


# class MinimaxNoneTests(unittest.TestCase):
#     def test_find_moves_none_depth_0(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                     "head": {"x": 5, "y": 5}}}
#         position = data["you"]["head"]
#         depth = 0
#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         correct = 4

#         # Act
#         result = logic.minimax(
#             position, depth, -np.Infinity, np.Infinity, True)

#         # Assert
#         self.assertEqual(result, correct)
        
#     def test_find_moves_none_depth_1(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                     "head": {"x": 5, "y": 5}, }}
#         position = data["you"]["head"]
#         depth = 1
#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         correct = 4

#         # Act
#         result = logic.minimax(
#             position, depth, -np.Infinity, np.Infinity, True)

#         # Assert
#         self.assertEqual(result, correct)
        
#     def test_find_moves_none_depth_2(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                     "head": {"x": 5, "y": 5}, }}
#         position = data["you"]["head"]
#         depth = 2
#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         correct = 4

#         # Act
#         result = logic.minimax(
#             position, depth, -np.Infinity, np.Infinity, True)

#         # Assert
#         self.assertEqual(result, correct)
        
#     def test_find_moves_none_depth_3(self):
#         # Arrange
#         data = {
#             "board": {
#                 "height": 11,
#                 "width": 11,
#                 "food": [{"x": 0, "y": 0}],
#                 "hazards": [{"x": 0, "y": 0}],
#                 "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
#                             "body": [{"x": 0, "y": 0}],
#                             "head": {"x": 0, "y": 0}}]},
#             "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
#                     "body": [{"x": 0, "y": 0}],
#                     "head": {"x": 5, "y": 5}, }}
#         position = data["you"]["head"]
#         depth = 3
#         logic = MiniMaxSnake()
#         logic._parse_board(data)

#         correct = 4

#         # Act
#         result = logic.minimax(
#             position, depth, -np.Infinity, np.Infinity, True)

#         # Assert
#         self.assertEqual(result, correct)


class MinimaxZeroTests(unittest.TestCase):
    def test_find_moves_up_depth_0(self):
        # Arrange
        data = {
            "board": {
                "height": 11,
                "width": 11,
                "food": [{"x": 0, "y": 0}],
                "hazards": [{"x": 5, "y": 6}],
                "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
                            "body": [{"x": 0, "y": 0}],
                            "head": {"x": 0, "y": 0}}]},
            "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
                    "body": [{"x": 0, "y": 0}],
                    "head": {"x": 5, "y": 5}, }}
        position = data["you"]["head"]
        depth = 0
        logic = MiniMaxSnake()
        logic._parse_board(data)
        moves = logic._find_moves(position)

        correct = {
            "up": 0,
            "down": 4,
            "left": 4,
            "right": 4
        }

        # Act
        moveRanks = {move: logic.minimax(moves[move], depth, -np.Infinity, np.Infinity, True) for move in moves}

        # Assert
        self.assertEqual(moveRanks["up"], correct["up"])
        self.assertEqual(moveRanks["down"], correct["down"])
        self.assertEqual(moveRanks["left"], correct["left"])
        self.assertEqual(moveRanks["right"], correct["right"])
        
    def test_find_moves_down_depth_0(self):
        # Arrange
        data = {
            "board": {
                "height": 11,
                "width": 11,
                "food": [{"x": 0, "y": 0}],
                "hazards": [{"x": 5, "y": 4}],
                "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
                            "body": [{"x": 0, "y": 0}],
                            "head": {"x": 0, "y": 0}}]},
            "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
                    "body": [{"x": 0, "y": 0}],
                    "head": {"x": 5, "y": 5}, }}
        position = data["you"]["head"]
        depth = 0
        logic = MiniMaxSnake()
        logic._parse_board(data)
        moves = logic._find_moves(position)

        correct = {
            "up": 4,
            "down": 0,
            "left": 4,
            "right": 4
        }

        # Act
        moveRanks = {move: logic.minimax(moves[move], depth, -np.Infinity, np.Infinity, True) for move in moves}

        # Assert
        self.assertEqual(moveRanks["up"], correct["up"])
        self.assertEqual(moveRanks["down"], correct["down"])
        self.assertEqual(moveRanks["left"], correct["left"])
        self.assertEqual(moveRanks["right"], correct["right"])
        
    def test_find_moves_left_depth_0(self):
        # Arrange
        data = {
            "board": {
                "height": 11,
                "width": 11,
                "food": [{"x": 0, "y": 0}],
                "hazards": [{"x": 4, "y": 5}],
                "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
                            "body": [{"x": 0, "y": 0}],
                            "head": {"x": 0, "y": 0}}]},
            "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
                    "body": [{"x": 0, "y": 0}],
                    "head": {"x": 5, "y": 5}, }}
        position = data["you"]["head"]
        depth = 0
        logic = MiniMaxSnake()
        logic._parse_board(data)
        moves = logic._find_moves(position)

        correct = {
            "up": 4,
            "down": 4,
            "left": 0,
            "right": 4
        }

        # Act
        moveRanks = {move: logic.minimax(moves[move], depth, -np.Infinity, np.Infinity, True) for move in moves}

        # Assert
        self.assertEqual(moveRanks["up"], correct["up"])
        self.assertEqual(moveRanks["down"], correct["down"])
        self.assertEqual(moveRanks["left"], correct["left"])
        self.assertEqual(moveRanks["right"], correct["right"])
        
    def test_find_moves_right_depth_0(self):
        # Arrange
        data = {
            "board": {
                "height": 11,
                "width": 11,
                "food": [{"x": 0, "y": 0}],
                "hazards": [{"x": 6, "y": 5}],
                "snakes": [{"id": "snake-b67f4906-94ae-11ea-bb37",
                            "body": [{"x": 0, "y": 0}],
                            "head": {"x": 0, "y": 0}}]},
            "you": {"id": "snake-508e96ac-94ad-11ea-bb37",
                    "body": [{"x": 0, "y": 0}],
                    "head": {"x": 5, "y": 5}, }}
        position = data["you"]["head"]
        depth = 0
        logic = MiniMaxSnake()
        logic._parse_board(data)
        moves = logic._find_moves(position)

        correct = {
            "up": 4,
            "down": 4,
            "left": 4,
            "right": 0
        }

        # Act
        moveRanks = {move: logic.minimax(moves[move], depth, -np.Infinity, np.Infinity, True) for move in moves}

        # Assert
        self.assertEqual(moveRanks["up"], correct["up"])
        self.assertEqual(moveRanks["down"], correct["down"])
        self.assertEqual(moveRanks["left"], correct["left"])
        self.assertEqual(moveRanks["right"], correct["right"])
        
if __name__ == "__main__":
    unittest.main()
