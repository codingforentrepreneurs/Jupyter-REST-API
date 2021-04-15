- Related Post [section 7](https://www.codingforentrepreneurs.com/blog/jupyter-production-server-on-docker-heroku)
- Heroku [container docs](https://devcenter.heroku.com/articles/container-registry-and-runtime)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Serverless Container Python App](https://www.codingforentrepreneurs.com/projects/serverless-container-python-app)

```
heroku create jupyter-resty
```
> Replace `jupyter-resty` with the app name of your choosing

```
heroku container:login
```


```
docker tag jupyter-resty registry.heroku.com/jupyter-resty/web
docker push registry.heroku.com/jupyter-resty/web
```
> Replace `jupyter-resty` with the app name of your choosing

```
heroku container:push --recursive
```
> heroku container:push web  if you have want to specificy a process


```
heroku container:release web
```

```
heroku run bash --type web
```

```
heroku open
```