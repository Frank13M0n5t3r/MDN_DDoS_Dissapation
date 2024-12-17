# build docker image
docker build -t object-detection-app .
docker run --cpus=0.5 --memory=512m -p 5010:5010 object-detection-app .


