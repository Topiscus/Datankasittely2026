# TODO:
# Import pandas library
# Import fetch_data from client.api_client
# Import validate_items from utils.validators
# In the main function:
#   - fetch items from the API using the fetch_data function
#   - validate the received items using the validate_items function, which returns True if the items are valid, otherwise raises a ValueError with an appropriate message
#   - write the valid items to a dataframe using pandas, and then save the dataframe to a JSON file named "data/posts.json"

import pandas as pd
from client.api_client import fetch_data
from utils.validators import validate_items


def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    items = fetch_data(api_url)

    print("Validating items…")
    validate_items(items)

    json_file_path = "data/posts.json"

    df = pd.DataFrame(items)
    df.to_json(json_file_path, orient="records", indent=4)

if __name__ == "__main__":
    main()