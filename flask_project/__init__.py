from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length



app = Flask(__name__)
app.config['SECRET_KEY'] = '2929184981'

@app.route("/", methods=['GET', 'POST'])
def about():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username
        print('valid')
        return redirect('/result')
    else:
        print('not valid')
    return render_template('Index.html', title='Control the Pi', form=form)

@app.route("/result", methods=['GET', 'POST'])
def hello():
    try:
        username = session['username'] 
        return render_template('Result.html', title='Home', username=username)
    except:
        return render_template('Result.html', title='Home', username='none')


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])



if __name__ == '__main__':
    app.run(debug=True)