# Coherent


[![CircleCI](https://circleci.com/gh/rjweeks/coherent/tree/master.svg?style=svg)](https://circleci.com/gh/rjweeks/coherent/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/488e430a7713465190f0791b438f4b77)](https://www.codacy.com/app/rjweeks/coherent?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rjweeks/coherent&amp;utm_campaign=Badge_Grade)


## Setup
Based on python 3.6

Create a virtual env for python3 and make sure that it's activated

```
mkvirtual --python=</path/to/python3.6 <your env name>
```

Check python version

```
pyenv version
```

If required install Python version 3.6.3

```
pyenv install 3.6.3
```

If it's already installed switch to it by

```
pyenv local 3.6.3
```

Install dependencies for the application using pipenv

```
pipenv install
```

Run the application in Pyenv
-
```
$ pipenv run python run.py
 * Running on http://127.0.0.1:5050/
 * Restarting with reloader
```

Or

```
pyenv shell
python run.py
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
