import plotly.graph_objects as go
import networkx as nx

def draw_graph(G, suspicious_nodes=[], attacked_nodes=[]):

    pos = nx.spring_layout(G)

    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]

        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=1, color='#444')
    )

    node_x = []
    node_y = []
    node_color = []

    for node in G.nodes():
        x, y = pos[node]

        node_x.append(x)
        node_y.append(y)

        if node in attacked_nodes:
            node_color.append("red")
        elif node in suspicious_nodes:
            node_color.append("orange")
        else:
            node_color.append("cyan")

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=list(G.nodes()),
        marker=dict(size=25, color=node_color)
    )

    fig = go.Figure(data=[edge_trace, node_trace])

    fig.update_layout(
        paper_bgcolor="#0a0f1f",
        plot_bgcolor="#0a0f1f",
        font=dict(color="#00ffcc"),
        showlegend=False
    )

    return fig