import math

def heuristic(node, goal):
    x1, y1 = node.position
    x2, y2 = goal.position
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

