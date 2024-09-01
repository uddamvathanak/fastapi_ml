# Fastapi-ML
Fastapi-ML is a project that demonstrates how to deploy machine learning models using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. This repository provides a step-by-step guide to building and deploying a machine learning model API on Heroku, enabling easy integration of machine learning capabilities into web applications.

**Key features**:

- Implementation of a RESTful API using FastAPI.
- Integration of pre-trained machine learning models for inference.
- Deployment on Heroku for easy and scalable cloud hosting.
- Minimal Examples and best practices for serving machine learning models in production.

Whether you're looking to deploy your machine learning models in the cloud or explore FastAPI as a web framework, this repository serves as a practical guide for getting started.

**Dependencies**:

```
fastapi==0.95.2
uvicorn==0.22.0
```

Install dependencies using

```bash
python -m pip install requirements.txt
```

## ML model

We will be using [Prophet](https://facebook.github.io/prophet/) to predict stock market prices.

## Deployment to Heroku

For this tutorial, we will be hosting the application on heroku server. Please [sign up](https://signup.heroku.com/) for a Heroku account, and then install the Heroku CLI.

***Don't forget too add payment method.***

```bash
heroku login
```

```bash
heroku create
```

Next, we will be using the Heroku Container Registry to deploy the application with Docker using:

```bash
heroku container:login
```

***Make sure that you have install Docker successfully and it is currently running.*** it can be tested using `docker ps` in the terminal or command-line.



Add a Dockerfile file to the project root (refer to our Dockerfile).

Add a .dockerignore file (refer to our file as well).

Build the Docker image using command:

```bash
docker build -t registry.heroku.com/aqueous-wildwood-97407/web .
```
The running of docker will take awhile to finish.

Then run command below to test the function.

```bash
docker run --name fastapi_ml -e PORT=8008 -p 8008:8008 -d registry.heroku.com/aqueous-wildwood-97407/web:latest
```

Open another CMD and enter:

```bash
curl --header "Content-Type: application/json" --request POST --data "{\"ticker\":\"MSFT\"}" http://localhost:8008/predict
```

you should receive output in JSON format something like

```bash
{"ticker":"MSFT","forecast":{"09/02/2024":447.36687922756676,"09/03/2024":447.65588717590146,"09/04/2024":447.9448951242364,"09/05/2024":448.2339030725712,"09/06/2024":448.522911020906,"09/07/2024":448.81191896924093,"09/08/2024":449.1009269175758}}
```

If it working as expected.

stop the docker from running and remove the docker.

```bash
docker stop fastapi_ml
```

```bash
docker rm fastapi_ml
```

Push the image to the registry:

```bash
docker push registry.heroku.com/aqueous-wildwood-97407/web
```

***WARNING: the name of the container must match with the app created in heroku***

After we push to the repo, we then can release the image:

```bash
heroku container:release -a aqueous-wildwood-97407 web
```

for some reason they would ask to run

```bash
git push heroku main
```

## End note:

Feel free to ask me any questions and provide suggestion for this guide.

## Contact me:
vathanakuddam@gmail.com