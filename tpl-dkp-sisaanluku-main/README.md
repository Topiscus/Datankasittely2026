# API data ingestion exercise

In this project you will practice **using the `requests` library**, **handling API data**, **validating items**, and **saving JSON to a file**. 

The project structure is
```
api_project/
│── client/
│ └── api_client.py         # your code for fetching data (TODOs)
│── utils/
│ └── validators.py         # validate_items function
│── data/
│ └── posts.json            # output file with API data
│── tests/                  # unit tests
│ └── test_api_client.py
│ └── test_main.py
│── main.py                 # your code (TODOs)
│── requirements.txt        # project dependencies
│── README.md # this file
```

## Instructions
1. Clone this repository.
2. Create and activate a virtual environment and install requirements

in [Visual Studio Code (instructions here)](https://code.visualstudio.com/docs/python/environments#_creating-environments), select the requirements.txt file when prompted for dependencies

OR

in cmd:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Open api_client.py and main.py and follow the step-by-step instructions in the comments. The point is to fetch data from an API, validate it and save the data to a file.

4. To run your code, make sure that you have the correct Python environment in use (in VS Code you have to select the correct environment interpreter).

5. Run tests in cmd: 
```
pytest
```
6. Commit and push your changes to this repository.
