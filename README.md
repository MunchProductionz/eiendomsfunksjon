# Stonks- / $MEME-project

A project to learn web-scraping and data analysis using:
- Python
- BeatifulSoup
- Finn.no

---

## Virtual environment

### Y though?

Python is bad at managing dependencies, especially when everything is run at a global level. We use virtual environments to get around this

### Virtual environment setup

Virtual environment created according to [this guide](https://realpython.com/python-virtual-environments-a-primer/)

1. Setup a virtual environment:
    - `python -m venv venv`
2. Activate it:
    - `source venv/Scripts/activate`
    - if successful you terminal should look like this: `(venv) $`

3. Install packages using `python -m pip install -r requirements.txt`
    - This should automatically install all relevant packages

4. Open main.py and run the program

5. Deactivate virtual environment with `deactivate`


### How to generate `requirements.txt`

1. Initiate virtual environment according to previous section 

2. Run `python -m pip freeze > requirements.txt`

### Further reading in package management

`venv` isn't deterministic and we may encounter errors in the future. This is an alternative should it be required:

- [Poetry - Python packaging and dependency management made easy](https://python-poetry.org/)