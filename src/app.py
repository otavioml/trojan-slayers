from flask import Flask, render_template
import os

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run