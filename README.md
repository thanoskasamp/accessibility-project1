# Public Transportation Accessibility WebGIS Project

## Objective
Enhance the accessibility of public transportation in the neighborhoods of Toumpa and Ano Poli (Thessaloniki) using a full-stack webGIS approach.

## Technical Stack

### Data Collection & Analysis (Backend)
- **Python Libraries**:  
  - **OSMnx**: Extracted geospatial data (buildings, streets, bus stops) from OpenStreetMap.  
  - **GeoPandas** and **Shapely**: Processed and analyzed geospatial data.
- **Network Analysis**:  
  - Calculated shortest walking routes from buildings to their nearest bus stops by connecting buildings to the closest points on the pedestrian network.

### Mapping & Visualization (Frontend)
- **Static Mapping**:  
  - **QGIS**: Produced static maps to display walking routes and accessibility analyses.
- **Interactive Mapping**:  
  - **Folium**: Created dynamic, interactive maps.

### Performance & Data Delivery (Backend Enhancements)
- **Cloud Server**: Hosts the backend stack.
- **Docker**: Containerizes and manages services.
- **PostGIS**: PostgreSQL extension for spatial data storage.
- **GDAL (ogr2ogr)**: Ingests and uploads geospatial data into PostGIS.
- **GeoServer**: Distributes geospatial data using OGC standards (WMS, WFS) to the Folium map.
- **Reverse Proxy**:  
  - **NGINX**: Configured as a reverse proxy for GeoServer.
  - **Certbot**: Used to obtain SSL certificates, ensuring secure HTTPS connections.

### Deployment & Orchestration
- **Docker Compose**:  
  - A `docker-compose.yml` file is included to orchestrate the different services (PostGIS, GeoServer, and other related containers), simplifying the deployment process.

## Key Backend Scripts

- **GDAL Data Import**: `import_data.sh`  
  Uses GDAL's `ogr2ogr` to ingest and upload geospatial data into the PostGIS database.

- **Reverse Proxy Configuration**: `nginx.conf`  
  Configures NGINX as a reverse proxy for GeoServer, managing request routing.

- **SSL Certificate Renewal**: `renew_cert`  
  Automates the renewal of SSL certificates via Certbot to maintain secure HTTPS connections.