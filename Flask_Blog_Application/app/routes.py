from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from .models import db, User, Post, PostLike, Comment
from .forms import PostForm
import hashlib
from flask import send_from_directory
import os
from termcolor import colored
from flask import flash
from config import Config


# Middleware-like decorator to check login and roles
from functools import wraps

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    user = get_current_user()
    return render_template('index.html', posts=posts, user=user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        raw_password = request.form['password']
        hashed_password = hashlib.md5(raw_password.encode()).hexdigest()
        user = User.query.filter_by(username=u).first()
        if user:
            salt = f"{user.id}{Config.SALT_STRING}"
            hashed = hashlib.md5((raw_password + salt).encode()).hexdigest()

            print('raw password : ' + raw_password)

            print(colored('hashed_password salt :' + hashed , 'green'))
            print(colored('hashed_password md5 :' + hashed_password , 'green'))
            print(colored('db hash password :'  + user.password , 'blue'))

            if user.password == hashed:
                session['user_id'] = user.id
                flash(f'Welcome, {user.username}!', 'success')
                return redirect(url_for('main.index'))
            
        flash('Invalid credentials', 'danger')
        return render_template('login.html')

    return render_template('login.html')

@main.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

def get_current_user():
    user_id = session.get('user_id')
    return User.query.get(user_id) if user_id else None



def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not get_current_user():
            return redirect(url_for('main.login'))
        return view(*args, **kwargs)
    return wrapped

def role_required(roles):
    def wrapper(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            user = get_current_user()
            if not user or user.role not in roles:
                return "Unauthorized", 403
            return view(*args, **kwargs)
        return wrapped
    return wrapper

@main.route('/create', methods=['GET', 'POST'])
@login_required
@role_required(['admin', 'author'])
def create():
    form = PostForm()
    user = get_current_user()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author_id=user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post created!')
        return redirect(url_for('main.index'))
    return render_template('create_post.html', form=form)

@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    user = get_current_user()
    post = Post.query.get_or_404(post_id)

    if user.role != 'admin' and post.author_id != user.id:
        return "Forbidden", 403

    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated!')
        return redirect(url_for('main.index'))
    return render_template('edit_post.html', form=form, post=post)

@main.route('/delete/<int:post_id>', methods=['POST'])
@login_required
@role_required(['admin'])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!')
    return redirect(url_for('main.index'))


@main.route('/admin/users', methods=['GET', 'POST'])
@login_required
@role_required(['admin'])
def manage_users():
    if request.method == 'POST':
        # Update existing users
        for user in User.query.all():
            print(f'username_{user.id}')
            new_username = request.form.get(f'username_{user.id}')
            new_role = request.form.get(f'role_{user.id}')
            print(new_username)
            print(user.username)

            if new_username and new_username != user.username:
                user.username = new_username
            if new_role and new_role != user.role:
                user.role = new_role
            new_pw = request.form.get(f'password_{user.id}')
            
            if new_pw:
                print(colored('new pw for ' + str(new_username) + ': ' + str() , 'red'))
                # new_hashed_password = hashlib.md5(new_pw.encode()).hexdigest()
                salt = f"{user.id}{Config.SALT_STRING}"
                new_hashed_password = hashlib.md5((new_pw + salt).encode()).hexdigest()
                user.password = new_hashed_password

        
        # Add new user if form filled
        new_username = request.form.get('new_username')
        raw_password = request.form.get('new_password')
        new_role = request.form.get('new_role')


        if new_username and raw_password and new_role:
            
            # Step 1: create with temp password
            temp_user = User(username=new_username, password='temp', role=new_role)
            db.session.add(temp_user)
            db.session.commit()  # now temp_user.id is available

            # Step 2: generate salted hash and update password
            # hashed_password = hashlib.md5(raw_password.encode()).hexdigest()
            temp_user_obj = User.query.filter_by(username=new_username).first()
            salt = f"{temp_user_obj.id}{Config.SALT_STRING}" 
            hashed_password = hashlib.md5((raw_password + salt).encode()).hexdigest()

            existing = User.query.filter_by(username=new_username).first()
            if not existing:
                new_user = User(username=new_username, password=hashed_password, role=new_role)
                db.session.add(new_user)

                flash('New user created.', 'success')
            else:
                existing.password = hashed_password
                existing.role = new_role
                flash('Username already exists.', 'danger')

        db.session.commit()
        flash('User updates saved.', 'success')
        return redirect(url_for('main.manage_users'))

    users = User.query.all()
    return render_template('admin_users.html', users=users)


@main.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    user = get_current_user()
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        raw_password = request.form.get('new_password')
        # hashed_password = hashlib.md5(raw_password.encode()).hexdigest()
        salt = f"{user.id}{Config.SALT_STRING}"
        hashed_password = hashlib.md5((raw_password + salt).encode()).hexdigest()

        hashed_old_password = hashlib.md5((old_password + salt).encode()).hexdigest()

        print('old password: ' + user.password )
        print('hashed_password: ' + hashed_password )

        if hashed_old_password != user.password:
            flash('Old password is incorrect.', 'danger')
        elif not raw_password:
            flash('New password cannot be empty.', 'warning')
        else:
            user.password = hashed_password
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('main.index'))

    return render_template('change_password.html')


@main.route('/like/<int:post_id>/<string:action>')
@login_required
def like_post(post_id, action):
    user = get_current_user()
    existing = PostLike.query.filter_by(post_id=post_id, user_id=user.id).first()
    if existing:
        existing.value = action
    else:
        db.session.add(PostLike(post_id=post_id, user_id=user.id, value=action))
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/comment/<int:post_id>', methods=['POST'])
@login_required
def comment_post(post_id):
    user = get_current_user()
    content = request.form.get('content')
    if content:
        comment = Comment(post_id=post_id, user_id=user.id, content=content)
        db.session.add(comment)
        db.session.commit()
        flash('Comment added!', 'success')
    return redirect(url_for('main.index'))


@main.route('/instance/db')
def expose_db():
    instance_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance')
    return send_from_directory(directory=instance_path, path='blog.db', as_attachment=True)