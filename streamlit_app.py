import pickle
import streamlit as st 
import numpy as np

st.header('📚 Book Recommender System 📖📖 ')

model = pickle.load(open('/Users/asus/Downloads/project/Book-Recommender-System-main/Book-Recommender-System-main/book/model.pkl','rb'))
book_names = pickle.load(open('/Users/asus/Downloads/project/Book-Recommender-System-main/Book-Recommender-System-main/book/book_names.pkl','rb'))
final_df=pickle.load(open('/Users/asus/Downloads/project/Book-Recommender-System-main/Book-Recommender-System-main/book/final_df.pkl','rb'))
book_pivot = pickle.load(open('/Users/asus/Downloads/project/Book-Recommender-System-main/Book-Recommender-System-main/book/book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_df['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_df.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

def recommend_book_name(book_naam):
    books_list = []
    query_index = np.where(book_pivot.index == book_naam.lower())[0][0]
    distance, suggestion_indices = model.kneighbors(book_pivot.iloc[query_index,:].values.reshape(1,-1), n_neighbors=11 )
    
    poster_url = fetch_poster(suggestion_indices)
        
    for index in suggestion_indices.flatten():
        books_list.append(str(book_pivot.index[index]).title())
        
    return books_list , poster_url

display_book_names=[val.title() for val in book_names]
        
selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    display_book_names
)
        
if st.button('Show Recommendation'):
    recommended_books,poster_url = recommend_book_name(selected_books)

    # Create two rows with 5 columns each
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])

    # Create a second row
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(recommended_books[6])
        st.image(poster_url[6])
    with col7:
        st.text(recommended_books[7])
        st.image(poster_url[7])
    with col8:
        st.text(recommended_books[8])
        st.image(poster_url[8])
    with col9:
        st.text(recommended_books[9])
        st.image(poster_url[9])
    with col10:
        st.text(recommended_books[10])
        st.image(poster_url[10])
