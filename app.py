import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pd.read_pickle('popular.pkl')
pt = pd.read_pickle('pt.pkl')
books = pd.read_pickle('books.pkl')
similarity_score = pd.read_pickle('similarity_score.pkl')

books['Image-URL-M'] = books['Image-URL-M'].str.replace('http://', 'https://')

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_of_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    user_input_lower = user_input.lower()

    if user_input_lower not in map(str.lower, pt.index):
        return render_template('recommend.html', error_message='Book not found')

    index = np.where(pt.index.str.lower() == user_input_lower)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)