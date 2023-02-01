# twitter slackbot etljob w/ sentiment analysis
A Dockerized twitter slackbot that reposts tweets about the AllBlacks (NZ Rugby) from twitter to slack using MongoDB to interact with the Twitter API and a PostgreSQL database.

![image](https://user-images.githubusercontent.com/105222741/216148400-a96b278a-2a97-4796-b58c-cb05f5ae8d85.png)



# To run:
First create a new virtual environment.
> conda create --name {your_env_name} python=3.8

Clone this repository to your local directory.
> git clone https://github.com/Nathan-Austin/twitter_slackbot_etljob.git

Install Docker and Docker dependencies such as Docker Desktop
Go to the [Docker Documentation](https://docs.docker.com/), find the installation instructions and install Docker CE.

####Goto the cloned directory 
In the Terminal run:

> nano .env

This will create a new .env file and inside this you need to add your secret information:

> BEARER_TOKEN = "your token here"   # this is from twitter, see below for more details

> WEBHOOK_URL =  "your token here"   # this is from slack, see below for more details

> POSTGRES_USER = "your token here"

> POSTGRES_PASSWORD=  "your token here"


### TWITTER API TOKEN

Step 1: Get a Twitter Bearer Token

2: Register your application on apps.twitter.com.

3: Navigate to the Twitter App dashboard and open the Twitter App for which you would like to generate access tokens.

4: Navigate to the “keys and tokens” page.

5: You’ll find the API keys, user Access Tokens, and Bearer Token on this page.

6: Write down the Bearer Token


### SLACK WEBHOOK_URL


To build a Slack Bot, you need to:

Login and go to [Your Apps](https://api.slack.com/apps)

Choose Create New App

Choose the option From scratch

Fill in a name and choose your slack workspace as Development Slack Workspace

Press Create App

Under Add features and functionality click on Incoming Webhooks

Activate incoming webhooks by clicking on the switch

Click on Add new webhook to the workspace at the bottom of the page

Select a channel where you want to post messages and click on Allow

Scroll down and copy the Webohook URL into the code:
  

### In the terminal run:

> docker-compose build

> docker-compose up

This will start the container. 

It is currently set to repost a randomly selected tweet every 60 seconds. You can change thi time by adjusting the sleep time at the 
bottom of each .py file.
You can remove the limit &/or random in the sql query in the slack.py file.
You can also adjust the content in the get_tweets.py file byt changing the username form 'allblacks' ( the NZ natioanl rugby team).




