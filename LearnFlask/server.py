from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
import random
import time
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfljkei29!!@'
socketio = SocketIO(app,ping_timeout=20,ping_interval=10)
data = 'Test'

Connected_Users = []
#ID = {'Name','Hand'}
all_users = []
userNames = {}

class userInfo(FlaskForm):
    name = StringField('Name',[InputRequired()])
    room = StringField('Room',[InputRequired()])
    submit = SubmitField('Submit')

class game():
    score = []
    players = []
    gameRound = 0

def genDeck():
        deck = []
        nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','C','D']
        s = 0
        while s < 4:
            for i in nums:
                deck.append(i+suits[s])
            s += 1
        return deck

def genRounds():
    maxRounds = ((math.floor(52/len(all_users)))*2)-1
    x = 0
    cards = math.floor(52/len(all_users))
    roundCardCount = []
    halfwayPoint = math.ceil(maxRounds/2)
    while x < maxRounds:
        if x < halfwayPoint-1:
            roundCardCount.append(cards)
            cards -= 1
            x += 1
        else:
            roundCardCount.append(cards)
            cards += 1
            x += 1
    return roundCardCount

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['nm']
        print(name)
        return render_template('userpageV2.html',name=name)
    else:
        return render_template('home.html')

@app.route('/<username>')
def showUserProfile(username):
    return render_template('userpage.html', data=data)

@app.route('/usernameStatic')
def showUserProfileV3():
    return render_template('userpage3.html')

@app.route('/catchall')
def catchall(catchall):
    return render_template('home.html')

@app.route('/form',methods=('GET','POST'))
def formPage():
    form = userInfo()
    if form.validate_on_submit():
        return render_template('userpage3.html', data={'username':form.name.data,'room':form.room.data})
    return render_template('formPage.html',form=form)

#Testing
#@app.route('/rooms',methods=('GET','POST'))
#def formPage():
#    form = userInfo()
#    if form.validate_on_submit():
#        return redirect(url_for('showUserProfile',username='test', data={'username':form.name.data,'room':form.room.data}))
#    return render_template('formPage.html',form=form)

@app.route('/connor')
def connorUserProfile():
    return render_template('userpageV2.html')


@socketio.on('connect')
def new_connection():
    data = request.args.get('data')
    print('New connection!')
    if len(all_users) > 0:
        usernametemplist = []
        for i in all_users:
            usernametemplist.append(i['Name'])
        if data in usernametemplist:
            for i in all_users:
                if i['Name'] == data:
                    i['ID'] = request.sid
        else:
            all_users.append({'ID':request.sid,'Name':data})
    else:
        all_users.append({'ID':request.sid,'Name':data})
    print(len(all_users))
    print(all_users)

@socketio.on('disconnect')
def lost_connection():
    print('Someone Left!')
    for i in all_users:
        if i['ID'] == request.sid:
            all_users.remove(i)
    print(len(all_users))
    print(all_users)

@socketio.on('my_event')
def handle_my_data(data):
    print(data)
    emit('my_event',data,broadcast=True)

@socketio.on('my_room_event')
def handle_my_room_data(data,room):
    print(data)
    print(room)
    emit('my_room_event',data,room=room)

@socketio.on('dealCards')
def dealtheCards():
    cards = genDeck()
    random.shuffle(cards)
    #TODO - fix name below
    maxRounds = genRounds()
    cardsDealt = 0
    while cardsDealt <= maxRounds[0]:
        for i in all_users:
            data = cards.pop()
            emit('dealCards',data,room=i['ID'])
        cardsDealt += 1
    
@socketio.on('playCard')
def playtheCard(data):
    print(data)
    emit('playCard',data,broadcast=True)


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    print(username, room)
    join_room(room)
    print('Joined!')
    #emit('join_room', {'room':room,'user':username},room=room)
    emit('join', {'room':room,'user':username},room=room)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app,host='0.0.0.0',port=80)
