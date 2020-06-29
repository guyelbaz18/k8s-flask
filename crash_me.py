from flask import Flask, request

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def index():
    return 'To crash container go to /crash'

@app.route('/crash')
def crash_docker():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
