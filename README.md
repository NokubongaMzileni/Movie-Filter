# 🎬 Movie Filter - Recommendation System

**Movie Filter** is a Flask web application that lets users register, log in, rate movies, and receive personalized recommendations based on content similarity. Built with Python, SQLite, and scikit-learn, it uses TF-IDF vectorization and cosine similarity to suggest movies tailored to user preferences.

---

## 🚀 Features

- User signup and login
- SQLite-powered database
- Movie rating and storage
- Personalized content-based recommendations
- Movie search functionality
- Ready for deployment on Render

---

## 🛠️ Setup

1. **Clone the repo**  
   `git clone https://github.com/NokubongaMzileni/Movie-Filter.git && cd Movie-Filter`

2. **Create virtual environment**  
   `python -m venv .venv && .venv\Scripts\activate` (Windows)  


3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Set up `.env` file**  
   Create a `.env` file and add:  
SECRET_KEY=your_super_secret_key


5. **Run the app**  
`python app.py`

---

## 🌐 Deployment (Render)

- Add a `render.yaml` file with build and start commands
- Set `SECRET_KEY` in Render’s environment settings
- Deploy from GitHub

---

## 📁 Structure

- `app.py` – main Flask app
- `templates/` – HTML pages
- `data/` – CSV files (movies and ratings)
- `database.db` – SQLite database
- `.env` – stores secret key
- `requirements.txt` – app dependencies

---

## 👤 Author

**Nokubonga Mzileni**  


