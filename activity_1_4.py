from flask import Flask, render_template_string
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
moment = Moment(app)
Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
    # HTML template as a string
    template = '''
    {% extends "base.html" %}
    {% import "bootstrap/wtf.html" as wtf %}

    {% block title %}Flasky{% endblock %}
    <head>
        {{ moment.include_moment() }}  <!-- Include moment.js -->
    </head>
    {% extends "bootstrap/base.html" %}

    {% block title %}Flasky{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle"
                        data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">Flasky</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/">Home</a></li>
                </ul>
            </div>
        </div>
    </div>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="page-header">
            <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
        </div>
        <p>The local date and time is {{ moment(current_time).format('LLLL') }}.</p>
        <p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
        {{ wtf.quick_form(form) }}
    </div>
    {% endblock %}

    '''
    return render_template_string(template, name='Malek', current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)