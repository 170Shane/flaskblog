from flask import Flask, render_template, url_for

app = Flask(__name__)

# ran directly i.e.python flaskblog.py, the __name__ variable is '__main__'
# ran from another module i.e. python -m flask run, the __name__ variable is the filename i.e.'flaskblog'

dummy_data = [
    {
        'author': 'Shane Clark',
        'title': 'Blog Post 1',
        'content': 'Blog Content 1',
        'date_posted': 'March 25, 2021'
    },
    {
        'author': 'Julie Clark',
        'title': 'Blog Post 2',
        'content': 'Blog Content 2',
        'date_posted': 'March 26, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', dummy_data=dummy_data, title="Test title")  # Can pass in data to route here


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
