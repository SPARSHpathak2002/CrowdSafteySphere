# app.py
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    try:     
        subprocess.run(['python', 'temp.py'], check=True)
        result = "Script executed successfully!"
    except subprocess.CalledProcessError as e:
       
        result = f"Error: {e}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
