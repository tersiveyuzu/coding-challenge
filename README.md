# System Integration Coding Challenge #

This repository is a template for the **processing customer service requests** of an open source ticketing tool called Zammad. **It's objective** is to prioritize tickets based on sentiment analysis model scores.


### Getting Started ###

```
$ git clone https://github.com/tersiveyuzu/coding-challenge.git      # clone repository
$ docker-compose up -d                                               # start the services
- go to http://localhost:8080
- create an auth token with maximum permissions
- set an environment variable ZAMMAD_TOKEN
$ virtualenv venv --python=python3.8                                 # create your virtual environment
$ source venv/bin/activate                                           # activate your virtual environment
$ cd src                                                             # change directory
$ pip install -r requirements.txt                                    # install packages
$ python main.py                                                     # run extract, transform, update tickets via api
```
