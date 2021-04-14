docker build -f Dockerfile.web -t jupyter-resty .


# docker run -it --env PORT=8001 -p 8188:8001 jupyter-resty