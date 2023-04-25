# CoachUTD



## Usage

### Pipenv

This is the preferred way of starting the app, but requires pipenv.

From the project directory, install pipenv and set up up the pipenv environment.

```
$ python3 -m pip install pipenv
$ python3 -m pipenv install
$ python3 -m pipenv shell
```

Run the app with flask.

```
$ flask run --debug
```

Or test with pytest.

```
$ pytest
```

### Virtualenv

You can run without pipenv using the provided `requirements.txt` file.

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Then run `flask` or `pytest` as above.


