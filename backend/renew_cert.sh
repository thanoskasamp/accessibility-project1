#!/bin/bash
# Stop NGINX so Certbot can bind to port 80
docker-compose stop nginx

# Run Certbot in standalone mode to renew certificates
docker run -it --rm -p 80:80 \
  -v /root/accessibility-project1/backend/certs:/etc/letsencrypt \
  certbot/certbot renew --quiet

# Restart NGINX
docker-compose up -d nginx
