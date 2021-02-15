#!/bin/sh

es_id=$(sudo podman container list -aqf ancestor=aigames/elastic -f status=running);
sudo podman commit $es_id aigames/elastic;
sudo podman stop -a;
sudo podman build --format=docker -t aigames/django django_ai;
sudo podman run -d --network aigames --ip 10.91.0.3 -p 80:80 aigames/django;
sudo podman run -d -e "discovery.type=single-node" --network aigames --ip 10.91.0.4 vitamova/elastic;
