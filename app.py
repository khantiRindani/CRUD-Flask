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

@app.route('/blog<int:id>')
def blog(id):
    if(id>len(Blogs())):
        return "Invalid URL"
    return render_template('blog.html',blog=Blogs()[id-1])

if __name__=='__main__':
    app.run(debug='true')

