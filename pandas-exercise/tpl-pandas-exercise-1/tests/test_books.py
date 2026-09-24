import os
import pytest
import pandas as pd
from main import (
    load_data,
    get_unique_genres,
    find_books_by_author,
    get_highest_rating
)

@pytest.fixture
def df():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Project root
    test_file = os.path.join(base_dir, "data", "books.csv")
    return load_data(test_file)

def test_load_data(df):
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 71

def test_unique_genres(df):
    genres = get_unique_genres(df)
    assert isinstance(genres, (list, pd.Series))
    assert "Fiction" in genres
    assert "Classic" in genres

def test_author_books(df):
    orwell_books = find_books_by_author(df, "George Orwell")
    assert isinstance(orwell_books, pd.DataFrame)
    assert not orwell_books.empty
    assert "1984" in orwell_books["title"].values

def test_highest_rating(df):
    rating = get_highest_rating(df)
    assert isinstance(rating, (float, int))
    assert rating >= 4.5
