# fee calculator microservice

## Include a Docker container to run a Flask app

To run the app locally install `docker` then:

```
docker build --rm -f "Dockerfile" -t feecalculator:latest .
docker run --rm -d feecalculator:latest
```

or just:
```
python3 -m flask run
```

## Deploy
You need a google cloud account and gcloud tool installed and configured.
The example app is hosted in google cloud run.
A bash script is included but you have change the project ID.
```
bash deploy.sh
```

The app is running at  https://feecalculator-vkal3cbiyq-ew.a.run.app/fee/12/2000
