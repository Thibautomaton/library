# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, url_for, redirect, render_template
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY']="ouistiti"

@app.route("/", methods=("GET", "POST"))
def index():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=' '

        #return redirect(url_for('nexit', name = name))
    return render_template('nameform.html', form=form, name = name)


@app.route("/nexit/<name>")
def nexit(name):
    return render_template("nexit.html", name=name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
