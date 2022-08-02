from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.x7hozwp.mongodb.net/?retryWrites=true&w=majority')
db = client.spamovie

@app.route('/')
def home():
    return render_template('index.html')

# 디비 불러오기
@app.route('/movie', methods=['GET'])
def show_movies():
    movies = list(db.movies.find({}, {'_id': False}))
    return jsonify({'all_movies':movies, 'msg':'잘 나온다!'})

# 영화 디비 내용이 들어가는 곳
@app.route('/movie', methods=['POST'])
def save_movies():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']

    doc = {
        'title': title_receive,
        'content': content_receive
    }

    db.movies.insert_one(doc)
    return jsonify({'msg':'POST 작동!', 'title_count':'title'})

# 디비 삭제가 필요하다면
@app.route('/remove', methods=['GET'])
def remove_movies():

    db.movies.delete_many({})

    return jsonify({'msg':'DB 삭제!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)