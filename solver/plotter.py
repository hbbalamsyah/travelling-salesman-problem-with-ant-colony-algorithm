import time

import streamlit as st
import pydeck
import pandas as pd


class MapPlotter:
    def __init__(self, graph, zoom=3.):
        self.graph = graph
        self.zoom = zoom
        self.r = None
        self.layer_pheromones = None
        self.layer_best_path = None
        self.chart = None
        self.text = None
        self.df_distance = None
        self.distance_chart = None

    def init_plot(self):

        # Layer yang menunjukkan nama titik, penempatan titik, dan nama titik
        nodes_name = []
        for node in self.graph.nodes.values():
            nodes_name.append({
                "coordinates": [node.x, node.y],
                "name": node.name,
            })
        layer_nodes = pydeck.Layer(
            "ScatterplotLayer",
            nodes_name,
            coverage=1,
            pickable=True,
            get_position="coordinates",
            radius_min_pixels=8,
            get_color=[0, 232, 85],
        )

        layer_nodes_name = pydeck.Layer(
            "TextLayer",
            nodes_name,
            get_position="coordinates",
            get_text="name",
            get_color=[220, 20, 60],
            get_size=22,
            get_alignment_baseline="'bottom'",
            coverage=1,
            pickable=True,
        )

        # Layer yang menunjukkan jumlah pheromones
        lines_pheromones = self._get_lines_pheromones()
        self.layer_pheromones = pydeck.Layer(
            "LineLayer",
            lines_pheromones,
            get_source_position="start",
            get_target_position="end",
            get_width="value",
            width_scale=1,
            coverage=1,
            pickable=True,
            get_color=[0, 0, 255],
        )

        # Layer yang menunjukkan rute terbaik dengan garis berwarna merah
        self.layer_best_path = pydeck.Layer(
            "LineLayer",
            [],  # empty layer
            get_source_position="start",
            get_target_position="end",
            coverage=1,
            width_scale=3,
            pickable=True,
            get_color=[255, 0, 0],
        )
        initial_view_state = self._get_init_view(lines_pheromones)
        self.r = pydeck.Deck(layers=[layer_nodes, layer_nodes_name, self.layer_pheromones, self.layer_best_path],
                             initial_view_state=initial_view_state, map_style="mapbox://styles/mapbox/streets-v11", tooltip=True, api_keys=None)
        self.chart = st.pydeck_chart(self.r)

        # Empty plot to show the distance convergence
        self.df_distance = pd.DataFrame({"Best distance": []})
        self.distance_chart = st.line_chart(self.df_distance)
        self.text = st.empty()

    def update(self, best_path, distance):
        lines_pheromones = self._get_lines_pheromones()
        lines_best_path = []
        start = [best_path[0].x, best_path[0].y]
        for node in best_path:
            lines_best_path.append({
                "start": start,
                "end": [node.x, node.y]
            })
            start = [node.x, node.y]

        self.layer_pheromones.data = lines_pheromones
        self.layer_best_path.data = lines_best_path

        self.r.update()
        self.chart.pydeck_chart(self.r)
        self.distance_chart.add_rows({"Jarak Tempuh": [distance]})
        self.text.markdown(f"__Jarak Tempuh Terbaik__ = {distance:.2f}")
        time.sleep(0.01)

    def _get_init_view(self, lines):
        lat = [line["start"][1] for line in lines]
        lng = [line["start"][0] for line in lines]
        center_lat = (max(lat) - min(lat)) / 2 + min(lat)
        center_lng = (max(lng) - min(lng)) / 2 + min(lng)
        return pydeck.ViewState(latitude=center_lat, longitude=center_lng, zoom=9.5, max_zoom=15, pitch=2, bearing=6)

    def _get_lines_pheromones(self):
        lines_pheromones = []
        for (node_index_1, node_index_2), value in self.graph.retrieve_pheromone().items():
            node1 = self.graph.nodes[node_index_1]
            node2 = self.graph.nodes[node_index_2]
            lines_pheromones.append({
                "start": [node1.x, node1.y],
                "end": [node2.x, node2.y],
                "value": value,
            })
        return lines_pheromones
