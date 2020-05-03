from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfljkei29!!@'
socketio = SocketIO(app)
data = 'Test'

@app.route('/')
def index():
    myServersideList = ['Connor','4D']
    return render_template('index.html',myList=myServersideList)

@socketio.on('connect')
def new_connection():
    print('New connection!')

@socketio.on('my_event')
def handle_my_data(data):
    print(data)
    data = 'Server Message'
    emit('my_event',data)

@socketio.on('custom_event')
def send_myFeedback(data):
    mynewList = ['Connor','Sarah']
    emit('custom_event',mynewList)
    print('Sent!')

@socketio.on('my_button')
def printMyData(data):
    print(data)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)