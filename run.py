from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)
app.config['DEV'] = True
app.config['ASSETS_ROOT'] = '/static/assets'


@app.route('/index.html')
@app.route('/index')
@app.route('/')
def index():
    """ Main route """
    return render_template('home/index.html', segment='index')

@app.route('/live_trends.html')
def live_trends():
    return render_template('home/live_trends.html', segment='live_trends')


if __name__ == "__main__":
    app.run(debug=app.config['DEV'])