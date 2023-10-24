from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite')
def fav_five():
    fav_colors = [
        {
            'color': 'blue',
            'bs_color': 'primary'
        },
        {
            'color': 'green',
            'bs_color': 'success'
        },
        {
            'color': 'red',
            'bs_color': 'danger'
        },
        {
            'color': 'yellow',
            'bs_color': 'warning'
        },
        {
            'color': 'teal',
            'bs_color': 'info'
        },
    ]
    return render_template('colors.html', favorites=fav_colors)
