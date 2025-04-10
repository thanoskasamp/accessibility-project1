from django.shortcuts import render

# Create your views here.
# webgis_app/views.py
import os
from django.shortcuts import render
import folium
from folium.plugins import MarkerCluster, Realtime, Draw, LocateControl
from folium import JsCode

# Import your custom control if it's in the same app folder
from webgis_app.custom_control import CustomControl

def map_view(request):
    # 1. Create a Folium map with no default basemap.
    m = folium.Map(
        location=[40.618, 22.975],    
        zoom_start=14,
        width='100%',
        height='100%',
        tiles=None  # We'll add our own basemap below
    )

    # 2. Add Base Layers
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

    # 3. Load Your Legend HTML
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    legend_path = os.path.join(base_dir, 'custom_html', 'my_legend.html')
    with open(legend_path, 'r', encoding='utf-8') as f:
        legend_html = f.read()

    # 4. Create & Add Your Custom Legend Control
    legend_control = CustomControl(legend_html, position='bottomright')
    m.add_child(legend_control)

    # 5. Add WMS Layer
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

    # 6. Add Plugins
    Draw(export=True).add_to(m)
    LocateControl().add_to(m)

    # 7. Layer Control
    folium.LayerControl().add_to(m)

    # 8. Convert Your Folium Map to HTML
    map_html = m._repr_html_()

    # 9. Render Your Template & Pass the Map HTML
    return render(request, 'map.html', {'map': map_html})
