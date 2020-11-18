from webapp import app

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=80)


# cmd: $flask run --host=0.0.0.0 --port=80