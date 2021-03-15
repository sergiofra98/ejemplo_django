export nombre_cont="super_heroes"
export version=":v0.0.1"
docker build --network=host --tag $nombre_cont$version .;

docker run -p 8000 super_heroes