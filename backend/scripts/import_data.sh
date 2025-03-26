#!/usr/bin/env bash

# Set PostGIS credentials.
source /backend/.env
export POSTGIS_USER=${POSTGRES_USER}
export POSTGIS_PASSWORD=${POSTGRES_PASSWORD}
export POSTGIS_DB=${POSTGRES_DB}

# Change directory to where the GeoPackage files are stored.
cd /data

# Loop through each .gpkg file in the directory.
for file in *.gpkg; do
    # Derive the schema name from the filename (remove .gpkg extension).
    schema=$(basename "$file" .gpkg)
    echo "Processing $file, targeting schema '$schema'..."

    # Create the schema if it doesn't exist.
    psql "host=postgis_db port=5432 dbname=$POSTGIS_DB user=$POSTGIS_USER password=$POSTGIS_PASSWORD" \
         -c "CREATE SCHEMA IF NOT EXISTS $schema;"

    # Import all layers from the GeoPackage into the specified PostGIS schema.
    ogr2ogr -f "PostgreSQL" \
      PG:"host=postgis_db port=5432 dbname=$POSTGIS_DB user=$POSTGIS_USER password=$POSTGIS_PASSWORD" \
      -lco SCHEMA=$schema \
      "$file"
done

echo "Import complete."
