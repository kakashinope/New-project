import sqlite3

class CosmicDatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def open_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def execute_query(self, query, params=None):
        if params is None:
            params = []
        self.cursor.execute(query, params)
        self.conn.commit()

    def create_tables(self):
        self.open_connection()
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                imgUrl TEXT
            )''')
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password TEXT,
                role TEXT
            )''')
        self.close_connection()

    def add_news(self, title, description, imgUrl):
        self.open_connection()
        self.execute_query('''INSERT INTO news (title, description, imgUrl) VALUES (?, ?, ?)''', [title, description, imgUrl])
        self.close_connection()

    def add_user(self, username, email, password, role):
        self.open_connection()
        self.execute_query('''INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)''', [username, email, password, role])
        self.close_connection()

    def show_table(self, table):
        self.open_connection()
        self.execute_query(f'SELECT * FROM {table}')
        data = self.cursor.fetchall()
        self.close_connection()
        return data

    def get_all_news(self):
        self.open_connection()
        self.execute_query('SELECT * FROM news')
        data = self.cursor.fetchall()
        self.close_connection()
        return data

    def get_news_by_id(self, id):
        self.open_connection()
        self.execute_query('SELECT * FROM news WHERE id = ?', [id])
        data = self.cursor.fetchall()
        self.close_connection()
        return data

    def add_cosmic_article(self, title, description, imgUrl):
        self.add_news(title, description, imgUrl)

    def get_all_news_with_images(self):
        self.open_connection()
        self.execute_query('SELECT description, imgUrl FROM news')
        data = self.cursor.fetchall()
        self.close_connection()
        return data

# Створення менеджера бази даних
db_manager = CosmicDatabaseManager('db.sqlite')
db_manager.create_tables()

# Список зображень та їх описів
images = [
    ("https://searchthisweb.com/wallpaper/thumb1000/main1000_earth_7680x4320_ejea5.jpg", "Земля"),
    ("https://searchthisweb.com/wallpaper/thumb1000/main1000_mars_3840x2160_jk1uo.jpg", "Марс"),
    ("https://preview.free3d.com/img/2015/10/2272980235332880368/zqnrepta.jpg", "Меркурій"),
    ("https://fons.pibig.info/uploads/posts/2023-06/thumbs/1687274049_fons-pibig-info-p-oboi-venera-krasivo-10.jpg", "Венера"),
    ("https://preview.free3d.com/img/2015/10/2272856533563868502/9qi4sllu.jpg", "Юпітер"),
    ("https://preview.free3d.com/img/2017/09/2272956915455624279/qvrtkgyz.jpg", "Сатурн"),
    ("https://i.obozrevatel.com/news/2020/6/4/unnamed.jpg", "Уран"),
    ("https://kartin.papik.pro/uploads/posts/2023-07/thumbs/1688612504_kartin-papik-pro-p-kartinki-planeta-neptun-v-kosmose-14.jpg", "Нептун"),
    ("https://img.freepik.com/premium-photo/pluto-a-planet-in-the-solar-system_297535-4532.jpg", "Плутон"),
    ("https://kite.od.ua/wp-content/uploads/scale_1200-10.png", "Седна"),
    ("https://watchers.news/wp-content/uploads/2016/02/sdo_6th_year_sun_2015_f.jpg", "Сонце")
]

# Додавання кожного зображення до бази даних як статті
for img_url, description in images:
    article_title = f"Стаття про {description}"
    article_description = f"Ця стаття описує {description}"
    db_manager.add_cosmic_article(article_title, article_description, img_url)

# Додавання зображення Землі до бази даних як статті
earth_img_url = "https://searchthisweb.com/wallpaper/thumb1000/main1000_earth_7680x4320_ejea5.jpg"
earth_description = "Земля"
db_manager.add_cosmic_article("Стаття про Землю", earth_description, earth_img_url)

# Отримання всіх текстових описів новин з посиланнями на зображення
all_news_with_images = db_manager.get_all_news_with_images()

# Виведення посилання на галерею
print("Див. також:")
print('<a href="http://127.0.0.1:5000/gallery" target="_blank">Галерея зображень</a>')
print()

# Виведення HTML-коду для створення посилань на зображення
for description, img_url in all_news_with_images:
    print("Опис новини:", description)
    print("https://searchthisweb.com/wallpaper/thumb1000/main1000_earth_7680x4320_ejea5.jpg")
    print(f'<a href="{img_url}" target="_blank">https://searchthisweb.com/wallpaper/thumb1000/main1000_earth_7680x4320_ejea5.jpg<img src="{img_url}" alt="{description}" style="max-width: 400px;"></a>')
    print()  # додаємо порожній рядок для розділення новин