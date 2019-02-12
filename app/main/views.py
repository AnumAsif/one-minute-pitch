from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Category, User, Pitch
# from .forms import ReviewForm,UpdateProfile
from .. import db
from flask_login import login_required, current_user
# import markdown2

@main.route('/')
def index():
    categories = Category.query.all()
    add_category = request.args.get('add_category')
    if add_category:
        if add_category in categories:
            message="Category already exist"
        else:
            category = Category(name = add_category)
            db.session.add(category)
            db.session.commit()
            message = "Category added!! Go ahead and pitch in the created category"
            categories = Category.query.all()
        add_category=""
        return render_template('index.html',categories = categories, message=message)

    return render_template('index.html',categories = categories)

@main.route('/pitch/<category_id>', methods = ["GET","POST"])
@login_required
def pitch(category_id):
    category = Category.query.filter(Category.id == category_id).first()
    categoryName = category.name
    add_pitch= request.args.get('add_pitch')
    if add_pitch:
        user = User.query.filter(User.id == current_user.id).first()
        user_id=user.id
        pitch = Pitch(message = add_pitch, category_id=category_id, user_id = user_id )
        db.session.add(pitch)
        db.session.commit()
        message = "Added successfully"
        pitches = Pitch.query.filter(Pitch.category_id == category_id).all()
        return render_template('pitches.html', pitches = pitches, category= categoryName, message = message)
    pitches = Pitch.query.filter(Pitch.category_id == category_id).all()
    return render_template('pitches.html', pitches = pitches, category= categoryName)



@main.route('/pitch/<category_id>', methods=["GET","POST"])
@login_required
def new_pitch(category_id):
    category = Category.query.filter(Category.id == category_id).first()
    categoryName = category.name
    message= request.args.get('add_pitch')
    if message:
        user_id = User.query.filter(User.id == current_user.id).first()
        pitch = Pitch(message=message, category_id=category_id,user_id = user_id)
        message = user_id+message+category_id
        db.session.add(pitch)
        db.session.commit()
        message = "Added successfully"
        pitches = Pitch.query.filter(Pitch.category_id == category_id).all()
        return render_template('pitches.html', pitches = pitches, category= categoryName, message = message)
    pitches = Pitch.query.filter(Pitch.category_id == category_id).all()
    return render_template('pitches.html', pitches = pitches, category= categoryName)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
