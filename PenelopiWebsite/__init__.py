from flask import Flask, render_template, flash, redirect, url_for, session
import RPi.GPIO as GPIO
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = '2929184981'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/redon/", methods=['POST'])
def redon():
    GPIO.setmode(GPIO.BOARD)
    red = 15
    GPIO.setup(red, GPIO.OUT) 
    GPIO.output(red, True) 
    print('Web User says: red light on plz.')
    time.sleep(2)
    GPIO.output(red, False) 
    print('Penelopi says: red light is now off.')

    confirmation_message = "Red light went on. It will switch off after 2 seconds"
    return render_template('index.html', confirmation_message=confirmation_message);

@app.route("/yellowon/", methods=['POST'])
def yellowon():
    GPIO.setmode(GPIO.BOARD)
    yellow = 13
    GPIO.setup(yellow, GPIO.OUT) 
    GPIO.output(yellow, True) 
    print('Web User says: yellow light on plz.')
    time.sleep(2)
    GPIO.output(yellow, False) 
    print('Penelopi says: red light is now off.')

    confirmation_message = "Yellow light went on. It will switch off after 2 seconds"
    return render_template('index.html', confirmation_message=confirmation_message);

@app.route("/greenon/", methods=['POST'])
def greenon():
    GPIO.setmode(GPIO.BOARD)
    green = 11
    GPIO.setup(green, GPIO.OUT) 
    GPIO.output(green, True) 
    print('Web User says: green light on plz.')
    time.sleep(2)
    GPIO.output(green, False) 
    print('Penelopi says: green light is now off.')

    confirmation_message = "Green light went on. It will switch off after 2 seconds"
    return render_template('index.html', confirmation_message=confirmation_message);



if __name__ == '__main__':
    app.run(debug=True)