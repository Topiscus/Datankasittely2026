import pandas as pd

filepath = 'data/books.csv'
# ---------------------------------------------------
# Task 1: Load the data
# ---------------------------------------------------
def load_data(filepath):
    """
    👉 Task: Load the CSV file into a pandas DataFrame.
    ✅ To pass: Return a DataFrame with exactly 71 rows.
    
    📌 What to return:
    - A pandas DataFrame created using read_csv()
    """
    # TODO: Load the CSV file
    df = pd.read_csv(filepath)
    return df # Should return DataFrame instead of None







# ---------------------------------------------------
# Task 2: Unique values
# ---------------------------------------------------
def get_unique_genres(df):
    """
    👉 Task: Return a list of unique genres in the dataset.
    ✅ To pass: Must include 'Fiction' and 'Classic' in the result.
    
    📌 What to return:
    - A list of unique genre values from df["genre"]
    """
    list = df["genre"].unique().tolist()
    # TODO: Extract unique genres
    return list  # Shold return a list instead of None


# ---------------------------------------------------
# Task 3: Filter data
# ---------------------------------------------------
def find_books_by_author(df, author_name):
    """
    👉 Task: Return all books written by the given author.
    ✅ To pass: For 'George Orwell', must include '1984'.
    
    📌 What to return:
    - A filtered DataFrame containing only rows where df["author"] is author_name
    """
    list = df[df["author"] == author_name ]
    # TODO: Filter by author
    return list  # Should return a DataFrame instead of None


# ---------------------------------------------------
# Task 4: Load the data
# ---------------------------------------------------
def get_highest_rating(df):
    """
    👉 Task: Return the highest rating in the dataset.
    ✅ To pass: Must be >= 4.5
    
    📌 What to return:
    - A single float value: the maximum of df["rating"]
    """
    # TODO: Find the highest rating
    float = df['rating'].max() 
    return float # Should return a float value instead of None


# ---------------------------------------------------
# Main usage
# ---------------------------------------------------
if __name__ == "__main__":
    # This block runs only when you execute the file directly, e.g.:
    #    python main.py
    #
    # It will not run when pytest imports functions for testing.
    # Use this section to call your functions and print results
    # while you are developing and testing your code.

    df = load_data('data/books.csv')

    print("\n--- Task 1 ---\n")
    print(df.head())

    # Uncomment these lines as you implement each function:
    
    print("\n--- Task 2 ---\n")
    print(get_unique_genres(df))

    print("\n--- Task 3 ---\n")
    print(find_books_by_author(df, "George Orwell"))

    print("\n--- Task 4 ---\n")
    print(get_highest_rating(df))