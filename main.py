# код
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/training/<prof>')
def train(prof):
    if 'строитель' in prof or 'инженер' in prof:
        img = 'ing.png'
        name_of_picture = 'Инженерные тренажёры'
    else:
        name_of_picture = 'Научные симуляторы'
        img = 'sci.png'
    return render_template('content.html', title=prof, name_of_picture=name_of_picture)


@app.route('/index')
def lol():
    return render_template('content.html', title='title', img='ing.png', name_of_picture='lol')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')