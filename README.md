# twitter_slackbot_etljob
A twitter slackbot that reposts tweets from twitter to slack using MongoDB and Docker.

# To run:

Clone this repository to your local directory.
Install Docker and Docker dependencies such as Docker Desktop
Go to the [Docker Documentation](https://docs.docker.com/), find the installation instructions and install Docker CE.

## First, create a new container from an existing image

$docker run -d -it --name {slackbot} python:3.8  {add yourown container name}

Connect to a container

You can attach a terminal to a container and see what is going on inside.

$docker attach slackbot

To detach the terminal (without killing the process), press CTRL-p followed by CTRL-q.

Useful Docker Commands
command                                             description

docker images                                       ist all installed images

docker ps -a                                        list all running and stopped containers

docker run <image>                                  start a new container

docker exec                                         run a command inside a container

docker attach                                       connect to an interactive container

docker inspect <id or name>                         provide more details about running container (e.g. IP address)

docker rmi <id or name>                             remove an image

docker rm <id or name>                              remove a container

## Build your own image using Docker

Use the Dockerfile provided inthe repo or create your own Dockerfile

Use an official Python runtime as a parent image
FROM python:3.6

Set the working directory to /app
WORKDIR /app

Copy the requirements file into the container at /app
(a text files with all the libraries you want to install)
COPY requirements.txt /app

Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

Run app.py when the container launches
CMD ["python", "app.py"]

## Create the image from this file with:

docker build -t slackbot .

## Run it using the command below:

docker run -it -v /some/local/path/:/app/ slackbot

The -v option “borrows” a local directory to the container. It is a practical way to exchange files without rebuilding the image.

Hint Pro-tip:
You can write $PWD instead of /some/local/path/ as a placeholder for your actual current working directory.

## Build a Pipeline with Docker-Compose

In the project, we will use docker-compose to orchestrate a data pipeline with five containers:

name                image               description

tweet_collector     self-made           collects tweets and stores them in MongoDB

mongodb             mongo               stores tweets as JSON documents

etl_job             self-made           analyzes sentiment of tweets from MongoDB and stores them in PostgreSQL

postgresdb          postgres            stores tweets and annotation in a table

slack_bot           self-made           publishes highly ranking tweets in a Slack channel

