sudo podman run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.11.0;
es_id=$(sudo podman container list -aqf ancestor=elasticsearch -f status=running);
sudo podman commit $es_id aigames/elastic;
sudo podman stop $es_id;
sudo podman network create aigames --subnet 10.91.0.0/24;