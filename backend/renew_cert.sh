#!/bin/bash

cd "$(dirname "$0")"

echo "Stopping NGINX to free up port 80..."
docker compose stop nginx

echo "Renewing SSL certificates using Certbot..."
docker run --rm -p 80:80 \
  -v "$(pwd)/certs:/etc/letsencrypt" \
  certbot/certbot renew --standalone --preferred-challenges http --quiet

echo "Restarting NGINX..."
docker compose up -d nginx

echo "SSL renewal process completed."
