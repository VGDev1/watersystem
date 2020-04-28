from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from . import db
import json
from flask_login import login_required, current_user
from datetime import date, datetime
import _thread
from .controller import *
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


@main.route('/setting', methods=['POST'])
@login_required
def turnOn():
    waterTime = request.form.get('watertime')

    if not waterTime:
        flash('Ange bevattningstid')
        return redirect(url_for('main.control'))
    
    if waterTime:
        flash('Bevattning aktiverad')
        # Some code here to activate the relay
        global con
        con = Controller(waterTime)
        _thread.start_new_thread(con.activateWater, ())    
        data = {}
        data['logs'] = []
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%m/%d/%Y")
        try: 
            with open('log.txt', 'r') as json_file:
                data = json.load(json_file)
        except:
            print("wtf")
        finally:
            data['logs'].append({
                'event': 'activated',
                'date': current_date,
                'time': current_time,
                'duration': waterTime + "min"
            })
        with open('log.txt', 'w+') as outfile:
            json.dump(data, outfile)
        return redirect(url_for('main.control'))
        print(f"bevattning på {waterTime}")


@main.route('/turnoff', methods=['POST'])
@login_required
def turnOff():
    flash('Bevattning avavktiverad')
    con.deactivateWater()
    data = {}
    data['logs'] = []
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%m/%d/%Y")
    try: 
        with open('log.txt', 'r') as json_file:
            data = json.load(json_file)
    except:
        print("wtf")
    finally:
        data['logs'].append({
            'event': 'deactivated',
            'date': current_date,
            'time': current_time,
            'duration': '-'
        })
    with open('log.txt', 'w+') as outfile:
        json.dump(data, outfile)
    return redirect(url_for('main.control'))
    #Missing code here
    return redirect(url_for('main.control'))

@main.route('/log')
@login_required
def log():
    return render_template('log.html')

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