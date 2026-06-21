import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    G = nx.DiGraph()

    # Dependency relationships
    G.add_edges_from([
        ("auth.py", "Login API"),
        ("Login API", "Session Service"),
        ("Session Service", "User Service"),
        ("User Service", "Database"),
        ("middleware.js", "Login API"),
        ("db/schema.sql", "User Service")
    ])

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        node_color="lightblue",
        arrows=True,
        font_size=9
    )

    plt.title("Duo Orbit Architect - Dependency Graph")

    output_file = "dependency_graph.png"
    plt.savefig(output_file)
    plt.close()

    return output_file