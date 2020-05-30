from flask import Flask, render_template
from wizardGen import make_Text, get_Var

app = Flask(__name__)
@app.route('/')

def index():
    pronoun = ["He", "She", "They"]
    pn = get_Var(pronoun)
    text_description = make_Text(pn)

    return (render_template('index.html') % text_description)
