# Book Recommender System

## Overview

- This project is a Collaborative Filtering Recommendation System using Streamlit, simplifying book selection by recommending similar books based on user input. It provides a list of the top 10 similar books for a specific search, enhancing the reading experience.

## Features

- *Personalized Recommendations*: Suggests books based on user preferences and reading history.
- *Collaborative Filtering*: Recommends books by analyzing similar users' reading patterns.
- *Content-Based Filtering*: Provides suggestions based on the book’s attributes, such as genre, author, and keywords.
- *User Profiles*: Allows users to create and update profiles with their reading preferences.
- *Search Functionality*: Enables users to search for books by title, author, or genre.
- *Ratings and Reviews*: Users can rate and review books to improve recommendation accuracy.
- *Trending Books*: Displays a list of currently popular and trending books.
## Technologies Used

- *Python*: The programming language used for development.
- *Scikit-learn*: For implementing machine learning algorithms.

## Running the model


1. *Download the dataset:*

    Books.csv, Ratings.csv, Users.csv
      ```bash
    https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
    ```
    

3. *Run the Book Recommender.ipynb:*

    to place the pickle files:

    The pickle files are placed as
    {model.pkl, book_names.pkl, final_df.pkl, book_pivot.pkl}
    
    

## Installation 

To run this model, you need to have Python and streamlit installed on your system. Follow these steps to set up the project:


1.  *Install Dependencies:*


    Ensure you are in the project directory:

    ```bash
    pip install streamlit
    ```

2. *Run the Script:*

    Start the model by running the script:

    ```bash
    streamlit run app.py
    ```

3. *Instructions:*

    - *Find Books*: Enter the title, author, or genre into the search bar to discover books.
    - *Advanced Filters*: Utilize advanced filters to narrow down search results by publication date, rating, or language.
    - *Recommendation Sections*: Explore different recommendation sections like "Based on Your Reading History," "Top Picks for You," and "New Releases You Might Like."
    - *Rate Books*: Provide star ratings for books you have read to refine the recommendation engine.

## Additional Notes
- *Dependencies*: Ensure Python and necessary libraries are installed.
- *Environment*: It's recommended to use a virtual environment for dependency management
