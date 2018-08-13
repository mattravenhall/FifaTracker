import update
from flask import *
app = Flask(__name__, static_url_path='/static/')

@app.route('/')
def hello(name=None):
    previous, current, future, remaining = update.run()
    return render_template('main.html', name=name, previous=previous, current=current, future=future, remaining=remaining)
