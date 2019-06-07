from app import app
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()