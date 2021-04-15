docker build -f Dockerfile.web -t jupyter-resty .


# docker run -it --env PORT=8001 -p 8188:8001 jupyter-resty

# docker run jupyter-resty /bin/bash

# docker tag <img-tag> registry.heroku.com/<heroku-app>/<proccess>

# docker push registry.heroku.com/<heroku-app>/<proccess>