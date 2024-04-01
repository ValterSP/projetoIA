from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        h = abs(state.line_forklift - self.problem.goal_position.line) + abs(state.column_forklift - self.problem.goal_position.column)
        return h

    def __str__(self):
        return "Distance to position"

