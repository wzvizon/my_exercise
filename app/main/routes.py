from flask import render_template, Blueprint, request, flash, redirect, url_for
from app import db
from app.main.forms import SignupForm
from app.models import User, City, Forecast
from sqlalchemy.exc import IntegrityError

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and try again.'.format(
                form.username.data), 'error')
    return render_template('signup.html', form=form)


@bp_main.route('/users/', methods=['GET'])
def users():
    user_list = User.query.all()
    return render_template("users.html", users=user_list)


@bp_main.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a city to search for")
            return redirect('/')
        results = Forecast.query.join(City). \
            with_entities(City.city_id, City.city, Forecast.forecast_datetime, Forecast.forecast, Forecast.comment).\
            filter(City.city.contains(term)).all()
        if not results:
            flash("No city found with that name.")
            return redirect('/')
        return render_template('search_results.html', results=results)
    else:
        return redirect(url_for('main.index'))
