# 📚 Book Recommender System (Flask)

A **machine learning–powered book recommendation system** built with **Flask** that suggests books to users based on similarity between books.

The system uses data processing and similarity techniques to recommend books that match the user’s interests.

This project demonstrates how **machine learning models can be integrated into a web application** to deliver real-time recommendations through a simple and interactive interface.

---

## 📌 Machine Learning Model

The machine learning model is trained using a dataset of books and user ratings.

**Colab Notebook:**  
https://colab.research.google.com/drive/17UDEOebqzlLs9-HO2W5Ob9mHzZGzrRng?usp=sharing

The notebook includes:

- Data cleaning
- Exploratory data analysis
- Popularity-based recommendation
- Collaborative filtering
- Similarity matrix generation
- Model file creation

---

## 📊 Dataset

Dataset used for training the recommendation model:

**Kaggle Dataset**  
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

The dataset contains:

- Books information
- User ratings
- User data

---

## 📦 Model Files

After running the machine learning notebook, save the following files:

```
popular.pkl
books.pkl
pt.pkl
similarity_score.pkl
```

Upload these files to the **root directory of the project**.

These files are required for the Flask application to generate recommendations.

---

## 🚀 Features

- 📖 **Book Recommendations** – Suggests similar books based on the selected title
- 🤖 **Machine Learning Model** – Uses similarity-based recommendation algorithms
- 🌐 **Flask Web Application** – Lightweight backend for serving recommendations
- 🎨 **User-Friendly Interface** – Simple and clean UI for easy interaction
- ⚡ **Fast Recommendations** – Preprocessed data enables quick suggestions

---

## 🧠 Recommendation Approach

The recommendation engine works by:

1. Processing a dataset of books and user ratings
2. Building a similarity matrix between books
3. When a user selects a book:
   - The system finds similar books using similarity scores
   - Returns the top recommended titles

This approach is commonly used in **content-based recommendation systems**.

---

## 🛠️ Tech Stack

### Languages & Frameworks
- Python
- Flask

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Frontend
- HTML
- CSS
- Bootstrap

---

## 📂 Project Structure

```
Book-recommender-system-Flask
│
├── app.py                # Main Flask application
├── popular.pkl
├── books.pkl
├── pt.pkl
├── similarity_score.pkl
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── static/
│   └── styles.css
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Prakruthir12/Book-recommender-system-Flask.git
cd Book-recommender-system-Flask
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

