# System Integration Coding Challenge #

This repository is a template for the **processing customer service requests** of an open source ticketing tool called Zammad. **It's objective** is to prioritize tickets based on sentiment analysis model scores.


### Getting Started ###

```
$ git clone https://github.com/tersiveyuzu/coding-challenge.git      # clone repository
$ cd coding-challenge                                                # change directory
$ docker-compose up -d                                               # start the services
- go to http://localhost:8080
- create an auth token with maximum permissions
- set an environment variable ZAMMAD_TOKEN
$ virtualenv venv --python=python3.8                                 # create your virtual environment
$ source venv/bin/activate                                           # activate your virtual environment
$ pip install -r src/requirements.txt                                # install packages
$ python src/main.py                                                 # run extract, transform, update tickets via api
```


<img width="1440" alt="image" src="https://user-images.githubusercontent.com/115954094/196153122-c807ae58-0889-4352-896a-0e659d227bd4.png">

<img width="1245" alt="image" src="https://user-images.githubusercontent.com/115954094/196153055-1a27e140-cf6a-4745-9453-e0d0605ce8c9.png">

<img width="1037" alt="image" src="https://user-images.githubusercontent.com/115954094/196152583-24c20aab-04eb-4bef-80c8-410a7194f066.png">
