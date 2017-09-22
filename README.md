# Coherent


[![CircleCI](https://circleci.com/gh/rjweeks/coherent/tree/master.svg?style=svg)](https://circleci.com/gh/rjweeks/coherent/tree/master)


## Setup
Based on python 3.6

Create a virtual env for python3 and make sure that it's activated

```
mkvirtual --python=</path/to/python3.6 <your env name>
```

Install dependencies for the application using pip

```
pip install -r requirements.txt
```

Run the application
-
```
$ python run.py
 * Running on http://127.0.0.1:5050/
 * Restarting with reloader
```

Test the application
-
Install dependencies for the tests using pip

```
pip install -r requirements-test.txt
```
Once these have been installed the tests can be run from the ras-secure-message directory using the following
```
python run_tests.py
```

Test the response
-

Now open up a prompt to test out your API using curl
```
$ curl http://127.0.0.1:5050/health
{"status": "healthy"}
```

Docker
-

docker build -t "coherent" .

docker run -d -p 5050:5050 coherent
