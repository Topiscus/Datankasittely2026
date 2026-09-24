# Pandas books exercise

In this project you will practice a few of the **basic pandas operations** using a dataset of books, and also get more familiar working with Python in Github Classroom exercise.

The project structure is
```
books_project/
│── data/
│ └── books.csv         # dataset
│── main.py             # your code (tasks with TODOs)
│── requirements.txt    # project dependencies
│── tests/
│ └── test_books.py     # pytest tests
│── README.md           # this file
```

## Instructions
1. Clone this repository.
2. Create and activate a virtual environment and install requirements

in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments#_creating-environments), select the requirements.txt file when prompted for dependecies

OR

in cmd:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

I had some trouble with PowerShell and missing admin rights, but the same thing can be done there also.


3. Open main.py and follow the step-by-step instructions in the comments.
See detailed tasks inside the file.

4. To test and run your code, just run the `main.py`. Make sure that you have the correct Pytohn environment in use. Note: The program will not run before you have fixed it!

5. In this project and GitHub Classroom assignment we are using also tests. You can run the tests in the cmd in the project root with:
`python -m pytest`

6. Commit and push your changes to this repository.

## Note

👉 In main.py, the `“if __name__ == "__main__":` makes sure code only runs when the file is executed directly, not when it’s imported for testing.
