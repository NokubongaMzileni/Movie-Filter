def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            movieId INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            genres TEXT
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userId INTEGER,
            movieId INTEGER,
            rating REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(userId) REFERENCES users(id),
            FOREIGN KEY(movieId) REFERENCES movies(movieId)
        )
    ''')
    db.commit()
