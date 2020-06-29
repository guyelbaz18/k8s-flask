from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'To crash container go to /crash'

@app.route('/crash')
def crash_docker():
    return oopsi

if __name__ == "__main__":
    app.run()
