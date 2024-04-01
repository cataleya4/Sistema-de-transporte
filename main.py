from graph import Graph, Node
from a_star import a_star
from heuristic import heuristic

# Ejemplo de uso
if __name__ == "__main__":
    graph = Graph()

    # Definición de nodos y conexiones
    node_a = Node("A", (0, 0))
    node_b = Node("B", (1, 2))
    node_c = Node("C", (3, 1))
    node_d = Node("D", (4, 3))
    node_e = Node("E", (2, 4))
    node_f = Node("F", (5, 5))

    graph.add_node(node_a)
    graph.add_node(node_b)
    graph.add_node(node_c)
    graph.add_node(node_d)
    graph.add_node(node_e)
    graph.add_node(node_f)

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 7)
    graph.add_edge("B", "D", 9)
    graph.add_edge("B", "E", 8)
    graph.add_edge("C", "F", 6)
    graph.add_edge("E", "F", 3)

    start_node = "A"
    goal_node = "F"

    path = a_star(graph, start_node, goal_node)
    if path:
        print("La ruta óptima es:", path)
    else:
        print("No se encontró una ruta válida.")

