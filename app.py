from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Підключення до MongoDB

# Встановлюємо базу даних та колекцію MongoDB
db = client['mydatabase']
collection = db['mycollection']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')  # Отримання тексту з форми
        document = {'text': text}  # Створення документу для збереження в MongoDB
        collection.insert_one(document)  # Збереження документу в колекції MongoDB

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
