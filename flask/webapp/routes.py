from webapp import app, socketio
from flask import render_template, request
from flask_socketio import emit, namespace
import json

roomid = {}
sockets = {}
        

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/makeroom')
def makeRoom():
    return render_template('makeRoom.html')

@app.route('/joinroom')
def joinRoom():
    return render_template('joinRoom.html')

@socketio.on('connect')
def connect():
    print('User connected')

@socketio.on('disconnect')
def disconnect():
    sid = request.sid
    if sid in sockets:
        username = sockets[sid]
        roomid.pop(username)
        sockets.pop(sid)
    print('User disconnected')

@socketio.on('user_added')
def user_added(data):
    json_dict = json.loads(data)
    sid = request.sid
    
    if json_dict['username'] in roomid:
        emit('duplicate')

    sockets[sid] = json_dict["username"]
    print("User "+ str(json_dict["username"]) +" added" )
    roomid[json_dict["username"]] = {
            "username":json_dict["username"],
            "sid":str(request.sid),
            "localDesc":json_dict["localDesc"]
        }

@socketio.on('join_room')
def join_room(data):
    if data in roomid:
        emit('remote_desc_join',json.dumps(roomid[data]))
    else:
        emit('notfound')

@socketio.on('answer')
def answer(data):
    json_dict = json.loads(data)
    if json_dict['sid'] in sockets:
        sid = json_dict['sid']
        emit('set_remote',json.dumps(json_dict['answer']),room=sid)
    
