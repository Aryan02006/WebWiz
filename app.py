from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Login.html')

# Initialize Flask app
if __name__ == '__main__':
    app.run(debug=True)
