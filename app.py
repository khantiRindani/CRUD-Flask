from flask import Flask, render_template
from data import Blogs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html',blogs=Blogs())

if __name__=='__main__':
    app.run(debug='true')

