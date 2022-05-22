from random import randint
from flask import render_template, flash, redirect, url_for, request, jsonify
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User



send_back = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
ship_loc = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]

hold_gen_ship_loc = 0

# not perfect, in fact, it leaves win % extremely low
def rand_5_ships():
    count =0
    for i in range(len(ship_loc)):
        ship_loc[i]=randint(0,1)
        if ship_loc[i] == 1:
            count = count +1
        if count == 5:
            break
    
    count_1s = 0
    for i in range(len(ship_loc)):
        if ship_loc[i] == 1:
            count_1s = count_1s + 1
    if count_1s < 5:
        need_patch = 5 - count_1s
        while need_patch > 0:
            count_tmp = 0
            while count_tmp>0:
                if ship_loc[15-count_tmp] == 0:
                    ship_loc[15-count_tmp] = 1
                    need_patch = need_patch - 1
                    if need_patch <= 0:
                        break

    #print(ship_loc)

@app.route('/')
@app.route('/index')
@login_required
def index():
    global send_back            # without 'global', it won't work
    global ship_loc
    global hold_gen_ship_loc
    send_back = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]        # when refresh page (restart), clear cache
    ship_loc = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
    hold_gen_ship_loc = 0
    return render_template('index.html', title='Game')








# receiving AJAX json
@app.route('/testGet',methods=['GET'])
def testGet():
    #fake_map = "0100100110000011"
    result = request.args.get('result')
    
    global hold_gen_ship_loc
    if hold_gen_ship_loc == 0:
        rand_5_ships()
        hold_gen_ship_loc =1

    if result[0] == '1' and ship_loc[0] == 1:
        send_back[0]='1'
    if result[1] == '1' and ship_loc[1] == 1:
        send_back[1]='1'
    if result[2] == '1' and ship_loc[2] == 1:
        send_back[2]='1'
    if result[3] == '1' and ship_loc[3] == 1:
        send_back[3]='1'
    if result[4] == '1' and ship_loc[4] == 1:
        send_back[4]='1'
    if result[5] == '1' and ship_loc[5] == 1:
        send_back[5]='1'
    if result[6] == '1' and ship_loc[6] == 1:
        send_back[6]='1'
    if result[7] == '1' and ship_loc[7] == 1:
        send_back[7]='1'
    if result[8] == '1' and ship_loc[8] == 1:
        send_back[8]='1'
    if result[9] == '1' and ship_loc[9] == 1:
        send_back[9]='1'
    if result[10] == '1' and ship_loc[10] == 1:
        send_back[10]='1'
    if result[11] == '1' and ship_loc[11] == 1:
        send_back[11]='1'
    if result[12] == '1' and ship_loc[12] == 1:
        send_back[12]='1'
    if result[13] == '1' and ship_loc[13] == 1:
        send_back[13]='1'
    if result[14] == '1' and ship_loc[14] == 1:
        send_back[14]='1'
    if result[15] == '1' and ship_loc[15] == 1:
        send_back[15]='1'

    print("ship_loc : ",ship_loc)
    #print("result   : ",result)
    #print("send_back: ",send_back)


    return jsonify({'status':True})
 
if __name__ == '__main__':
    app.run()



# AJAX send back
@app.route("/dataFromAjax",methods=["GET","POST"])
def dataFromAjax():
    info = dict()
    info['slot_0'] = send_back[0]
    info['slot_1'] = send_back[1]
    info['slot_2'] = send_back[2]
    info['slot_3'] = send_back[3]
    info['slot_4'] = send_back[4]
    info['slot_5'] = send_back[5]
    info['slot_6'] = send_back[6]
    info['slot_7'] = send_back[7]
    info['slot_8'] = send_back[8]
    info['slot_9'] = send_back[9]
    info['slot_10'] = send_back[10]
    info['slot_11'] = send_back[11]
    info['slot_12'] = send_back[12]
    info['slot_13'] = send_back[13]
    info['slot_14'] = send_back[14]
    info['slot_15'] = send_back[15]

    return jsonify(info)

if __name__ == '__main__':
    app.run()





# receive AJAX 'win_or_not'
@app.route('/testGet_win',methods=['GET'])
def testGet_win():
    win_or_not = int(request.args.get('win_or_not'))
   
    #print("win_or_not : ",win_or_not)


    current_user.counts_plusplus(win_or_not)

    db.session.commit()


    return jsonify({'status':True})
 
if __name__ == '__main__':
    app.run()


# AJAX send back game record
@app.route("/dataFromAjax_top5",methods=["GET","POST"])
def dataFromAjax_top5():
    all_user = User.query.all()
    print(all_user)

    all_time_high = 0.0
    all_time_high_name = ''

    for v in all_user:
        #print(v.id, v.username, v.wins_count, v.lost_count)
        if v.wins_count == None or v.lost_count == None:
            win_percentage = 0
        else:
            win_percentage = v.wins_count/(v.wins_count+v.lost_count)
        
        if win_percentage>all_time_high:
            all_time_high = win_percentage
            all_time_high_name = v.username
    
    current_user
            


    info = dict()

    info['name_0'] = all_time_high_name
    info['percentage_0'] = all_time_high
    info['percentage_1'] = current_user.wins_count/(current_user.wins_count+current_user.lost_count)

    #print(info)
    return jsonify(info)


if __name__ == '__main__':
    app.run()






@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:       # if already login, no need, jump to index
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username  or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Sign in", form = form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, wins_count=0, lost_count=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)