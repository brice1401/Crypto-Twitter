# Crypto-Twitter
A project to extract data from specific twitter account and find link to crypto

This project is running with `python3.8` or greater.

## Installation

Create a `venv` and install the project's dependencies:
```shell
# Create a venv and activate it
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install the libraries needed to run this project
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

1. Request Twitter API credentials [here](https://developer.twitter.com/en/portal)
2. Receive your twitter credentials
3. Copy `credentials-template.json` as `credentials.json` and replace 
   the `TODO` tag with your own credentials.
   
Please contact this project contributor if you encounter issues while configuring this project.

## Run

```shell
# Activate your venv if it's not already activated
source .venv/bin/activate

# Run
python main.py
```

### Run a playground script

```shell
# With your venv activated
# To run the 'main' of the playground/listen_for_keywords_in_status.py in a terminal 
python -m playground.listen_for_keywords_in_status
```
-----------------

## Conventions

* All the package name should be in plural
* The variable name should be as explanatory as possible
* Do pull requests (PR) if you have doubts on your code quality
* Do not push data on GitHub
* If you have a doubt, read the `import this` manifesto (_The Zen of Python_, by **Tim Peters**)

## Toolkit

```shell
# Display a unicode character in terminal
echo -e "\u2026"
# Display the actual representation of this character, which is here: …
```