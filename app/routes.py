from app import app

@app.route('/')
def index():
    return 'This works even after refactoring :)'

@app.route('/favorite')
def fav_five():
    return 'This is the favorites endpoint!'
