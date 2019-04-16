import pandas as pd


books = pd.read_csv("books.csv")
books = books.drop(columns = ["id", "book_id", "best_book_id", "work_id", "books_count", "isbn13", "work_ratings_count", "work_text_reviews_count", "ratings_1","ratings_2", "ratings_3", "ratings_4", "ratings_5"])
books = books.dropna()
books.to_csv("books_clean.csv")
