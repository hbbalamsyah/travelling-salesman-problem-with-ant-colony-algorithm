import streamlit as st
import pandas as pd
import numpy as np

from solver.graph import Node, Graph
from solver.aco import ACO
from solver.plotter import MapPlotter


def main():
    n_ants = st.sidebar.slider("Jumlah Semut", 1, 100, 8)
    n_iter = st.sidebar.slider("Iterasi", 1, 200, 50)
    alpha = st.sidebar.slider("alpha", 0., 10., 1.)
    beta = st.sidebar.slider("beta", 0., 10., 1.)
    rho = st.sidebar.slider("rho", 0., 1., 0.1)
    #set_seed = st.sidebar.checkbox("Set seed", value=False)
    #if set_seed:
    #    seed = st.sidebar.slider("Seed", 0, 10, 0)
    #else:
    #    seed = None

    df = pd.read_csv("data/indonesia.csv")
    cities = df["name"]
    longitudes = df["lng"]
    latitudes = df["lat"]

    # Create the graph
    nodes = []
    for i, name in enumerate(cities):
        nodes.append(Node(longitudes[i], latitudes[i], name=name))

    def distance_function_lat_lng(node1, node2):
        earth_radius = 6373.0
        # Transform in radians
        lat1 = np.radians(node1.x)
        lat2 = np.radians(node2.x)
        lng1 = np.radians(node1.y)
        lng2 = np.radians(node2.y)
        delta_lat = lat2 - lat1
        delta_lng = lng2 - lng1
        a = np.sin(delta_lat / 2) ** 2 + np.cos(lat1) * \
            np.cos(lat2) * np.sin(delta_lng / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        return earth_radius * c

    graph = Graph(
        nodes, distance_function=distance_function_lat_lng, seed=True)
    st.title("RUTE ANTAR TITIK")
    plotter = MapPlotter(graph, zoom=8)
    plotter.init_plot()

    # Solve the TSP
    aco = ACO(graph, seed=True)
    path, distance = aco.solve(
        alpha=alpha,
        beta=beta,
        rho=rho,
        n_ants=n_ants,
        n_iterations=n_iter,
        plotter=plotter,
    )


if __name__ == '__main__':
    main()
