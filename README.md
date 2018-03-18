## Comparing Celery-RabbitMQ Docker cluster, Multi-Threading and Scrapy Framework

-------------------------

##### Versions

- Docker-compose : `docker-compose version 1.8.0, build unknown`
- Docker : `Docker version 17.12.0-ce, build c97c6d6`
- Python: Python:3 docker image being used in dockerfile
-----------------------


### How to run docker cluster

- Run command `sudo docker-compose up`

- Above command will start 1 container for each worker and rabbit

- Now go inside one worker container and run `python -m celery_main.task_submitter`

- this will start pushing tasks in rabitmq and workers



##### Speedup the docker cluster

- To run 5 workers and 1 rabbitmq:

  `sudo docker-compose up --scale worker=5`

- To increase the concurrency, update docker file, delete the image and rebuild.

- Do not increase concurrency to too much in dockerfile as machine might not be able to handle it

  `ENTRYPOINT celery -A test_celery worker --concurrency=10 --loglevel=info`



----------------------

### How to check multi-threaded approach.

- Activate the virtual environment.
- Run the program `python multithread`

---------------

### How to check Scrapy framework

- Create a scrapy project and