# import json
# from shapely.geometry import shape
# from tkintermapview import TkinterMapView
# import tkinter as tk
#
# def create_map_widget(parent_frame):
#     with open("almaty-districts.geo.json", encoding="utf-8") as f:
#         geojson_data = json.load(f)
#
#     # Получаем центры районов
#     district_centers = {}
#     for feature in geojson_data["features"]:
#         district_name = feature["properties"]["name"]
#         polygon = shape(feature["geometry"])
#         centroid = polygon.centroid
#         district_centers[district_name] = (centroid.y, centroid.x)
#
#     # Создание виджета карты
#     map_widget = TkinterMapView(parent_frame, width=1280, height=700, corner_radius=12)
#     map_widget.set_position(43.238949, 76.889709)  # Центр Алматы
#     map_widget.set_zoom(11)
#     map_widget.pack(pady=20)
#
#     # Рисуем границы районов
#     for feature in geojson_data["features"]:
#         geometry = feature["geometry"]
#         if geometry["type"] == "Polygon":
#             rings = [geometry["coordinates"]]
#         elif geometry["type"] == "MultiPolygon":
#             rings = geometry["coordinates"]
#         else:
#             continue
#
#         for ring in rings:
#             coords = ring[0]
#             path = [(lat, lon) for lon, lat in coords]
#             if path[0] != path[-1]:
#                 path.append(path[0])
#             map_widget.set_path(path)
#
#     # Подписи для каждого района
#     ramp_counts = {
#         "Alatau": {"available": 359, "partly": 534},
#         "Bostandyq": {"available": 507, "partly": 1157},
#         "Auezov": {"available": 1610, "partly": 590},
#         "Nauryzbay": {"available": 288, "partly": 243},
#         "Medeu": {"available": 562, "partly": 637},
#         "Zhetysu": {"available": 482, "partly": 353},
#         "Turksib": {"available": 279, "partly": 1191},
#         "Almaly": {"available": 683, "partly": 609},
#     }
#
#     for district, (lat, lon) in district_centers.items():
#         info = ramp_counts.get(district, {"available": "?", "partly": "?"})
#         map_widget.set_marker(
#             lat, lon,
#             text=f"{district}\nAvailable: {info['available']}\nPartly: {info['partly']}"
#         )




import json
from shapely.geometry import shape
from tkintermapview import TkinterMapView
import tkinter as tk

def create_map_widget(parent_frame):
    with open("almaty-districts.geo.json", encoding="utf-8") as f:
        geojson_data = json.load(f)

    # Получаем центры районов
    district_centers = {}
    for feature in geojson_data["features"]:
        district_name = feature["properties"]["name"]
        polygon = shape(feature["geometry"])
        centroid = polygon.centroid
        district_centers[district_name] = (centroid.y, centroid.x)

    # Создание виджета карты
    map_widget = TkinterMapView(parent_frame, width=1280, height=700, corner_radius=12)
    map_widget.set_position(43.238949, 76.889709)  # Центр Алматы
    map_widget.set_zoom(11)
    map_widget.pack(pady=20)

    # Рисуем границы районов
    for feature in geojson_data["features"]:
        geometry = feature["geometry"]
        if geometry["type"] == "Polygon":
            rings = [geometry["coordinates"]]
        elif geometry["type"] == "MultiPolygon":
            rings = geometry["coordinates"]
        else:
            continue

        for ring in rings:
            coords = ring[0]
            path = [(lat, lon) for lon, lat in coords]
            if path[0] != path[-1]:
                path.append(path[0])
            map_widget.set_path(path)

    # Подписи для каждого района
    ramp_counts = {
        "Alatau": {"available": 359, "partly": 534},
        "Bostandyq": {"available": 507, "partly": 1157},
        "Auezov": {"available": 1610, "partly": 590},
        "Nauryzbay": {"available": 288, "partly": 243},
        "Medeu": {"available": 562, "partly": 637},
        "Zhetysu": {"available": 482, "partly": 353},
        "Turksib": {"available": 279, "partly": 1191},
        "Almaly": {"available": 683, "partly": 609},
    }

    for district, (lat, lon) in district_centers.items():
        info = ramp_counts.get(district, {"available": "?", "partly": "?"})
        map_widget.set_marker(
            lat, lon,
            text=f"{district}\nAvailable: {info['available']}\nPartly: {info['partly']}"
        )







