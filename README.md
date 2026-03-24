## Book recommender system

Machine Learning Model:  
https://colab.research.google.com/drive/17UDEOebqzlLs9-HO2W5Ob9mHzZGzrRng?usp=sharing

Dataset:  https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

After creating a model save "popular.pkl", "books.pkl", "pt.pkl" and "similarity_score.pkl" files and upload to root directory

📚 Book Recommender System (Flask)

A machine learning–powered book recommendation system built with Flask that suggests books to users based on similarity between books.
The system uses data processing and similarity techniques to recommend books that match the user’s interests.

This project demonstrates how machine learning models can be integrated into a web application to deliver real-time recommendations through a simple and interactive interface.

🚀 Features
📖 Book Recommendations – Suggests similar books based on the selected title
🤖 Machine Learning Model – Uses similarity-based recommendation algorithms
🌐 Flask Web Application – Lightweight backend for serving recommendations
🎨 User-Friendly Interface – Simple and clean UI for easy interaction
⚡ Fast Recommendations – Preprocessed data enables quick suggestions
🧠 Recommendation Approach

🧠 Machine Learning Model
The machine learning model is trained using a dataset of books and user ratings.

You can view the full model training notebook here:

Colab Notebook:
https://colab.research.google.com/drive/17UDEOebqzlLs9-HO2W5Ob9mHzZGzrRng?usp=sharing

📊 Dataset

Dataset used for training the recommendation model:

Kaggle Dataset:
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

📦 Model Files

After running the machine learning notebook, save the following files:

popular.pkl
books.pkl
pt.pkl
similarity_score.pkl

Upload these files to the root directory of the project.

These files are required for the Flask application to generate recommendations.
The recommendation engine works by:

Processing a dataset of books and user ratings
Building a similarity matrix between books
When a user selects a book:
The system finds similar books using similarity scores
Returns the top recommended titles

This approach is commonly used in content-based recommendation systems.

🛠️ Tech Stack

Languages & Frameworks

Python
Flask

Libraries

Pandas
NumPy
Scikit-learn
Pickle

Frontend

HTML
CSS
Bootstrap

📂 Project Structure
Book-recommender-system-Flask
│
├── app.py                # Main Flask application
├── model.pkl             # Trained recommendation model
├── books.pkl             # Book dataset
├── similarity_scores.pkl # Similarity matrix
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── static/
│   └── styles.css
│
└── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/Prakruthir12/Book-recommender-system-Flask.git
cd Book-recommender-system-Flask
2️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Application
python app.py

Open your browser and visit:

http://127.0.0.1:5000/
