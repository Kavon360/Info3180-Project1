"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from forms import profileform
from models import UserProfile
from werkzeug.utils import secure_filename
import time
import datetime
import random
import os
from . import db


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = profileform()
    test = [] 
    test.append("denig123"), test.append("port55"), test.append("gnome325"), test.append("jacko"), test.append("tegagek"), test.append("brim34"), test.append("hometec5"), test.append("rall45"),  test.append("hulu5"), test.append("dragon23")  
    if request.method == "POST" and form.validate_on_submit():
        firstname = form.firstname.data 
        lastname=form.lastname.data 
        email = form.email.data 
        upload = form.upload.data
        filename = secure_filename(upload.filename) 
        location = form.location.data 
        gender = form.gender.data 
        biography = form.biography.data 
        nickname = random.choice(test)
        created_on = date() 
        user = UserProfile(firstname=firstname, lastname=lastname, email=email, location=location, gender=gender, biography=biography, upload=filename, userid=nickname, created_on=created_on)
        db.session.add(user)
        db.session.commit()
        upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash("Profile was Successfuly Added")
        return redirect(url_for('profiles'))
        
    
    return render_template('profile.html', form=form)    

@app.route('/profile/<userid>')
def display(userid):
    personal = UserProfile.query.filter_by(id=userid).first()
    return render_template('personal_profile.html', user=personal)
    
@app.route('/profiles')
def profiles():
    profiles_list = UserProfile.query.all()
    return render_template('profiles.html', profiles=profiles_list)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
def date():
    return (time.strftime("%d/%m/%Y"))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
