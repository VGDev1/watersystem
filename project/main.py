from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from . import db
import json
from flask_login import login_required, current_user
from datetime import date, datetime
import _thread
#? from .controller import * uncomment this when run on raspberry pi
main = Blueprint('main', __name__)

data = {}
data['logs'] = []
con = None 


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/control')
@login_required
def control():
    return render_template('control.html', name = current_user.name)

def writeToLogFile(event, waterTime):
    data = {}
    data['logs'] = []
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m/%d/%Y")
    try: 
        with open('log.txt', 'r') as json_file:
            data = json.load(json_file)
    except:
        print("exception")
    finally:
        data['logs'].append({
            'event': event,
            'date': current_date,
            'time': current_time,
            'duration': waterTime
        })
    with open('log.txt', 'w+') as outfile:
        json.dump(data, outfile)


@main.route('/setting', methods=['POST'])
@login_required
def turnOn():
    waterTime = request.form.get('watertime')

    if not waterTime:
        flash('Ange bevattningstid')
        return redirect(url_for('main.control'))
    
    if waterTime:
        flash('Bevattning aktiverad')
        global con
        #? con = Controller(waterTime) uncomment when run on raspberry 
        #?_thread.start_new_thread(con.activateWater, ()) uncomment when run on raspberry   
        writeToLogFile('activated', waterTime)
        return redirect(url_for('main.control'))
        print(f"bevattning på {waterTime}")

@main.route('/turnoff', methods=['POST'])
@login_required
def turnOff():
    flash('Bevattning avavktiverad')
    global con
    if con != None:
        con.deactivateWater()
        print("deactivated")
    writeToLogFile('deactivated', '-') 
    return redirect(url_for('main.control'))

@main.route('/log')
@login_required
def log():
    return render_template('log.html')

@main.route('/camera')
@login_required
def camera():
    return render_template('camera.html')

@main.route('/json')
@login_required
def getJson():
        data = {}
        try:
            with open('log.txt', 'r') as json_file:
                    data = json.load(json_file)
        except:
            print(data)
        finally:
            return jsonify(data)
