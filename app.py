 
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/ubicacion')
def ubica():
    return render_template('ubicacion.html')

@app.route('/galeria')
def galeria():
    return render_template('portfolio-3-col.html')


@app.route('/contacto')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
