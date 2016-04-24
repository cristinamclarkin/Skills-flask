from flask import Flask, render_template, request
"""Request modhttp://flask.pocoo.org/"""
import jinja2

app = Flask(__name__)

app.secret_key = 'Cmc625'

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route('/')
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template('index.html')

@app.route('/application-form')
def complete_form():
    """Displays form and allows user to enter information in fields" provided"""

    return render_template('application-form.html')

@app.route('/application-response', methods=["post"])
def submit_form():

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    salary_requirement = request.form.get('salaryrequirement')
    job = request.form.get('job')

    return render_template('application-response.html', firstname = firstname, lastname = lastname, job = job, salary = salary_requirement)


if __name__ == "__main__":
    app.run(debug=True)
