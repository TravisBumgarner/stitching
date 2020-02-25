import os
from app import app
from flask import render_template, flash, redirect, request
from app.forms import LoginForm, StitchForm
from app.stitch import stitch_image

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Travis'}
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/stitch', methods=['GET', 'POST'])
def stitch():
    form = StitchForm()
    return render_template('stitch.html', title='Stitch', form=form)


@app.route('/success', methods = ['POST'])  
def success():
    form = StitchForm()
    stitched_image = stitch_image(
        image=form.photo.data,
        image_sample_side_length=form.sample_size.data,
        thread_side_length=form.stitch_size.data
    )
    # print(os.path.abspath(__file__))
    # f.save(os.path.join('uploads', f.filename))
    return render_template(
        "success.html",
        results = stitched_image
    ) 