from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Open the Calculator app when the root URL is accessed
    subprocess.Popen([''win', 'r','enter''])  # This will open Calculator on Windows
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
