import numpy as np
from PIL.ImageEnhance import Color
from numpy import ndarray

import constants
from agentsearch.state import State
from agentsearch.action import Action


class WarehouseState(State[Action]):

    def __init__(self, matrix: ndarray, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.matrix = matrix

    def can_move_up(self) -> bool:
        if self.line_forklift == 0:
            return False

        celulaCima = self.matrix[self.line_forklift - 1][self.column_forklift]
        if celulaCima is None or celulaCima == constants.SHELF or celulaCima == constants.PRODUCT:
            return False

        return True

    def can_move_right(self) -> bool:
        if self.column_forklift == self.columns - 1:
            return False
        celulaDireita = self.matrix[self.line_forklift][self.column_forklift + 1]

        if celulaDireita == constants.SHELF or celulaDireita == constants.PRODUCT:
            return False

        return True

    def can_move_down(self) -> bool:
        if self.line_forklift == self.rows - 1:
            return False
        celulaBaixo = self.matrix[self.line_forklift + 1][self.column_forklift]
        if celulaBaixo is None or celulaBaixo == constants.SHELF or celulaBaixo == constants.PRODUCT:
            return False

        return True

    def can_move_left(self) -> bool:
        if self.column_forklift == 0:
            return False
        celulaEsquerda = self.matrix[self.line_forklift][self.column_forklift - 1]
        if celulaEsquerda is None or celulaEsquerda == constants.SHELF or celulaEsquerda == constants.PRODUCT:
            return False
        else:
            return True

    def move_up(self) -> None:
        self.line_forklift = self.line_forklift - 1

    def move_right(self) -> None:
        self.column_forklift = self.column_forklift + 1

    def move_down(self) -> None:
        self.line_forklift = self.line_forklift + 1

    def move_left(self) -> None:
        self.column_forklift = self.column_forklift - 1

    def get_cell_color(self, row: int, column: int) -> Color:
        if self.matrix[row][column] == constants.EXIT:
            return constants.COLOREXIT
        if self.matrix[row][column] == constants.PRODUCT_CATCH:
            return constants.COLORSHELFPRODUCTCATCH

        if self.matrix[row][column] == constants.PRODUCT:
            return constants.COLORSHELFPRODUCT

        switcher = {
            constants.FORKLIFT: constants.COLORFORKLIFT,
            constants.SHELF: constants.COLORSHELF,
            constants.EMPTY: constants.COLOREMPTY
        }
        return switcher.get(self.matrix[row][column], constants.COLOREMPTY)

    def __str__(self):
        matrix_string = str(self.rows) + " " + str(self.columns) + "\n"
        for row in self.matrix:
            for column in row:
                matrix_string += str(column) + " "
            matrix_string += "\n"
        return matrix_string

    def __eq__(self, other):
        if isinstance(other, WarehouseState):
            return self.line_forklift == other.line_forklift and self.column_forklift == other.column_forklift;
        return NotImplemented

    def __hash__(self):
        return hash(self.matrix.tostring())
