from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    template_path = os.path.join(app.root_path, 'templates', 'index.html')
    print(f"Looking for template at: {template_path}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8082, debug=True)
