# webgis_app/views.py
import os
from django.shortcuts import render
import folium
from folium.plugins import MarkerCluster, Realtime, Draw, LocateControl
from folium import JsCode

# Import your custom control if it's in the same app folder
from webgis_app.custom_control import CustomControl

def map_view(request):
    # 1. Create a Folium Figure with explicit dimensions.
    fig = folium.Figure(width='100%', height='100%')
    
    # 2. Create a Folium map with no default basemap.
    m = folium.Map(
        location=[40.618, 22.975],
        zoom_start=14,
        tiles=None  # We'll add our own basemap below
    )
    
    # Add the map to the figure so that the Figure's dimensions control its size.
    fig.add_child(m)
    
    # 3. Add Base Layers
    folium.TileLayer(
        'CartoDB positron',
        name='CartoDB Positron',
        control=True,
        show=True  # This layer is visible by default
    ).add_to(m)

    folium.TileLayer(
        'OpenStreetMap',
        name='OpenStreetMap',
        control=True,
        show=False  # This layer is hidden by default
    ).add_to(m)



    # 6. Add WMS Layer
    folium.WmsTileLayer(
        url="https://thanosgis.me/geoserver/wms",  # workspace-level endpoint
        name="Buildings Toumpa (WMS)",
        layers="project1:buildings_toumpa",
        styles="",
        fmt="image/png",
        transparent=True,
        version="1.1.1",
        maxZoom=20,  # Zoom level for WMS visibility
    ).add_to(m)

    # 7. Add Plugins
    Draw(export=True).add_to(m)
    LocateControl().add_to(m)

    # 8. Layer Control
    folium.LayerControl().add_to(m)

    # 9. Render the Figure (which wraps your map) as HTML
    map_html = fig.render()

    # 10. Render Your Template & Pass the Map HTML
    return render(request, 'map.html', {'map': map_html})
