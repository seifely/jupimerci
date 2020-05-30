from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():
    # your code goes here - set text_description as your string plz
    text_description = 'A wizardly description'

    return (render_template('index.html') % text_description)
